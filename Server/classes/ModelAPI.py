from urllib import response
from openai import OpenAI
import os
import time
import openai

import requests


class ModelAPI:

  def __init__(self, modelV):
    self.modelV = modelV

  def api_req(self,prompt,req):  
    max_retries = 5  # Maximum number of retries  
    retry_interval = 2  # Seconds to wait between retries
    
    for attempt in range(max_retries):
      try:
        client = OpenAI(
        api_key=os.getenv("API_KEY"),
        )
        completion =  client.chat.completions.create(
          model=self.modelV,
          messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": req}
          ]
        )
        return completion
     
      except Exception as e:
                print(f"An unexpected error occurred: {e}. Attempt {attempt + 1} of {max_retries}.")
                if attempt < max_retries - 1:
                    time.sleep(retry_interval)
                else:
                    raise
            
  
  def get_message(self, response):
    return response.choices[0].message.content
  
  def get_tokens(self, response):
    return response.usage.total_tokens


 
#rea1 = ModelAPI("ft:gpt-3.5-turbo-0613:personal::8ZUN5zei")
#res1 = rea1.api_req("You are content creator with many years experience.","Write a description for an article about magical Dinosaur in the old ages, i want to promot this description.Keep it clear and strong. Keep it less than 200 words. Write in tone Professional and Persuasive. Write in Simple powerful words and clear in manner. Write in human style and don't write duplication content. Write in tone Formal. Write in structure Subheadings structure")
#response1 = rea1.get_message(res1)
#print(response1)

