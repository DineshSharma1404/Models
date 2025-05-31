from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
res = model.invoke('What is the capital of India?')
print(res.content)
