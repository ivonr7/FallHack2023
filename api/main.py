from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import Question, Answer
app = FastAPI()

history = {}
i=0
@app.get("/history/")
async def getHistory():
    return history

@app.get("/ask/") 
async def ask(message:str ):
    global i
    resp=Answer(answer=message) # generate questions + answers
    history.update({i:{message:resp.answer}})
    headers= {"Access-Control-Allow-Origin": "*", "Content-Language": "en-US" }
    i+=1
    return JSONResponse(content=resp, headers=headers)


@app.get("/")
async def root():
    return {"hello":"hello"}