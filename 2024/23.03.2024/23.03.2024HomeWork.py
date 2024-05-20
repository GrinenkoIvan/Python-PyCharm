class OrderDirect:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if value is None:
            raise ValueError(f'{self.__name} должно быть числом')
        if not isinstance(value, int) or value < 0:
            raise ValueError(f'{self.__name} должно быть положительным числом')
        instance.__dict__[self.__name] = value


class Order:
    count = OrderDirect()
    price = OrderDirect()

    def __init__(self, title, count, price):
        self.title = title
        self.count = count
        self.price = price



p = Order('apple', 5, 10)


a = p.title, p.count, p.price
print('Order', a)
print(p.count * p.price, 'шт')
