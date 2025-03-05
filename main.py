from openai import OpenAI
from dotenv import load_dotenv
from json import loads
from os import getenv
from time import time

load_dotenv() # Carregas variaveis de ambiente

api_key = getenv("ChatGPT_API_Key") # Pega a chave da API do ChatGPT

assistant_id = "asst_iN92X2yDZccGoKvWbGpQyGG3" # ID do assistente

client = OpenAI(api_key=api_key) # Cria o cliente

def upload_image(image_path:str)->str:
    """
    Recebe o caminho de uma imagem e a envia para o OpenAI e retorna o ID da imagem.
    Args:
        image_path (str): O caminho da imagem.
    Returns:
        str: O ID da imagem.
    """
    with open(image_path,"rb") as image:
        response = client.files.create(file=image,purpose="vision")
        return response["id"]
    