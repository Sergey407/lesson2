class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        self.new_floor = new_floor
        if int(new_floor) < 1 or int(new_floor) > int(self.number_of_floors):
            print("Такого этажа не существует")
        else:
            i = 1
            while i <= int(new_floor):
                print(i)
                i += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, Кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):  #1
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):  # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):  #3
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value): #4
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

print(h1)

print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__

print(h1)

print(h1 == h2)

h1 += 10 # __iadd__

print(h1)

h2 = 10 + h2 # __radd__

print(h2)

print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__