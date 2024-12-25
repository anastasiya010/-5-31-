def field(goods, *args):
    for item in goods:
        if len(args) == 1:  # Если передан только один аргумент
            key = args[0]
            value = item.get(key)
            if value is not None:  # Пропускаем, если значение None
                yield value
        else:  # Если передано несколько аргументов
            result = {key: item.get(key) for key in args if item.get(key) is not None}
            if result:  # Пропускаем, если все значения None
                yield result


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': 'Тумба', 'price': 3000, 'color': 'white'}
]

# Генерация значений для одного ключа
for value in field(goods, 'title'):
    print(value)

# Генерация словарей для нескольких ключей
for item in field(goods, 'title', 'price'):
    print(item)

