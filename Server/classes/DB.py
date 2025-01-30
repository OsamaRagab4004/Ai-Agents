import html
import json
import firebase_admin
from firebase_admin import credentials
import firebase_admin
from firebase_admin import credentials, firestore
from ID import ID
import os
class DB :

    def __init__(self): 
        # Use a service account
# Use a service account
        base_dir = os.path.dirname(os.path.abspath(__file__))
        cred_path = os.path.join(base_dir, "profy-2d565-firebase-adminsdk-r6sz7-7c1d7a076a.json")
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        # Get a reference to the database
        self.db = firestore.client() 
        self.id = ID()



#######################################################################################################
    def get_file_data(self, filename):
        try :
            with open(filename, 'r') as file:
                data = json.load(file)
        except Exception as e:
            print(e)
            return False        
        return data

    def set_document(self, collection, document_id, data):
        try:
            doc_ref = self.db.collection(collection).document(document_id)
            doc_ref.set(data)
        except Exception as e:
            print(e)
            return False
        
    def get_document(self, collection, document_id):

        try:
            doc_ref = self.db.collection(collection).document(document_id)
            doc = doc_ref.get()
            return doc.to_dict()
        except Exception as e:
            print(e)
            return False
        

    
    def get_article_by_id(self, article_id):
        try:
            # Query all collections named 'articles' for a document with the given ID
            articles =    self.db.collection('articles').where('id', '==', article_id).get()

            # Check if any document was found
            if articles:
                # Assuming there's only one document with this ID, return its contents
                return articles[0].to_dict()
            else:
                # No document found with the given ID
                return None
        except Exception as e:
            print(e)
            return False
    
    def get_summarized_article_by_id(self, article_id):
        try:
            # Query all collections named 'articles' for a document with the given ID
            articles =    self.db.collection('summurized_articles').where('summary_id', '==', article_id).get()

            # Check if any document was found
            if articles:
                # Assuming there's only one document with this ID, return its contents
                return articles[0].to_dict()
            else:
                # No document found with the given ID
                return None
        except Exception as e:
            print(e)
            return False
        
    def get_summarized_articles_by_categories(self, categories):
        try:
            # Query all collections named 'articles' for a document with the given ID
            articles =    self.db.collection('summurized_articles').where('categories', 'array-contains', categories).get()

            # Check if any document was found
            if articles:
                # Assuming there's only one document with this ID, return its contents
                return articles[0].to_dict()
            else:
                # No document found with the given ID
                return None
        except Exception as e:
            print(e)
            return False
    
        
    def update_document(self, collection, document_id, data):
        try:
            self.db.collection(collection).document(document_id).update(data)
            return True
        except Exception as e:
            print(f"Error updating document: {e}")
            return False


    def delete_document(self, collection, document_id):
        try:
            self.db.collection(collection).document(document_id).delete()
            return True
        except Exception as e:
            print(f"Error deleting document: {e}")
            return False
        


  ####################################################################################################### 

    def check_blog_page_url_exists(self, url):
        try:
            
            query_results = self.db.collection("blog_pages").where('url', '==', url).get()
            # Process the query results
            for doc in query_results:
                status = doc.to_dict().get('status')
                if status == 1:
                    return True
            print("No matching documents.")
            return False

        except Exception as e:
            print(f"Error checking if URL exists: {e}")
            return False   
          
    def set_blog_page_url(self, blog_page_data):
        try:
            # Reference to the URL document
            url_doc_ref = self.db.collection('blog_pages').document()

            # Add a new article to the 'articles' subcollection
            url_doc_ref.set(blog_page_data)
            print("Blog_Page added successfully")
            return True
        except Exception as e:
            print(f"Error adding Blog_Page: {e}")
            return False

   


    def update_blog_page_url(self, blog_page_url, blog_page_data):
        try:
            # Reference to the 'blog_pages' subcollection
            blog_pages_subcol =    self.db.collection('blog_pages')

            # Query to find the document with the matching URL
            query_results =    blog_pages_subcol.where('url', '==', blog_page_url).get()

            # Find the first document with the matching URL and update it
            for doc in query_results:
                if doc.exists:
                    # Get the document ID
                    blog_page_doc_id = doc.id

                    # Reference to the specific blog page document
                    blog_page_doc_ref = blog_pages_subcol.document(blog_page_doc_id)

                    # Update the document with new data
                    blog_page_doc_ref.update(blog_page_data)
                    print("Blog page URL updated successfully")
                    return  # Exit the function after updating

            # If no matching document is found
            print("No blog page found with the specified URL.")

        except Exception as e:
            print(f"Error updating blog page URL: {e}")


        

              
    def set_article(self, article_data):
        try:
            # Reference to the URL document
            url_doc_ref = self.db.collection('articles').document()

            # Add a new article to the 'articles' subcollection
            url_doc_ref.set(article_data)
            print("Article added successfully")
        except Exception as e:
            print(f"Error adding article: {e}")


   

    def update_article(self, article_url, blog_page_data):
        try:
            # Reference to the 'blog_pages' subcollection
            blog_pages_subcol = self.db.collection('articles')

            # Query to find the document with the matching URL
            query_results = blog_pages_subcol.where('article_url', '==', article_url).get()

            # Find the first document with the matching URL and update it
            for doc in query_results:
                if doc.exists:
                    # Get the document ID
                    blog_page_doc_id = doc.id

                    # Reference to the specific blog page document
                    blog_page_doc_ref = blog_pages_subcol.document(blog_page_doc_id)

                    # Update the document with new data
                    blog_page_doc_ref.update(blog_page_data)
                    print("Article URL updated successfully")
                    return  # Exit the function after updating

            # If no matching document is found
            print("No Articles found with the specified URL.")

        except Exception as e:
            print(f"Error updating blog page URL: {e}")




    def blog_url_data(self,blog_page_url=None, status=None):
        # Create a dictionary with the provided data
        if blog_page_url == None:
            data ={
                "status": status
            }
        elif status == None:
            data ={
                "url": blog_page_url
            }
        else:        
            data = {
                "url": blog_page_url,
                "status": status
            }

        return data
    

    def delete_sub_document(self, website_id,sub_collection, document_id):
        try:
            # Reference to the specific blog page document in the 'blog_pages' subcollection
            blog_page_doc_ref = self.db.collection('websites').document(website_id).collection(sub_collection).document(document_id).delete()

           
            print("Document deleted successfully")
        except Exception as e:
            print(f"Error deleting document: {e}")   


    def get_all_unscraped_blog_urls(self):
        try:
            # Reference to the specific blog page document in the 'blog_pages' subcollection
            blog_page_doc_ref = self.db.collection('blog_pages').where('status','==',0).get()
            unscraped_urls = []
            for doc in blog_page_doc_ref:
                doc_data = doc.to_dict()
                unscraped_urls.append(doc_data.get('url'))  # Assuming 'url' is a field in each document
            return unscraped_urls
        except Exception as e:
            print(f"Error getting all unscraped blog urls: {e}")       
            return False 
   
    

    def get_all_unscraped_articles(self):
            try:
                # Query to find all blog pages with status 0 in any 'blog_pages' subcollection
                query_results = self.db.collection('articles').where('status','==',0).get()

                # Process the query results
                
                article_urls = []
                for doc in query_results:
                    doc_data = doc.to_dict() 
                    article_urls.append(doc_data.get('article_url')) 
                return  article_urls
            except Exception as e:
                print(f"Error getting unscraped article: {e}")
                return False


    def get_all_untokenized_articles(self): 
        try:
            # Query to find all documents with 'tokenized' field set to '0' in any 'articles' subcollection
            query_results = self.db.collection('articles').where('tokening', '==', 0).get()

            # Process the query results
            untokenized_article_ids = []
            for doc in query_results:
                # Append the document ID to the list
                untokenized_article_ids.append(doc.id)

            return untokenized_article_ids

        except Exception as e:
            print(f"Error getting IDs of untokenized articles: {e}")
            return []


   


        except Exception as e:
            print(f"Error getting all unscraped blog urls: {e}")
            return []        
        

    def set_token(self,data) :
        try:
            # Reference to the URL document
            url_doc_ref = self.db.collection('tokens').document()

            # Add a new article to the 'articles' subcollection
            url_doc_ref.set(data)
            return True
        except Exception as e:
            print(f"Error adding article: {e}") 
            return False
        
    def set_generated_article(self, title, article_content):
        id = self.id.generate_unique_id()
        try:
            # Reference to the URL document
            url_doc_ref = self.db.collection('generated_articles').document()
            data = {
                "article_id": id,
                "article_title": title,
                "article_content": article_content
            }
            # Add a new article to the 'articles' subcollection
            url_doc_ref.set(data)
            return True
        except Exception as e:
            print(f"Error adding article: {e}")
            return False
        
    def get_generated_article(self) : 
        try:
            # Query to find all documents with 'tokenized' field set to '0' in any 'articles' subcollection
            query_results = self.db.collection('generated_articles').get()

            # Process the query results
            generated_articles = []
            for doc in query_results:
                # Append the document ID to the list
                generated_articles.append(doc.to_dict())

            return generated_articles

        except Exception as e:
            print(f"Error getting IDs of untokenized articles: {e}")
            return []
    
    def get_all_unsummurized_articles(self):
            try:
                # Query to find all blog pages with status 0 in any 'blog_pages' subcollection
                query_results = self.db.collection('articles').where('summurized', '==', 0).get()

                # Process the query results
                #scraped_data = []
                article_urls = []
                for doc in query_results:
                    doc_data = doc.to_dict()
                    #scraped_data.append(doc_data.get('scraped_data'))  
                    article_urls.append(doc_data.get('article_url')) 
                return article_urls
            except Exception as e:
                print(f"Error adding article: {e}")
                return False


    def get_article_by_url(self,url) :
        try:
            # Query to find all documents with 'tokenized' field set to '0' in any 'articles' subcollection
            query_results = self.db.collection('articles').where('article_url', '==', url).get()

            # Process the query results
            for doc in query_results:
                # Append the document ID to the list
                return doc.to_dict()

            return []

        except Exception as e:
            print(f"Error getting IDs of untokenized articles: {e}")
            return []

    def store_summurized_article(self,data): 
        try : 
            url_doc_ref = self.db.collection('summurized_articles').document()
            url_doc_ref.set(data)
            return True
        except Exception as e:
            print(f"Error adding summurized article: {e}")
            return False
    
    def get_all_summurized_articles(self,db) :
        try:
            # Query to find all documents with 'tokenized' field set to '0' in any 'articles' subcollection
            query_results =  self.db.collection('summurized_articles').get()

            # Process the query results
            summurized_articles = []
            for doc in query_results:
                # Append the document ID to the list
                summurized_articles.append(doc.to_dict())

            return summurized_articles

        except Exception as e:
            print(f"Error getting IDs of untokenized articles: {e}")
            return []
    

    def check_article_url_exists(self, url):
        try:
            # Query the database
            query_results = self.db.collection("articles").where('article_url', '==', url).get()

            # Check if any documents were returned
            if query_results and len(query_results) > 0:
                print(f"Found article with URL: {url}")
                return True
            else:
                print("No matching documents.")
                return False

        except Exception as e:
            print(f"Error checking if URL exists: {e}")
            return False


    def delete_all_data_realtime_database(self):
            
            # Fetch all collection references
            collections = self.db.collections()
            
            for collection in collections:
                # Fetch all documents in the collection
                docs = collection.stream()
                for doc in docs:
                    # Delete each document
                    doc.reference.delete()
                print(f"Deleted all documents in collection {collection.id}")



    def search_summarized_article_by_category(self,categories):
            # Initialize Firestore client
           articles_ref = self.db.collection('summurized_articles').get()
            # Filter articles by category
           filtered_articles = []
           for category in categories:
                # Reference to your articles collection
                for article in articles_ref:
                    article_data = article.to_dict()

                    # Check if 'categories' field exists
                    if 'categories' in article_data:
                        categories_html = article_data['categories']

                    if category in categories_html:
                        filtered_articles.append(article_data['summary_id'])
           return filtered_articles
    

    def delete_summarized_article_by_id(self,article_id):
        try:
            # Query all collections named 'articles' for a document with the given ID
            articles =    self.db.collection('summurized_articles').where('summary_id', '==', article_id).get()

            # Check if any document was found
            if articles:
                # Assuming there's only one document with this ID, return its contents
                for doc in articles:
                    doc.reference.delete()
                return True
            else:
                # No document found with the given ID
                return False
        except Exception as e:
            print(e)
            return False