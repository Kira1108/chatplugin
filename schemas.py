from pydantic import BaseModel

class StatusResponse(BaseModel):
    response:str = "OK"
    

class UserTodo(BaseModel):
    todos:list = []

