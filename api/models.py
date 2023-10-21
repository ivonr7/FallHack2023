from pydantic import BaseModel


class Question(BaseModel):
    message: str

class Answer(BaseModel):
    answer: str