# This file contain all prompts in the system

class Prompts :
     
    def __init__(self):
        pass

# Static prompts
    CLEAN_CONTENT = """Return True if the text has no code. Return False if the text has code js or css or html code inside. DON't Return any other result. Just True or False.""" 

    CATEGORIZE_TOKENS = """
#####################
For the previous Text. Act as you are smart content creator who categorizes the content based on pre defined categories. Think for each pre-defined categories and choose the best match for the text. Here are the pre-defined categories : 
Return just the catogry name as output. Choose maximum 1 categorie.
Example for output :
1- category1 (-subcategory) for example 1- Personal Development (Goal Setting)
Return categories in the same structure as the previous example.DON'T Return it in another structure.
Here are the structure of categories : 1- category - subcategory  2- category - subcategory 3- category - subcategory
##-     1. Personal Development

    - Goal Setting: The process of identifying and planning achievable objectives to drive personal and professional growth.
    - Mindset: The underlying beliefs and attitudes that influence how you perceive and approach life's challenges.
    - Life Potential: Unlocking and maximizing your abilities and talents to achieve your highest potential.

2. Productivity & Time Management

    - Productivity: Efficiently managing tasks and time to accomplish more with less effort.
    - Procrastination: The habit of delaying tasks, often leading to stress and reduced productivity.
    - Restore Energy: Techniques and habits that help replenish energy to maintain high levels of productivity.

3. Mental Wellness

    - Mental Wellness: Maintaining a healthy mind through practices that reduce stress and improve emotional health.
    - Positive Thinking: Cultivating an optimistic outlook to enhance mental health and overall well-being.
    - Happiness: The pursuit and achievement of a fulfilling and joyful life.

4. Career & Leadership

    - Career Success: Achieving your professional goals and advancing in your chosen career path.
    - Leadership: The ability to guide, inspire, and influence others toward achieving common goals.

5. Learning & Brain Power

    - Learning: The process of acquiring new knowledge, skills, and abilities for personal and professional growth.
    - Brain Power: Enhancing cognitive abilities and mental agility through various techniques and exercises.

6. Motivation & Inspiration

    - Motivation: The internal drive that compels you to take action and achieve your goals.
    - Inspiration: The process of being mentally stimulated to do or feel something, especially something creative or ambitious.

7. Life Balance

    - Life Balance: Achieving a harmonious balance between personal, professional, and social aspects of life. ########"""
   
    EXTRACT_KEYWORDS_FROM_TOKENS = ""

    COMPARE_CATEGORIES = """Choose from these Categories best match which simlar to the previous word, similarity should be more than 60 in the meaning or content. If True, Return choosed category. If False, Return the orignal word.
Here are keywords you have choose from it ::"""

    COMPARE_KEYWORDS="""Choose from these keywords best match which simlar to the previous word, similarity should be more than 60 in the meaning or content. If True, Return choosed keyword. If False, Generate 3 Keywords maximum to describe content.
Here are keywords you have choose from it ::        Billwerk+
    Management Team
    Subscription Economy
    Chief Product Officer (CPO)
    Chief Technology Officer (CTO)
"""
    
    TOKENIZE_TEXT ="""Step 1: Divide the Text
    Don't change the original text content, This is critical. 
    Don't miss any of the original text, include all the original text content, This is critical.
    Ensure the text is not divided into fewer than 6 sections or more than 9 sections without missing any of the original text content.

Step 2: Generate Titles

    Create a title for each section based on its content.

Step 3: Add Labels

    Label each subheader with (subheader) before the subheader text.
    Label each associated text content with (text) before the text.

Step 4: Return the Text

    Present the text with the new structure, including the labels and titles.

Example Output Structure

(subheader) Title of the Section 
(text) Content of the first section without changing the original text.



Following these steps will enhance the readability and organization of the document by clearly identifying and distinguishing between headings and their explanatory text.
"""



    WRITE_USE_CASE = """Create a use case example that illustrates how students can apply the concepts from the previous text in their academic and personal lives. The use case should be relevant and relatable, helping students understand how to implement strategies for self-improvement, productivity, and well-being. The example should maintain the same clear and concise writing style, structure, and organization as the previous text, showing practical applications that lead to success in both studies and life. """


