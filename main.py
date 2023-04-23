from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import json
from schemas import (
    StatusResponse,
    UserTodo)
from chatplugin import ChatPluginJson

description = """
This is a todo plugin app
""".strip()

_TODOS = {}

app = FastAPI(
    title = 'TODO app', 
    description = description, 
    version = 'v1',
    servers=[{"url": "http://127.0.0.1:12003"}])

origins = [
    "https://chat.openai.com",
    "http://localhost",
    "http://localhost:12003",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/todos/{username}", summary = "Add a todo for a user")
def add_todo(username:str, todo:str):
    if username not in _TODOS:
        _TODOS[username] = []
    _TODOS[username].append(todo)
    return StatusResponse()


@app.get("/todos/{username}", summary = "Get all todos for a user")
def get_todos(username:str):
    todos = _TODOS.get(username, [])
    return UserTodo(todos=todos)


@app.delete("/todos/{username}", summary = "Delete todo for a user")
def delete_todos(username:str, todo_idx:int):
    if 0 <= todo_idx < len(_TODOS[username]):
        _TODOS[username].pop(todo_idx)
    return StatusResponse()


@app.get("/logo", summary = "Get logo",response_class=FileResponse)
def get_logo():
    return FileResponse("./logo.png",media_type="image/png")

@app.get("/.well-known/ai-plugin.json")
def get_plugin_json():
    response_text = json.loads(open(".wellknown/ai-plugin.json",'r').read())
    return ChatPluginJson(**response_text)

@app.get("/openapi.yaml")
def openapi_spec():
    with open("./openapi.yaml", "r") as f:
        return PlainTextResponse(f.read(), media_type="text/yaml")