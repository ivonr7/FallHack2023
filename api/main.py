from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from models import Question, Answer
app = FastAPI()


origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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

    i+=1
    return JSONResponse(content=jsonable_encoder(resp),headers={})


@app.get("/")
async def root():
    return {"Welcome":"To Fall Hacks Backend"}