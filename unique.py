class Unique:
    def __init__(self, data, **kwargs):
        self.data = data
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __iter__(self):
        for item in self.data:
            # Приводим строку к нижнему регистру, если ignore_case == True
            normalized_item = item.lower() if self.ignore_case and isinstance(item, str) else item

            # Проверяем наличие дубликата
            if normalized_item not in self.seen:
                self.seen.add(normalized_item)
                yield item


# Пример использования
if __name__ == '__main__':
    items = ['apple', 'Apple', 'banana', 'banana', 'cherry', 'apple', 'Cherry']
    unique_items = Unique(items, ignore_case=True)

    for item in unique_items:
        print(item)


    # Тестирование с генератором
    def generator():
        yield 'dog'
        yield 'cat'
        yield 'dog'
        yield 'Cat'
        yield 'fish'


    unique_gen = Unique(generator(), ignore_case=True)

    for item in unique_gen:
        print(item)