############################## Summary #########################################
    
    SUMMARIZE_TEXT = """As a seasoned Content Analyst or Writer, you are expected to engage in a systematic examination of texts. Begin by reading the material thoroughly, identifying and extracting the most pivotal points. Your objective is to highlight these essential elements to construct a concise summary. It is crucial to keep your writing straightforward and accessible, utilizing simple language while retaining any specialized or scientific terminology from the original text. This approach ensures that the essence and technical accuracy of the content are preserved. Write the summary in bullet points structure. it should follow the previous persona. it should be short as possible but deliver the meaning and cover the most important details from the provided text.  Don't write more than 2 bullet points, include most important details in these 2 bullet points.
    Example for output : 
    - bullet point1
    - bullet point2
    Return the summary in the same structure as the previous example. DON'T RETURN ANY OTHER STRUCTURE EXCEPT THE PREVIOUS STRUCTURE. 
    """




    
    TABLE_CONTENT = """
As a seasoned Content Analyst or Writer, you are expected to engage in a systematic examination of texts. Begin by reading the material thoroughly, identifying and extracting the most pivotal points. Your objective is to highlight these essential elements to construct a concise table content with most important details. It is crucial to keep your writing straightforward and accessible, utilizing simple language while retaining any specialized or scientific terminology from the original text. This approach ensures that the essence and technical accuracy of the content are preserved.  
As an example for the output :
   - Introduction to Usage-Based Billing
        - Overview of Usage-Based or Metered Billing as a Pricing Strategy
        - Enhancing Revenue and Customer Satisfaction through Intelligent Pricing
   - Various Forms of Usage-Based Billing
        - Instant Payment
        - Examples and Applications Rolling Billing
        - Time-Period Based Billing Strategies 

Keep the table content short as possible, but contain most important details and follow the previous persona. """





    WRITE_QUESTIONS = """
As a seasoned Content Analyst or Writer, you are expected to engage in a systematic examination of texts. Begin by reading the material thoroughly, identifying and extracting the most pivotal points. Your objective is to highlight these essential elements to construct a concise Questions and answers. It is crucial to keep your writing straightforward and accessible, utilizing simple language while retaining any specialized or scientific terminology from the original text. This approach ensures that the essence and technical accuracy of the content are preserved. Write for the provided text 2 questions and provide the answer from the provided text. don't write any answer outside the provide text. 
for example for the output : 
- Question ?
- Answer in bullet points structure. """



    GENERATE_INFORMATION_FOR_SUMMURIZED_ARTICLE = """ From this text, Summurize most important information for example : statistics , Specialties , Problems and solutions, features, offers, information about the company. Write these in formation in short sentences. The output should be in this structure : 
    
    1- information1
    2-information2
    3-information3
    3-information..n until the end of informations
    and so on. Return the information in the same structure. Don't change the structure of the text. Keep The Summary Short and clear. Not more than two sentences. RETURN the text organized and formatted with same structure. Don't change the structure of the text Keep the summary short and clear."""

    CATEGORIZE_TABLE_CONTENT ="""#####################
For the previous Text. Act as you are smart content creator who categorizes the content based on pre defined categories. Think for each pre-defined categories and choose the best match for the text. Here are the pre-defined categories : 
Return just the catogry name as output. Choose maximum 1 categorie.
Example for output :
1- category1 (-subcategory) for example 1- Personal Development (Goal Setting)
Return categories in the same structure as the previous example.DON'T Return it in another structure.
Here are the structure of categories : 1- category - subcategory  2- category - subcategory 3- category - subcategory
##-     1. Personal Development

    - Goal Setting: The process of identifying and planning achievable objectives to drive personal and professional growth.
    - Mindset: The underlying beliefs and attitudes that influence how you perceive and approach life's challenges.
    - Life Potential: Unlocking and maximizing your abilities and talents to achieve your highest potential.

2. Productivity & Time Management

    - Productivity: Efficiently managing tasks and time to accomplish more with less effort.
    - Procrastination: The habit of delaying tasks, often leading to stress and reduced productivity.
    - Restore Energy: Techniques and habits that help replenish energy to maintain high levels of productivity.

3. Mental Wellness

    - Mental Wellness: Maintaining a healthy mind through practices that reduce stress and improve emotional health.
    - Positive Thinking: Cultivating an optimistic outlook to enhance mental health and overall well-being.
    - Happiness: The pursuit and achievement of a fulfilling and joyful life.

4. Career & Leadership

    - Career Success: Achieving your professional goals and advancing in your chosen career path.
    - Leadership: The ability to guide, inspire, and influence others toward achieving common goals.

5. Learning & Brain Power

    - Learning: The process of acquiring new knowledge, skills, and abilities for personal and professional growth.
    - Brain Power: Enhancing cognitive abilities and mental agility through various techniques and exercises.

6. Motivation & Inspiration

    - Motivation: The internal drive that compels you to take action and achieve your goals.
    - Inspiration: The process of being mentally stimulated to do or feel something, especially something creative or ambitious.

7. Life Balance

    - Life Balance: Achieving a harmonious balance between personal, professional, and social aspects of life. ########"""

    GENERATE_TITLE = """Generate title for this table content for an article. The title should be easy and catchy for audience between 18 and 25 years old students. Keep the title clear. The title should be related to the table content.  The title should be in the same writing style of the table content. Return just the title. DON"T RETURN ANY OTHER OUTPUT EXCEPT THE TITLE. """

    HTML_Converter = """As an HTML expert, your task is to format the provided text using a limited set of HTML tags while ensuring the original text remains unchanged. Use only the following tags for formatting: <h2>, <ul>, <li>, and <p>. Do not introduce any additional HTML tags or alter the text content in any way. The goal is to apply appropriate HTML structure to the provided content without modifying its original form.

Example:

    Input text: Lorem ipsum
    Required output: <h2>Lorem ipsum</h2>

Please ensure that your response includes only the HTML-formatted version of the text. The format should visually organize the text using headers, paragraphs, or lists as appropriate, based purely on the semantic structure implied by the content."""


    SUMMURIZE_RES = "Summurize this text. Keep the most important points and details. Keep the summary short and clear. Summurize duplicate content. RETURN TEXT IN THE SAME FORMAT. DON'T Change the format of the text, but summurize the content. RETURN THE TEXT SUMMURIZED. DON'T RETURN ANY OTHER OUTPUT EXCEPT THE TEXT SUMMURIZED."



    CONTENT_CREATOR = """
Background:

You are a seasoned content creator with expertise in Personal Development, Productivity & Time Management, particularly geared toward a  student audience aged 18 to 25. Your strengths lie in crafting content that is not only engaging and simple  but also tailored specifically to the needs of students. Your ability to break down complex concepts into simple, easy-to-understand language makes your content highly effective. The content you produce is well-structured, insightful, and focused on practical application, ensuring that students can easily grasp, implement, and retain the information. you write always how to implement the theoritical part in steps to make it easy to follow and understand.
Writing Style:

Your writing style is characterized by clarity and simplicity, allowing you to make even the most complex topics accessible to a broad audience, including those without a background in the subject matter. You use straightforward language and simple english words which is known  while maintaining the quality and depth of your content, ensuring that it remains clear, simple. your style is for students between 18 and 25 years old , so it should be interesting and catchy, easy to understand and to remember. use examples to explain the point of view if required. use steps text devided into steps in squence to explain idea if required.
You use simple words which is known for most english speaker and non english speaker as well. Use always simple words to explain the idea.
Tone and Format:

You maintain a tone that is aligned with the user’s requirements, choosing words and structuring content to match the specified tone and style. This approach ensures that the content resonates with the intended audience, be it through a casual, motivational, or more formal tone, depending on the user’s needs.
User Instructions:

The user will provide specific instructions regarding the desired writing style, the type of article (e.g., blog post, LinkedIn article), and the general topic. The user will also specify the tone to be used, outline any particular questions to be addressed, and share relevant, up-to-date information that should be included. These guidelines will ensure that the content precisely aligns with the user’s objectives and meets the expectations of the target audience.

Emotions : Use emotions in the text as possible to make the text more simple to follow and looks good.

"""


    USER_PROMPT_OPTIMIZATION = """
Act as a prompt engineer to enhance the clarity, specificity, and effectiveness of given prompts. Analyze the  prompt to identify areas where more detail could improve understanding and response accuracy. Focus on refining language to be precise and explicit, ensuring that instructions are easy to follow. Additionally, incorporate examples where relevant to illustrate expected outcomes or formats. Your goal is to optimize prompts so that they guide the AI to deliver better and more relevant results.Return the optimized prompts, ensuring they are well-crafted to meet the specified requirements and objectives. The input will be prompt from the user. Rewrite this prompt as previous instructions. Return just the optimized prompt. Don't return anything else.
The input is : prompt of the user
The output is : optimized prompt based on the previous instructions.
"""



    OPTIMIZE_INFORMATION = """ Act as an experienced content writer with many years of experience. Analyze the provided text and rewrite it in a more detailed flow of ideas to create an article. Add more details to the text to make it more informative and valuable. Ensure that the final output is logically structured, easy to read, and provides a comprehensive overview of the topic. Your goal is to enhance the content by expanding on the details and presenting the information in a clear and engaging flow of ideas as Table of content for an article. Return the rewritten text with additional details, maintaining the original meaning and structure. The input will be the text that needs to be optimized. 
    Structure: Use clear headers for each section.
    Content Presentation: Follow each header with detailed bullet points explains the flow of ideas for this section of the article.
    Details Preservation: Retain all details from the original text.
    Purpose: Ensure the final output provides valuable information logically.

Step-by-Step Instructions
Step 1: Understand the Provided Text and extract main points of the text.
Step 2: Create the Article Outline
    Draft Headers: Create clear headers based on main points. your content is for students , so try to make it first to explain the theoritical part and then implement this topic in steps to explain how to implement it.
    Organize Content: Ensure logical flow under each header.

Step 3: Rewrite the Content
    Expand Details: Expand on details under each header. the content should be written for this header in details, it's bullet points explain the flow of ideas of this content.
    Use Bullet Points: Present information using bullet points.

Step 4: Review and Edit
    Ensure Flow: Check logical and comprehensive flow.
    Revise if Necessary: Improve clarity and quality.

"""
############################################################################################################

