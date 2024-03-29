import datetime

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Answers(BaseModel):
    name: str | None
    sex: str | None
    birth_date: datetime.date | None
    birth_place: str | None
    living_place: str | None
    phone_number: str | None
    email: str | None
    admission_date: datetime.date | None
    med_group: str | None
    height: int | None
    mass: int | None


last_content = None


@app.post("/")
async def create_ans(answers: Answers):
    global last_content
    last_content = answers
    return answers


@app.get("/")
async def get_content():
    global last_content
    if last_content:
        return last_content
    return {"smth": "nothing"}
