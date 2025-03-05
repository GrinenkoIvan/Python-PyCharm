# Абстрактные классы

from abc import ABC, abstractmethod

class Chess(ABC):  # Абстрактный класс
    def draw(self):
        print("Нарисовал шахматную фигуру")

    @abstractmethod
    def move(self):
        print('Метод move() в базовом классе ')


class Queen(Chess):
    def move(self):
        super().move()
        print("Двигаться королевой")




q = Queen()
q.draw()
q.move()



