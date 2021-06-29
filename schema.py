from pydantic import BaseModel, validator


class ToDoIn_pydantic(BaseModel):
    title: str
    description: str

class ToDo_pydantic(BaseModel):
    id: int
    title: str
    description: str

    @validator("title", pre=True, always=True)
    def check_title(cls, title):
        assert len(title) > 0, "title cannot be empty string!"
        return title


    class Config:
        arbitrary_types_allowed = True
        orm_mode = True