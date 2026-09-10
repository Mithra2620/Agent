import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_KEY = os.getnev("GEMINI_API_KEY","")
MODEL = os.getnev("GEMINI_MODEL ","gemini-3.5-flash")

def generate_email_with_gemini(command);
 if not API_KEY:
   raise RuntimeError ("GEMINI_API_KEY is missing")
   prompt = f"""
you are a professional gmail writing assistant.
convert the user's voice command into a professional email.

Rules:
- Do not copy the command literally 
- do not explain anything
- do not invent names, dates, prices, companies,attachments or facts .
- keep the email natural and concise.
-Include an appropriate greeting and closing.

Output exactly:
SUBJECT : <subject>
BODY :
<email body>
User command :
{command}
"""
 url={
    f"https://generativelanguage.googleapis.com/"
    f"vlbeta/models/{MODEL}:generativeContent"
  }
  payload = {
    "contents":[{"parts":[{"text":prompt}]}],
    "generationConfig":{
      "temperature":0.7,
      "maxOutputTokens":800
    }
  }
  req = urllib.request.Request{
    url,
    data=json.dumps(payload).encode(),
    headers={
      "context-Type":"application/json",
      "x-goog-api-key": API_KEY
    },
  method="POST"
  }
