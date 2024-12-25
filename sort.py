#С использованием lambda-функции
data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
result = sorted(data, key=lambda x: abs(x), reverse=True)
print(result)


#Без использования lambda-функции
data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

def sort_key(x):
    return abs(x)

result = sorted(data, key=sort_key, reverse=True)
print(result)
