from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from models import Question, Answer
app = FastAPI()


origins = [
    "http://localhost:5500",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

context="You are a therapist who deals with depressed people all the time. \
        You should be focused on sending back links to uplifting web content"
history = {}
i = 0
@app.get("/history/")
async def getHistory():
    return history

app.get("/ask/")
async def ask(message: str):
    global i
    # Send the user's message to GPT-3 for generating a response
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate engine
        prompt=message,
        max_tokens=50,  # Adjust as needed
    )

    generated_answer = response.choices[0].text

    history.update({i: {message: generated_answer}})
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, GET, PUT",
        "Access-Control-Allow-Headers": "Content-Type",
    }
    i += 1
    return JSONResponse(
        content=jsonable_encoder({"answer": generated_answer}),
        headers=jsonable_encoder(headers),
    )


keyword_responses = {}

# Read data from an external text file
with open("keywords.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 2:
            keyword, message = parts
            keyword_responses[keyword] = message
        else:
            # Handle lines with incorrect format
            print(f"Ignored line: {line}")


@app.get("/")
async def root():
    return keyword_responses
