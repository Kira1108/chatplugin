from chatplugin import (
    ChatAPI, 
    ChatAuth, 
    ChatPluginJson)


auth = ChatAuth(type="none")


api = ChatAPI(url = 'http://localhost:3333/openapi.yaml',
               is_user_authenticated = False, 
               type = 'openai')

plugin_json = ChatPluginJson(
    schema_version = 'v1',
    name_for_human = 'TODO Plugin',
    name_for_model = 'todo',
    description_for_human = 'Plugin for managing a TODO list. You can add, remove and view your TODOs.',
    description_for_model = 'Plugin for managing a TODO list. You can add, remove and view your TODOs.',
    auth = auth,
    api = api,
    logo_url = 'http://localhost:3333/logo.png',
    contact_email="327485253@163.com",
    legal_info_url="http://www.example.com/legal"
)


if __name__ == "__main__":
    print(plugin_json)


