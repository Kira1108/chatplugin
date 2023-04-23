from pydantic import BaseModel

class ChatAuth(BaseModel):
    type:str = "none"

class ChatAPI(BaseModel):
    url:str
    is_user_authenticated:bool = False
    type:str = 'openai'

class ChatPluginJson(BaseModel):
    schema_version:str
    name_for_human:str
    name_for_model:str
    description_for_human:str
    description_for_model:str
    auth: ChatAuth
    api:ChatAPI
    logo_url:str
    contact_email:str
    legal_info_url:str


if __name__ == "__main__":
    plugin_json = {
    "schema_version": "v1",
    "name_for_human": "TODO Plugin",
    "name_for_model": "todo",
    "description_for_human": "Plugin for managing a TODO list. You can add, remove and view your TODOs.",
    "description_for_model": "Plugin for managing a TODO list. You can add, remove and view your TODOs.",
    "auth": {
        "type": "none"
    },
    "api": {
        "type": "openapi",
        "url": "http://localhost:3333/openapi.yaml",
        "is_user_authenticated": False
    },
    "logo_url": "http://localhost:3333/logo.png",
    "contact_email": "support@example.com",
    "legal_info_url": "http://www.example.com/legal"
    }

    json_str = ChatPluginJson(**plugin_json).json()
    print(json_str)