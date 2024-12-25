import random


def gen_random(count, min, max):
    for _ in range(count):
        yield random.randint(min, max)


if __name__ == "__main__":
    print('Введите кол-во чисел:')
    count = int(input())
    print('Введите min диапозона:')

    min = int(input())
    print('Введите max диапозона:')
    max = int(input())

    for number in gen_random(count, min, max):
        print(number)
