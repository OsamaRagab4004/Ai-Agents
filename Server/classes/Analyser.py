import Prompts
from ModelAPI import ModelAPI


# This class to anaylse the data which scrapped from the web pages, generate tokens from the text, and to optimize the structure of the data
class Analyser :
    def __init__(self, data):
        self.data = data

    prompt = Prompts()


    #################################### Clean the scraped content from any non text values ####################################

# @Return: Cleaned data : This data will be stored in the database as scraped data
# This function should have fne tuning to clean the data from any non text values, it's mcuh faster and accurate.
    def cleanContent(self):
        #gpt-4-1106-preview
        model_api = ModelAPI("gpt-3.5-turbo-16k")
        prompt = self.prompt.CLEAN_CONTENT
        response = model_api.api_req( prompt , self.data)
        final_result = model_api.get_message(response)
        # clean data
        return final_result


    #################################### Analyse the content of the data ####################################
    # 1- Generating category for the content using AI
    def categorizeContent(self):
        # Analyse data
        return self.data
    
   
    
    # 3 - Generating short description for the content using AI
    def generateShortDescription(self):
        # Analyse data
        return self.data

    #4 - Generating SEO keywords for the content using AI
    def analyseKeywords(self):
        # Analyse data
        return self.data
    
    #5 - Generating Tone for the content using AI
    def generateTones(self):
        # Analyse data
        return self.data
    
    #6- Define the typ of the article
    def defineType(self):
        # Analyse data
        return self.data
    #7- Mention an example for the paragraph
    def generateExample(self):
        # Analyse data
        return self.data
    #8- Generate QA for the content
    def generateQA(self):
        # Analyse data
        return self.data
    
    ############################################################################################################


    #################################### Optimize the content of the data ####################################

    # Summarize the content of the data based on predefined parameters by the user which will affect the prompt
   
    def summarizeContent(self):
        # Analyse data
        return self.data
    

    # Generate content for the MindMap
    def generateMindMap(self):
        # Analyse data
        return self.data


Text = """What Is Checkout Abandonment and Why Is It Happening? Checkout abandonment occurs when an online shopper begins the purchase process but never actually completes it. Items are often left in virtual shopping carts and considered abandoned. If you’re a frequent online shopper at one point or another, you’ve been guilty of checkout abandonment. Maybe you were interrupted by a phone call from a family member, forgot about dinner in the oven, or just had a change of heart right before clicking “complete purchase” Whatever the reason – you didn’t end up buying what you intended. For consumers, it’s just something that happens. For ecommerce businesses, it’s a challenge that requires constant attention and strategic testing that aims to get shoppers to complete their purchases with online retailers fully. window.onevent = function(event) { if (event.type == 'message') { console.log('received message from extension!', event.data); } };
"""
analyser = Analyser(Text)
msg = analyser.cleanContent()
print(msg)