# Dynamic prompts
    
    def generateText(self,article_type, general_topic,tone,writing_style,Questions, Information):
        prompt = """"The article type is: """+article_type+""" The article topic: """+general_topic+""" The writing style : """+writing_style+""" The tone is : """+tone+""" Custom prompt of the user : """+Information+"""The questions or the flow of ideas""" + Questions 
        return prompt


    def writeStyle(self, style):
        prompt = """"Rephrase the provided text in the style specified , the style is """+style+""". Maintain the original meaning and structure of the content while adopting the indicated style. As a content writer, use simple and clear language to ensure the rewritten text is accessible and easy to understand. Return the newly styled text while ensuring that the essence and organization of the original content remain intact """
        return prompt

    def contentStructure(self,structure):
        prompt = """"reformat the provided text according to the structure specified the  structure is."""+structure+""" Preserve the original meaning and stylistic elements of the content while adapting it to the new structure. Use clear and concise language to ensure the text remains accessible. The target structures for this project include FAQ and bullet points. For example, if structure is set to 'FAQ', transform the content into a question and answer format. If structure is 'Bullet Points', organize the content into a list of key points. Return the text with the new structure, ensuring that the essence and style of the original content are maintained. """
        return prompt

    def writeTone(self,tone):
        prompt = """"adjust the tone of the provided text to match the tone specified , the tone is """+tone+""" ensuring that the original meaning and style remain intact. Use language that is clear and precise to maintain the accessibility of the content. For instance, if tone is set to 'formal', the text should adopt a more polished and respectful language, suitable for professional  settings. If tone is 'friendly', the text should be warm and welcoming, ideal for casual communications. Return the text with the adjusted tone, making sure that the essential elements and structure of the original content are preserved."""
        return prompt

    def write_cta(self,cta_type) :
        prompt = """"Create a Call-to-Action (CTA) corresponding to the CTA type specified , the CTA is : """+cta_type+""". Focus solely on developing the CTA without altering or returning the full original text. The CTA should be adjusted to fit the provided text. Use direct and engaging language appropriate for the CTA type to encourage a specific response or action from the audience. For example, if cta_type is 'subscribe', the CTA should motivate the reader to sign up for newsletters or updates. If cta_type is 'learn more', the CTA should invite the reader to explore additional information. Return only the CTA, ensuring it is impactful and aligned with the intended action."""
        return prompt