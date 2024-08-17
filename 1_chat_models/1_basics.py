from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain.chains import LLMChain

load_dotenv()
model = ChatOpenAI( model="gpt-4o-mini" )

result = model.invoke("Hello, World!")

print("Model Answer Full Response: ", result)

print("Only Content: ", result.content)
