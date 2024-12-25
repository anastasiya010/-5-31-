import json
import sys
import os
from field import field
from print_result import print_result
from cm_timer import cm_timer_1
from gen_random import gen_random
from unique import Unique
from random import randint


path = 'C:/Users/Admin/PycharmProjects/pythonProject5/venv/Scripts/data.json'

try:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Файл не найден. Убедитесь, что путь указан верно.")
    sys.exit(1)
except json.JSONDecodeError:
    print("Ошибка при декодировании JSON. Проверьте формат файла.")
    sys.exit(1)

@print_result
def f1(arg):
    return sorted(Unique([job['profession'] for job in arg]), key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист"), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    salaries = [randint(100000, 200000) for _ in range(len(arg))]
    return [f"{profession}, зарплата {salary} руб." for profession, salary in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
