#класс исключений
class exceptions():

#класс точек кораблей
class dot():
    def __init__(self, ship_x, ship_y) -> None:
    self.ship_x = ship_x
    self.ship_y = ship_y

    def __eq__(self, dots) -> bool:
        return self.dot in self.dots #mb i tak !


#класс кораблей с длиной, точкой носа корбаля, ориентация корабля(горизонтально/вертикалько),
#количество неподбитых точек корабля
class ship(length, dot_nose, orientation, life_dot ):
    def dots(self):
        return self.dots() #mb i tak !


#класс игровых досок
class boards():
    def add_ship(self):



    def board_player(self):


    def board_computer(self):