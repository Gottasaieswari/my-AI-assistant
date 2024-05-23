
import json
import requests
import openai

from thonai import speak

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTE0YzYyODktZGNhYy00ZDRmLWE4OWUtNTE4NGQyYzQyZjMyIiwidHlwZSI6ImFwaV90b2tlbiJ9.gyWxFbb1eDX-Sg6ug5gC7wlCGvb0bRzIK3fSnnOYqYs"}
url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello i need your help ! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "abcd"
}




def take(query):
    payload["text"]=query
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    speak(result['openai']['generated_text'])