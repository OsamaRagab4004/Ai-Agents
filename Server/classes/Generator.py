import asyncio
from Prompts import Prompts
from ModelAPI import ModelAPI
from DB import DB
class Generator :
    def __init__(self):
        pass

    prompt = Prompts()
    gpt3_5 = ModelAPI("gpt-4o-mini")
    GPT4 = ModelAPI("gpt-4o-mini")
    #db = DB()
    #################################### Generate the content of the data ####################################

    async def generateArticle(self,article_type, general_topic,tone,writing_style,Questions, Information) :
        optimized_Questions_req = self.gpt3_5.api_req(self.prompt.OPTIMIZE_INFORMATION,Questions)
        optimized_Questions = self.gpt3_5.get_message(optimized_Questions_req)
        prompt =  self.prompt.generateText(article_type, general_topic,tone,writing_style,optimized_Questions, Information)
        persona = self.prompt.CONTENT_CREATOR
        res1 = self.GPT4.api_req(persona,prompt)
        response1 = self.GPT4.get_message(res1)
        return response1
        
    
    async def Tokenize_generated_article(self,text):
        prompt = self.prompt.TOKENIZE_TEXT
        res1 = self.gpt3_5.api_req(prompt,text)
        response1 = self.gpt3_5.get_message(res1)
        return response1

    async def text_to_json_sections(self,text):
        # Splitting the text into parts based on the subheader pattern
        parts = text.split('(subheader) ')
        json_data = []

        for part in parts[1:]:  # Skipping the first split as it will be empty
            # Further splitting each part into title and text
            title_text = part.split('(text) ')
            if len(title_text) == 2:
                title, text = title_text
                text = text.replace('\n', ' ')
                json_data.append({"title": title.strip(), "text": text.strip(),"cta":"","tone":"","writing_style":"","content_structure":"","userInput":""})

        # Wrapping the list in a parent dictionary
        return {"sections": json_data}
    
    async def api_response(self,article_type, general_topic,tone,writing_style,Questions, Information):
        article =await self.generateArticle(article_type, general_topic,tone,writing_style,Questions, Information)
        processed_article = await self.Tokenize_generated_article(article)
        tokens = await self.text_to_json_sections(processed_article)
        return tokens


#################################### Generate the content of the data ####################################
    # (token, writing_style, content_structure, content_tone, content_cta, userInput)

    async def operate_token(self,token, writing_style="",content_structure="",content_tone="",content_cta="",userInput=""):

        new_token = token
        cta_result="CTA"
        use_case_result=""

        if writing_style != "":
           new_token = await self.write_with_style(new_token, writing_style)
        if content_tone != "":
            new_token = await self.write_with_tone(new_token, content_tone)
        if content_structure != "":
            new_token = await self.write_with_content_structure(new_token, content_structure)
        if content_cta != "":
            cta_result = await self.write_CTA(new_token, content_cta)
        if userInput != "":
            new_token = await self.custom_user_prompt(new_token, userInput)
        return new_token,cta_result,use_case_result

       


    async def write_with_style(self,token, style):
        prompt = self.prompt.writeStyle(style)
        req = self.gpt3_5.api_req(prompt, token)
        res = self.gpt3_5.get_message(req)
        return res
    
  
    
    #- Generate FAQs for the content using AI
    async def write_with_content_structure(self,token,structure):
        prompt = self.prompt.contentStructure(structure)
        req = self.gpt3_5.api_req(prompt, token)
        res = self.gpt3_5.get_message(req)
        return res
    
    
    
     # Generate SEO Keywords for the content using AI
   
    async def write_with_tone(self,token, tone):
        prompt = self.prompt.writeTone(tone)
        req = self.gpt3_5.api_req(prompt, token)
        res = self.gpt3_5.get_message(req)
        return res
   



    async def write_use_case(self,token, usecase):
        prompt = self.prompt.WRITE_USE_CASE
        req = self.gpt3_5.api_req(prompt, token)
        res = self.gpt3_5.get_message(req)
        return res
   
   
    async def write_CTA(self,token, cta_type):
        prompt = self.prompt.write_cta(cta_type)
        req = self.gpt3_5.api_req(prompt, token)
        res = self.gpt3_5.get_message(req)
        return res
   


    async def write_USE_CASE(self,token):
        prompt = self.prompt.WRITE_USE_CASE
        req = self.gpt3_5.api_req(prompt, token)
        res = self.gpt3_5.get_message(req)
        return res
   
    async def custom_user_prompt(self,token,custom_prompt):
        #user_prompt_optimization = self.prompt.USER_PROMPT_OPTIMIZATION
        #res = self.GPT4.api_req(user_prompt_optimization, custom_prompt)
        #prompt = self.GPT4.get_message(res)
        req = self.gpt3_5.api_req(custom_prompt, token)
        final_res = self.gpt3_5.get_message(req)
        return final_res
   

    def set_generated_articles(self,article_id, article_content,db):
        result = db.set_generated_article(article_id,article_content) 
        return result
    
    async def get_generated_articles(self, db):
        result = db.get_generated_article() 
        return result

# Example usage

