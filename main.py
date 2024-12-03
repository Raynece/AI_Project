import os
from dotenv import load_dotenv
from utils.llm_utils import get_openai_api_key
from utils.database import get_user_data, save_user_data
from models.langchain_handler import LangChainHandler

#Загрузка ключей API
load_dotenv()
openai_api_key = get_openai_api_key()

#Инициализация LangChain
langchain_handler = LangChainHandler(openai_api_key)


#Основной цикл чат-бота
def chatbot():
    print("Добро пожаловать в чат-бот на базе GPT-3! (для выхода напишите 'exit')")

    while True:
        #Ввод от пользователя
        user_input = input("Вы: ")

        if user_input.lower() == 'exit':
            print("До свидания!")
            break

        #Проверка наличия данных пользователя в базе
        user_data = get_user_data(user_input)

        if user_data:
            print(f"Бот: Привет, {user_data['name']}! Как я могу помочь?")
        else:
            print("Бот: Привет, незнакомец! Могу ли я сохранить ваше имя?")
            user_name = input("Введите ваше имя: ")
            save_user_data(user_input, user_name)

        #Обработка запроса через LangChain
        response = langchain_handler.run_chain(user_input)
        print(f"Бот: {response}")


if __name__ == "__main__":
    chatbot()
