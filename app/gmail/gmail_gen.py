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

