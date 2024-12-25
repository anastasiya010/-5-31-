import telebot
from telebot import types

API_TOKEN = '7716906729:AAHzMuP4y3vFlE1mfCn9LX_zG5UUUedovZc'
bot = telebot.TeleBot(API_TOKEN)

# Состояния
START, QUIZ, RESULT = range(3)

# Вопросы и ответы
questions = [
    ("Какое самое крупное наземное животное?", "Слон", ["Слон", "Лев", "Тигр"]),
    ("Какое животное известно как король джунглей?", "Лев", ["Лев", "Слон", "Гепард"]),
    ("Какое самое быстрое наземное животное?", "Гепард", ["Гепард", "Лев", "Жираф"]),
    ("Какое животное известно своей способностью менять цвет?", "Хамелеон", ["Хамелеон", "Тигр", "Сова"]),
    ("Какое самое крупное млекопитающее в океане?", "Кит", ["Кит", "Дельфин", "Акула"]),
    ("Какое животное известно своей мудростью?", "Сова", ["Сова", "Летучая мышь", "Кошка"]),
    ("Какое единственное млекопитающее способно по-настоящему летать?", "Летучая мышь", ["Летучая мышь", "Птица", "Сова"]),
    ("Какое животное известно своей длинной шеей?", "Жираф", ["Жираф", "Слон", "Лев"]),
    ("Какой самый крупный вид медведей?", "Полярный медведь", ["Полярный медведь", "Медведь гризли", "Медведь черный"]),
    ("Какое животное известно своими полосами?", "Тигр", ["Тигр", "Лев", "Гепард"]),
]

user_data = {}

@bot.message_handler(commands=['start'])
def start_quiz(message):
    user_data[message.chat.id] = {'state': START, 'score': 0, 'question_index': 0}
    bot.send_message(message.chat.id, "Добро пожаловать на викторину о животных! Type /quiz to start.")

@bot.message_handler(commands=['quiz'])
def quiz(message):
    user_data[message.chat.id]['state'] = QUIZ
    ask_question(message)

def ask_question(message):
    user_id = message.chat.id
    index = user_data[user_id]['question_index']
    if index < len(questions):
        question, _, options = questions[index]
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for option in options:
            markup.add(option)
        bot.send_message(user_id, question, reply_markup=markup)
    else:
        show_result(message)

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('state') == QUIZ)
def handle_answer(message):
    user_id = message.chat.id
    index = user_data[user_id]['question_index']
    if index < len(questions):
        _, correct_answer, _ = questions[index]  # Получаем правильный ответ
        if message.text.lower() == correct_answer.lower():
            user_data[user_id]['score'] += 1
        user_data[user_id]['question_index'] += 1
        ask_question(message)  # Переход к следующему вопросу

def show_result(message):
    user_id = message.chat.id
    score = user_data[user_id]['score']
    bot.send_message(user_id, f"Твой результат {score} из  {len(questions)}! Type /start to play again.")
    user_data[user_id]['state'] = RESULT

bot.polling()
