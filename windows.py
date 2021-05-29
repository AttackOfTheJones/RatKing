import openai
import requests

#Retrieve user's API Key
openai.api_key = input("Enter API key:\n")

#Issue Free Request to verify Key
r = requests.get("https://api.openai.com/v1/engines/davinci/completions/browser_stream",
  headers={
    "Authorization": f"Bearer {openai.api_key}"
  },
  
  params={
    "prompt": 'Authentification',
    "max_tokens": 0,
    "logprobs": 1,
    "echo": True
})

if (r.reason == 'Unauthorized'):
    print("Invalid Key")
else:
    print("Valid Key")
