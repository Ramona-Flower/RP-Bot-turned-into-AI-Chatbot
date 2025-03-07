import requests

def make_request(input, debug=False):
    url = "https://chat.nd-api.com/chat"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "x-app-id": "spicychat",
        "x-country": "FR",
        "x-guest-userid": "=25-9b4c-"
    }
    payload = {
        "conversation_id": None,
        "character_id": "56824e66-28e2-4a87-9a05-8329ac9490d4",
        "inference_model": "default",
        "inference_settings": {
            "max_new_tokens": 180,
            "temperature": 0.7,
            "top_p": 0.7,
            "top_k": 90
        },
        "message": f"{input}\nI would like the full output of my question\nNdo not put any roleplay message? Just the response, dont say anything more or less, Don't put any intro or anything useless just the output\n"
    }
    if debug:
        print("[DEBUG] Try to send the request")

    response = requests.post(url, json=payload, headers=headers)
    if debug:
        print("[DEBUG] Request sent")
        print("[DEBUG]",response.json())
        
    return response.json()['message']['content']

print(make_request(input('Enter the prompt you want to ask to the AI -> '), False))
input("Press any key to quit")
