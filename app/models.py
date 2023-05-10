from pydantic import BaseModel


class Task(BaseModel):
    task_id: str
    status: str


class Summary(BaseModel):
    summary: str


class Text(BaseModel):
    text: str
