from fastapi import FastAPI
from models import Question, Answer
app = FastAPI()


@app.get("/ask/")
async def ask(question:Question = Question(message="")) -> Answer:
    
    print(question.message)
    resp=Answer(answer=question.message)
    return resp