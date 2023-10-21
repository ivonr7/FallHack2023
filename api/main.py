from fastapi import FastAPI
from models import Question, Answer
app = FastAPI()

history = {}
i=0
@app.get("/history/")
async def getHistory():
    return history

@app.get("/ask/") 
async def ask(message:str ):
    resp=Answer(answer=message) # generate questions + answers
    history.update({i:{message:resp.answer}})
    i+=1
    return resp


@app.get("/")
async def root():
    return {"hello":"hello"}