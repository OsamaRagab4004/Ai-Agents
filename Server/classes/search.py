
import html
from DB import DB
from google.cloud import firestore


class search :
   
    def search_summarized_article_by_category(self,db,category):
            # Initialize Firestore client
           
            # Reference to your articles collection
            articles_ref = db.collection('summurized_articles').get()

            # Filter articles by category
            target_category = category
            filtered_articles = []

            for article in articles_ref:
                article_data = article.to_dict()

                # Check if 'categories' field exists
                if 'categories' in article_data:
                    categories_html = article_data['categories']

                    # Parse the HTML to extract text
                    categories_text = html.unescape(categories_html).replace('<h2>', '').replace('</h2>', '')

                    # Split into individual categories
                    categories = categories_text.split(' - ')

                    # Check if target category is in the list
                    if target_category in categories:
                        filtered_articles.append(article_data)

            return filtered_articles

s = search()
db = DB()
# search.search_summarized_article_by_category(db,"Customer Support and Service")
arr = s.search_summarized_article_by_category(db,"Customer Support and Service")
print(arr)
