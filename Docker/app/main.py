from typing import Annotated
from fastapi import FastAPI,Form
from transformers import pipeline

app = FastAPI()

question_answering = pipeline("question-answering",model = "bert-large-uncased-whole-word-masking-finetuned-squad")

@app.post("/answer/")
async def question_answer(Question : Annotated[str,Form()],Context : Annotated[str,Form()]):
    result = question_answering(question = question,context = context)
    return {"Answer" : result}
