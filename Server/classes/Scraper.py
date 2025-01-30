import re
import requests
from lxml import html
from ModelAPI import ModelAPI
from DB import DB
from ID import ID

class Scraper:
    numberOfTokens = 0
    #db = DB()
    def __init__(self):
        pass
        
    id_uniq = ID()


# Scraping the HTML URLs from the blog page
    def fetch_text_only_a_tags(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        try:
            response = requests.get(url, headers=headers, timeout=10)  # Adding timeout for safety
            print(f"Status Code: {response.status_code}")  # Print the status code of the response

            if response.status_code in [200, 403]:  # Handle both 200 OK and 403 Forbidden
                tree = html.fromstring(response.content)
                a_tags = tree.xpath('//a')
                text_only_a_tags = [tag for tag in a_tags if self.is_text_only(tag)]
                print(f"Found {len(text_only_a_tags)} text-only <a> tags.")
                return text_only_a_tags
            else:
                print(f"Unexpected response status: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def is_text_only(self, tag):
        # Check if the tag contains only text and no other elements
        return tag.text is not None and len(tag) == 0 or any(child.tag == 'span' for child in tag)
    
# For Testing purposes  ##################
    def save_text_only_a_tags(self):
        a_tags =  self.fetch_text_only_a_tags()
        if a_tags:
            with open(self.filename, 'w', encoding='utf-8') as f:
                for tag in a_tags:
                    f.write(html.tostring(tag, encoding='unicode') + "\n")
            print(f"Text-only <a> tags saved to {self.filename}")
        else:
            print("Failed to save text-only <a> tags")


# FLOW :: the scraper will extract the urls from the html file and then pass them to the model api to check if it's an article url or not. If it's an article url then it will be stored in the array of urls. If it's not an article url then it will be ignored. 
# @Return True or False if the tag is article url or not
    def checkArticleURL(self,modelV, tag,prompt):
        self.modelV = modelV
        model_api = ModelAPI(self.modelV)
        self.tag = tag
        full_res =  model_api.api_req(prompt, self.tag)
        message_res = model_api.get_message(full_res)
        total_tokens = model_api.get_tokens(full_res)
        self.numberOfTokens = total_tokens + self.numberOfTokens
        return message_res
        #print(message_res)

######################### Improvement:: use fining tuning to make the model more accurate or chatgpt4 ############################# or use prompt
# Extracting the URLs for all articles from the blog page. ## This function should be executed for each blog page url to extract urls of articles.
# @Return: Array of URLs for articles
     
    def extractURLs(self,url):
        a_tags = self.fetch_text_only_a_tags(url)
        print(a_tags)
        try:
            if a_tags:
                urls = []
                for tag in a_tags:
                    if html.tostring(tag, encoding='unicode').replace(" ", "") == "" :
                        continue
                    prompt = "You are smart crawler.Return True or False.Return True if <a> is a link for an article or has text that is an article title, the text have to be more than one word. Search in the attributes if there is a title text for an article or in the text inside the <a> element."
                    result = self.checkArticleURL("gpt-4o-mini", html.tostring(tag, encoding='unicode'),prompt)
                    if result == "True":
                        article_url = self.validateURL("gpt-4o-mini", tag.attrib['href'],url)
                        urls.append(article_url)
                        #print(result)
                        print(html.tostring(tag, encoding='unicode'))
                        print("Number of tokens used: ", self.numberOfTokens)
                    elif (result != "False") and (result!= "True"):
                        #print(result)
                        #print(html.tostring(tag, encoding='unicode'))
                        print("Not Valid output from Chatgpt")    
                    else:
                        print("Not an article URL")
                return urls
            else:
                print("Failed to extract URLs : a_tags is empty")
        except Exception as e:
            print("Error extracting URLs: ", e)
            return None
            

    # Validation of url and rewrite the url if it's not valid, for example /cat?23 will be written with full url of the main url of the website
    # @Return: Valid URL with full path
     
    def validateURL(self, modelV, check_URL,url):
        
        model_api = ModelAPI(modelV)
        req = model_api.api_req("Extract and Provide the base URL from the following link: For example, if the link is https://www.chargebee.com/blog/improve-customer-experience/, I need the base url return 'https://www.chargebee.com/. DON'T RETURN any ouptut except base_url", url)
        main_domain = model_api.get_message(req)
        req2 = model_api.api_req("Check if the URL is valid or not.RETURN True if it's valid link and RETURN False if it's not valid. DON'T RETURN any output Except True or False. example for not valid link : /blog/author/arijit-bose/ example for valid link: https://www.chargebee.com/blog/category/growth/", check_URL)
        check_validation_url = model_api.get_message(req2)
        if check_validation_url != "True" or check_validation_url != "False":
            print("Not Valid output from Chatgpt")
        if check_validation_url == "False":
            check_URL = check_URL.replace("/", "",1)
            valid_url = main_domain + check_URL
        #print(valid_url)
        else:
            return check_URL
        return valid_url
        


    # Generate the pages of the blog from the first page to the last page, if the url is like this : https:\\chargebee.com\blog\page\2 then the function will generate the pages from 2 to the last page.
    # @Return: Array of URLs for pages
     
    def GeneratePagesOfBlog(self,base_url,first_page, last_page) :
        base_url = re.sub(r'\d+$', '', base_url)
        urls=[]
        for i in range(first_page,last_page+1):
            urls.append(base_url + str(i))
        return urls
    
    # Generate the pages of the blog from the first page to the last page, if the url is like this : https:\\chargebee.com\blog\?o=10 then the function will generate the pages
    # @Return: Array of URLs for pages
     
    def GeneratePagesOfBlogFromDB(self,base_url,first_amout, last_amout, increment) :
        urls=[]
        start = first_amout
        base_url = re.sub(r'\d+$', '', base_url)
        for i in range(first_amout,last_amout+1, increment):
            urls.append(base_url + str(start))
            start = start + increment
        return urls


# This function will define if the url is for a pagination page or not, if it's a pagination page then it will generate the pages of the blog, if it's not a pagination page then it will generate the pages of the blog from the DB.
# @Return: Array of URLs for pages and define if the url is for a pagination page or not
    def Define_Generate_BlogPages(self, modelV, url, first_val,last_val,increment):
        pages_urls = []
        model_api = ModelAPI(modelV)
        req =   model_api.api_req("Return JUST True or False or # sign as Output. RETURN True only if the url is for a pagination page in this style For example : https://gocardless.com/resources/3/ this link is true, This link https://paypal.com/blog/3/ is true as well. Return false if the link is fetching data using a parameter. for example https://gocardless.com/resources/?o=10 this links is false and has parameter ?o=10. if the link is not both, Return # sign.", url)
        result =   model_api.get_message(req)
        if result == "True":
            pages_urls =   self.GeneratePagesOfBlog(url,first_val,last_val)
        elif result == "False":
            pages_urls =   self.GeneratePagesOfBlogFromDB(url,first_val,last_val,increment)
        else:
            print("Not Valid Blog Page URL !!!!")    
        return pages_urls
    

# Store the URLs of the blog pages in the DB.
# @Return: True if the function is done successfully, False if there is an error
    def StoreBlogPagesURLs(self, pages_urls,db):
            try:
                
                #exclude the existing urls of the blog pages
                for url in pages_urls:
                    if db.check_blog_page_url_exists(url):
                        continue
                    id =   self.id_uniq.generate_unique_id()
                    data ={
                        "id": id ,
                        "status": 0,
                        "url": url
                    }
                    #  set_blog_page_url(self, website_id,  blog_page_data):
                    
                    db.set_blog_page_url(data)
                print("successfully updated.")
                return True
            except Exception as e:
                print("Error updating the blog pages urls in the DB: ", e)
                return False

   

   


    
    #Function to scrap each article page
    # @Return: Array of tuples containing the tag and the text
    def scrape_content(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Continue if HTTP status code is 200

            tree = html.fromstring(response.content)
            xpath_query = '//h1|//h2|//h3|//h4|//h5|//h6|//p|//span|//ul|//ol|//li'
            content = [f"{element.tag}: {element.text_content().strip()}" for element in tree.xpath(xpath_query)]
            return '\n'.join(content)

        except requests.HTTPError as e:
            print(f"HTTP Error for URL {url}: {e}")
            return []
        except requests.Timeout as e:
            print(f"Timeout Error for URL {url}: {e}")
            return []
        except requests.RequestException as e:
            print(f"Request Exception for URL {url}: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []



# Parse the content of the article page into an array of paragraphs and headers
    def tokenonize_content(self,text):
        lines = text.split('\n')
        content_array = []
        current_header_content = ''

        for line in lines:
            if line.startswith(('h1:', 'h2:', 'h3:', 'h4:', 'h5:', 'h6:')):
                # If there's content in the current header, append it to the array
                if current_header_content:
                    content_array.append(current_header_content.strip())
                current_header_content = line.split(':', 1)[1].strip() + ' '
            elif line.startswith('p:'):
                current_header_content += line.split(':', 1)[1].strip() + ' '

        # Append the last header content if it exists
        if current_header_content:
            content_array.append(current_header_content.strip())

        return content_array







    # Flow for the full function : extract blog pages urls > store it in temp json file > scrap each Blog page and store the articles in the temp json file > scrap each url in the array of articles for each url page > when it's done change the status for this blog url to 1 which is scraped > the result of scraping page should be stored [Take a decision how you will store it in DB or temp on server ! it's important to save the results for future use].
    ############# This flow should be tracked with try and catch to detect any bug or error. The flow should support if there is an error with api request for chatgpt, the tool will run the function again until the request is done successfully. Even for each Url of articles, 
    # Even if the single url of article didn't scraped for api issues, then the code will just know this url not scraping all articles again.  Design a log for errors to detect errors of the tool, this log will be stored in temp DB#####################


# Store the URLs of the blog pages in the DB.
    def Generate_Store_BlogURLs(self,url,first_val,last_val,increment,db):
        #extract blog pages urls > store it in the DB
        pages_urls =   self.Define_Generate_BlogPages("gpt-4o-mini",url,first_val,last_val,increment)
        self.StoreBlogPagesURLs(pages_urls,db)
        return True

# Store articles urls of each blog page in the DB
# Flow : fetch all blog pages urls from the DB with status 0> for each blog page url, extract urls  > update status of blog page to 1 > store the articles urls in the DB

############ Function works fine, but the extractURLs function should be improved to trace when it freezes and to continue from the last url it stopped at and using finate tuning to improve the output of the AI model ############################
     
    def Generate_Store_ArticlesURLs(self,db):
        unsraped_blog_pages_urls =  db.get_all_unscraped_blog_urls()
        for url in unsraped_blog_pages_urls:
            print("URL OF BLOG #### "+url)
            articles_urls =  self.extractURLs(url)
                # Error because of id
           
            try:
                db.update_blog_page_url(url, {"status":1})
            except:
                print("Error in updating blog pages url")
                return False
            
            for article_url in articles_urls:
                print("URL OF ARTICLE #### "+article_url)
##################### Test if this article url is already stored in the DB or not, if it's already stored then continue to the next article url ******************************* ##############################
                if  db.check_article_url_exists(article_url):
                    continue
                #set_article(self,website_id, article_data)
                try : 
                    ############################# Error because of id #########################################
                    id = self.id_uniq.generate_unique_id()
                    db.set_article({"article_id":id ,"status": 0,"tokening":0,"summurized":0 ,"finite_tuning":0,"article_url": article_url, "blog_page_url": url, "scraped_data": None})
                except:
                    print("Error in storing articles urls")
                    continue    
        return unsraped_blog_pages_urls



# Scrap each article page and store the articles in the DB
# Flow : fetch all articles urls from the DB with status 0>  for each article url, scrap the article page > update status of article to 1 > store the article in the DB
    def scrape_store_articles(self,db):
        unscraped_articles_urls =   db.get_all_unscraped_articles()
        print(unscraped_articles_urls)
        #unscraped_articles_urls = self.db.get_all_unscraped_articles_specific_website(website_id)
        for url in unscraped_articles_urls:
            try:
                
                scraped_data =   self.scrape_content(url)
                tokens_arr =   self.tokenonize_content(scraped_data)
                tokens_structure =   self.build_tokens_structure(tokens_arr)
            except:
                print("Error in scraping articles" + url)
                continue
            try:
                
                db.update_article(url, {"status": 1, "scraped_data": scraped_data, **tokens_structure})
                print("Stored successfully"+ url)
                
            except:
                print("Error in storing articles in DB" + url)
                continue
        return True
            

#tokens_key_value_pairs  = scraper.generate_tokens_key_value_pairs(tokens_arr)
#article_data = {"status": 1, "scraped_data": "your_scraped_data_here", **tokens_key_value_pairs}

    def build_tokens_structure(self,tokens_arr):
    # Create key-value pairs for each token
         return {f"token{i+1}": token for i, token in enumerate(tokens_arr)}
    

# run extractUrls function for each blog page url



