import asyncio
from Prompts import Prompts
from ModelAPI import ModelAPI
from ID import ID

class Summarize : 
    
    def __init__(self):
        pass
    
    prompt = Prompts()
    gpt3= ModelAPI("gpt-4o-mini")
    gpt4_preview = ModelAPI("gpt-4o-mini")
    id = ID()


   #Extract values of tokens from the article data
    async def process_tokens(self, data):
        tokens = []
        # Create a sorted list of keys that start with 'token', are followed by a number, and are not 'tokenning'
        sorted_keys = sorted(
            (key for key in data.keys() if key.startswith('token') and key not in ['tokening']),
            key=lambda x: int(x[len('token'):])  # Correctly slicing out the number part
        )

        # Loop through the sorted keys
        for key in sorted_keys:
            # Process each token (For example, append to list)
            tokens.append(data[key])

        return tokens



    async def get_all_unsummarized_articles(self,db):
        urls = db.get_all_unsummurized_articles()
        return urls


    async def summarize(self,text):
        prompt = self.prompt.SUMMARIZE_TEXT
        res = self.gpt4_preview.api_req(prompt,text)
        message =  self.gpt4_preview.get_message(res)
        return message
    

    async def get_table_content(self,text):
        prompt= self.prompt.TABLE_CONTENT
        res = self.gpt3.api_req(prompt,text)
        message = self.gpt3.get_message(res)
        return message

    def store_summarized_article(self,data,db):
        db.store_summurized_article(data)

    async def generate_Questions(self,text):
        prompt = self.prompt.WRITE_QUESTIONS
        res = self.gpt4_preview.api_req(prompt,text)
        message =  self.gpt4_preview.get_message(res)
        return message
    
    def generate_Informations(self,text, questions):
        prompt = self.prompt.GENERATE_INFORMATION_FOR_SUMMURIZED_ARTICLE + questions
        res = self.gpt4_preview.api_req(prompt,text)
        message = self.gpt4_preview.get_message(res)
        return message
    
    def generate_categories(self,text):
        prompt = self.prompt.CATEGORIZE_TABLE_CONTENT
        res = self.gpt3.api_req(prompt,text)
        message =  self.gpt3.get_message(res)
        return message
    
    def generate_title(self,text):
        prompt = self.prompt.GENERATE_TITLE
        res = self.gpt3.api_req(prompt,text)
        message =  self.gpt3.get_message(res)
        return message
    
    async def HTML_Converter(self,text):
        prompt = self.prompt.HTML_Converter
        res = self.gpt3.api_req(prompt,text)
        message =  self.gpt3.get_message(res)
        return message
    
    async def summurize_res(self,text):
        prompt = self.prompt.SUMMURIZE_RES
        res = self.gpt4_preview.api_req(prompt,text)
        message = self.gpt4_preview.get_message(res)
        return message

    async def summurize_algorithm(self,db):
            summaries = []
            table_contents = []
            generated_questions_list = []
            print("Summurizing : get all unsummarized articles" + "\n")
            #data,urls = await self.get_all_unsummarized_articles(db)
            urls = await self.get_all_unsummarized_articles(db)
            print("Summurizing : get all unsummarized articles is Done" + "\n")
            for url in urls:
                print("Summurizing : get article by url" +url+ "\n")
                #Get all the data of the article as a dictionary
                data_of_article = db.get_article_by_url(url)
                tokens = await self.process_tokens(data_of_article)
                print("Summurizing : 3 functions are processing" + "\n")
                for token in tokens:

                    try :
                        summary =  self.summarize(token)
                        table_content = self.get_table_content(token)
                        #generated_questions = self.generate_Questions(token)
                        summary, table_content = await asyncio.gather(
                        summary, table_content)
                        summaries.append(summary)
                        table_contents.append(table_content)
                        #generated_questions_list.append(generated_questions)
                        print("Summurizing : 3 functions are done" + "\n")
                        print("Summurizing : generating Information..." + "\n")
                        print("Summurizing : generating Information is Done" + "\n")
                    except Exception as e:
                        print("Summurizing : Error in summurizing" + "\n")
                        print(e)
                        continue
                id = self.id.generate_unique_id()

                #These results should be optimized with gpt4 to deliver the final result.
                f_summary = "\n".join(summaries)
                f_table_content = "\n".join(table_contents)
                #f_generated_questions = "\n".join(generated_questions_list)

                print("Summary Num : " + str(len(f_summary.split())) + "\n")
                print("Table Content Num : " + str(len(f_table_content.split())) + "\n")
                #print("Questions Num : " + str(len(f_generated_questions.split())) + "\n")
                              
        #
        #        if len(f_table_content.split()) > 1700:
        #            f_table_content = await self.summurize_res(f_table_content)
        #            print("table content is shorted :::::" + "\n")
        #        if len(f_summary.split()) > 1700:
        #           f_summary = await self.summurize_res(f_summary)
        #           print("summary content is shorted :::::" + "\n")
        #        if len(f_generated_questions.split()) > 1700:
        #            f_summary = await self.summurize_res(f_summary)
        #            print("Questions content is shorted :::::" + "\n")
                
                
                f_categories = self.generate_categories(f_table_content)  
                f_title= self.generate_title(f_summary)
                print("Summurizing : HTML Processing..." + "\n")

##############################################################################################
                f_summary = self.HTML_Converter(f_summary)
                f_table_content = self.HTML_Converter(f_table_content)
                #f_generated_questions = self.HTML_Converter(f_generated_questions)
                f_categories = self.HTML_Converter(f_categories)
                f_title = self.HTML_Converter(f_title)
                f_summary, f_table_content, f_categories, f_title = await asyncio.gather(f_summary, f_table_content, f_categories, f_title)

                print("Summurizing : storing Summurized article..." + "\n")
                self.store_summarized_article({"summary_id":id,"title":f_title,"summary":f_summary,"table_content":f_table_content,"categories":f_categories, "article_url":url},db)
                updated_data = {"summurized":1}
                db.update_article(url,updated_data)
                print("Summurizing : storing Summurized article is Done ##############################################" + "\n")
                #free all lists
                summaries.clear()
                table_contents.clear()
                #db.update_summurized_article(urls[i])
            return "Done Summurizing"
        

    def get_all_summurized_articles(self,db):
        data = db.get_all_summurized_articles(db)
        return data
    


