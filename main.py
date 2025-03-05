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
        return response.id

def create_thread():
    """
        Cria uma nova thread no OpenAI e retorna o ID da thread.
    Returns:
        str: O ID da thread.
    """
    return client.beta.threads.create().id

def send_message(thread_id:str,image_id:str):
    """
    Envia uma mensagem para o OpenAI.
    Args:
        thread_id (str): O ID da thread.
        image_id (str): O ID da imagem.
    """
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content= [
            {
                type:"image_file",
                "image_file":{
                    "file_id":image_id
                }
            }
        ]
    )