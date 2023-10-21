from fastapi import FastAPI
from models import Question, Answer
app = FastAPI()


@app.get("/")
async def root() -> Answer:
    resp=Answer(answer="Hello Pydantic")
    return {"message": Answer}