import sqlite3

DATABASE = 'chatbot_db.sqlite3'


def create_table():
    """
    Создание таблицы пользователей в базе данных.
    """
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                question TEXT NOT NULL
            )
        ''')


def get_user_data(question):
    """
    Проверка, есть ли данные о пользователе в базе.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE question=?", (question,))
        result = cursor.fetchone()
        if result:
            return {"name": result[1], "question": result[2]}
        return None


def save_user_data(question, name):
    """
    Сохранение данных о новом пользователе.
    """
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO users (name, question) VALUES (?, ?)", (name, question))


# Убедитесь, что таблица создана перед выполнением запросов
create_table()

# Пример использования
save_user_data("Как дела?", "Иван")
user_data = get_user_data("Как дела?")
print(user_data)
