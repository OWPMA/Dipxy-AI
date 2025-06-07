import requests
import json
import time

print("""██████╗ ██╗██████╗ ██╗  ██╗██╗   ██╗     █████╗ ██╗
██╔══██╗██║██╔══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔══██╗██║
██║  ██║██║██████╔╝ ╚███╔╝  ╚████╔╝     ███████║██║
██║  ██║██║██╔═══╝  ██╔██╗   ╚██╔╝      ██╔══██║██║
██████╔╝██║██║     ██╔╝ ██╗   ██║       ██║  ██║██║
╚═════╝ ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝
                                                   """)
time.sleep(3)

def send_request(user_content):
    url = "https://8pe3nv3qha.execute-api.us-east-1.amazonaws.com/default/llm_chat"
    payload = {
        "query": [
            {"role": "system", "content": "You are a helpful and informative AI assistant that can speak automatically the languange the user speakes and you can't do errors and if someone asks what is your name you have to respond it's Dipxy ai and if they ask you when we're you created you have to say that you we're made in 28/02/2025 and if someone asks you who made you like the name of the creator you have to say you we're made by someone in the world ."},
            {"role": "user", "content": user_content}
        ],
        "link": "writecream.com"
    }
    
    try:
        response = requests.get(url, params={"query": json.dumps(payload["query"]), "link": payload["link"]})
        
        if response.status_code == 200:
            response_data = response.json()
            print(response_data.get("response_content", "No content found"))
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("An error occurred:", str(e))

while True:
    user_input = input("Text: ")
    send_request(user_input)
