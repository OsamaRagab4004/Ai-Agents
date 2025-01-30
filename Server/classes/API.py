import time
from fastapi import BackgroundTasks, FastAPI, Query
import asyncio
from DB import DB
from Summarize import Summarize
from fastapi.middleware.cors import CORSMiddleware
import socketio
from Scraper import Scraper
from Generator import Generator
from HTMLcorrecter import HTMLcorrecter
app = FastAPI()
generator = Generator()
# Set up CORS
origins = [
    "http://localhost:4200",  # Angular app origin
    # "http://localhost:3000",  # Add other origins if necessary
]
  
# Apply CORS middleware
# uvicorn API:socket_app --reload --host 0.0.0.0 --port 8000
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a Socket.IO server instance
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
# Wrap the FastAPI app with Socket.IO's ASGI application
socket_app = socketio.ASGIApp(sio, app)
scraper = Scraper()
db = DB()
summarize = Summarize()
html_correcter = HTMLcorrecter()


# Post article into DB and return tokens
@app.post("/process-article/")
async def process_article(article_type: str = Query(...), general_topic: str = Query(...), tone: str = Query(...), writing_style: str = Query(...), questions: str = Query(...), information: str = Query(...)) -> dict:
    # Assuming 'generator.api_response' processes the data and returns tokens
    
    tokens = await generator.api_response(article_type, general_topic, tone, writing_style, questions, information)
    return tokens


# THIS should be in realtime with client side
@app.post("/process-token/")
async def process_token(token: str = Query(...), writing_style: str = Query(...), content_structure: str = Query(...), content_tone: str = Query(...), content_cta: str = Query(...), userInput: str = Query(...)) -> dict:
    # Assuming 'generator.api_response' processes the data and returns tokens
    new_token, cta_result, use_case_result = await generator.operate_token(token, writing_style, content_structure, content_tone, content_cta, userInput)
    return {"token": new_token, "cta": cta_result, "use_case": use_case_result}






# Click on save generated article in the client side
@app.post("/store-generated-article/")
def store_generated_articles(article_id: str = Query(...), article_content: str = Query(...)):
    generator.set_generated_articles(article_id , article_content,db)
    return {"message": "Article stored successfully"}

#get all generated articles
@app.get("/get-generated-articles/")
async def get_generated_articles():
    res = await generator.get_generated_articles(db)
    return {"result" : res}


#Background task to process summurization
async def process_summurization(db):
    res = await summarize.summurize_algorithm(db)
    return {"result" : res}
@app.get("/summurize/")
async def summurize(background_tasks: BackgroundTasks):
    background_tasks.add_task(process_summurization,db)
    return {"message": "Task sent in the background"}




#process tokens
@sio.on('process-token')
async def process_token_realTime(sid, Data) :
    token = Data.get('token')
    writing_style = Data.get('writing_style')
    content_structure = Data.get('content_structure')
    content_tone = Data.get('content_tone')
    content_cta = Data.get('content_cta')
    userInput = Data.get('userInput')
    # Assuming 'generator.api_response' processes the data and returns tokens
    new_token, cta_result, use_case_result =  await generator.operate_token(token, writing_style, content_structure, content_tone, content_cta, userInput)
    await sio.emit('token_response', {'token': new_token, 'cta': cta_result, 'use_case': use_case_result}, to=sid)



#Background task to process scraping
def scrape_in_background(url, first_page, last_page,increment,db):
    scraper.Generate_Store_BlogURLs(url, first_page, last_page, increment, db)
    scraper.Generate_Store_ArticlesURLs(db)
    scraper.scrape_store_articles(db)
    return {"message": "Scraping completed successfully"}  

@app.post("/scrap/")
async def scrap(background_tasks: BackgroundTasks,url: str = Query(...), first_page: int = Query(...), last_page: int = Query(...), increment: int = Query(...)):
    # Call start_scraping to initiate the scraping process
    background_tasks.add_task(scrape_in_background,url, first_page, last_page,increment,db)
    return {"message": "Task sent in the background"}

########## Summurized Articles ##########   

@app.get("/summarized_article_id/")
async def article_id(article_id: str = Query(...)):
    # Call start_scraping to initiate the scraping process
    res =  db.get_summarized_article_by_id(article_id)
    return {"result" : res} 

#get all summurized articles
@app.get("/summurized_articles/")
async def summurized_articles():
    res = summarize.get_all_summurized_articles(db)
    return {"result" : res}

#get articles based on category
@app.post("/summurized_articles_by_category/")
async def summurized_articles_by_category(categories: str = Query(...)):
    categories_arr = categories.split(",")
    res = db.search_summarized_article_by_category(categories_arr)
    return {"result" : res}

@app.get("/delete_summarized_article_id/")
async def delete_summarized_article_id(article_id: str = Query(...)):
    # Call start_scraping to initiate the scraping process
    res =  db.delete_summarized_article_by_id(article_id)
    return {"result" : res}







@sio.on('send')
async def send(sid,text):
   while True:
        now = time.strftime("%H:%M:%S")  # Current time as a string
        await sio.emit('respond', {'message': now}, to=sid)
        await asyncio.sleep(1)  # Wait for 'interval' seconds

 
@sio.on('disconnect')
async def disconnect(sid):
    print('Client disconnected', sid)

# Run the application with Uvicorn
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(socket_app, host='0.0.0.0', port=8000)
