from fastapi import FastAPI
from models import Question, Answer
app = FastAPI()


@app.get("/ask/")
async def ask(message:str ) -> Answer:
    
    print(message)
    resp=Answer(answer=message)
    return resp


@app.get("/")
async def root():
    return {"hello":"hello"}