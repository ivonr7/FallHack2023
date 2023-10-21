from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models import Question, Answer
app = FastAPI()

context="You are a therapist who deals with depressed people all the time. \
        You should be focused on sending back links to uplifting web content"
history = {}
i = 0
@app.get("/history/")
async def getHistory():
    return history

@app.get("/ask/") 
async def ask(message:str ):
    global i
    resp=Answer(answer=message) # generate questions + answers
    history.update({i:{message:resp.answer}})
    headers={"Access-Control-Allow-Origin:": "*","Access-Control-Allow-Methods": "POST, GET, PUT"
             ,"Access-Control-Allow-Headers": "Content-Type"}
    i+=1
    return JSONResponse(content=jsonable_encoder(resp),headers=jsonable_encoder(headers))


@app.get("/")
async def root():
    return {"Welcome":"To Fall Hacks Backend"}