from openai import OpenAI
from dotenv import load_dotenv
from json import loads
from os import getenv
from time import time

load_dotenv() # Carregas variaveis de ambiente

api_key = getenv("ChatGPT_API_Key") # Pega a chave da API do ChatGPT

assistant_id = "asst_iN92X2yDZccGoKvWbGpQyGG3" # ID do assistente