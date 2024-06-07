from pydantic import BaseModel

class ToDo(BaseModel):
    id:int
    item:str
    