import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

def get_openai_api_key():
    """
    Функция для получения API ключа OpenAI из переменных окружения.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API ключ не найден в переменных окружения")
    return api_key
