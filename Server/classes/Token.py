from DB import DB
from Prompts import Prompts
from ModelAPI import ModelAPI


class Token :
    def __init__(self) :
        pass

    db = DB()
    prompt = Prompts()

    ########### Adapt the model version to the one you want to use ############
    ModelAPI = ModelAPI("gpt-4o-mini")


    def get_all_untokenized_articles_ids(self):
            articles_ids = self.db.get_all_untokenized_articles()
            return articles_ids

# Get all tokens for each article which is not tokenized (Tokens are not stored in tokens collection)
    def get_tokens_for_each_article(self, article_id):
        
        doc_data = self.db.get_article_by_id(article_id)
        return doc_data
    
#Extract tokens from the article data
    def process_tokens(self,data):
        tokens=[]
        # Loop through all key-value pairs in the dictionary
        for key, value in data.items():
            if key.startswith('tokening'):
                continue
            else : 
                # Check if the key starts with 'token'
                if key.startswith('token'):
                    # Process the token (For example, print it)
                    tokens.append(value)
        return tokens
    
    # @Return categories of the token
    # @Return keywords of the token
    def analyse_token(self,type,token):
        if type =='categorize':
            prompt = self.prompt.CATEGORIZE_TOKENS
            response = self.ModelAPI.api_req(prompt,token)
            message = self.ModelAPI.get_message(response)
        elif type =='keywords':
            prompt = self.prompt.EXTRACT_KEYWORDS_FROM_TOKENS
            response = self.ModelAPI.api_req(prompt,token)
            message = self.ModelAPI.get_message(response)
        return message
    


    

# Store the token in the database
# @Return True if the token is stored successfully
    def store_token(self, data):
        db_op = self.db.set_token(data)
        return db_op
            

    def token_algorithm(self):
        id="id" ############### create unique id for each token
        not_tokenized_articles_ids = self.get_all_untokenized_articles_ids()
        for article_id in not_tokenized_articles_ids:
            #get the data for each token
            data = self.get_tokens_for_each_article(article_id)
            #extract the tokens from the data
            tokens = self.process_tokens(data)
            for token in tokens:
                #Analyse the token
                token_categories = self.analyse_token('categorize',token)
                token_keywords = self.analyse_token('keywords',token)
                token_data = {
                        'token_id': id,
                        'token': token,
                        'categories': token_categories,
                        'keywords': token_keywords
                    }
                self.store_token(token_data)
                
                    
        





