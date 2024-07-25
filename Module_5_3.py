class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название:{self.name},кол-во этажей:{self.number_of_floors}'
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self,other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        self.number_of_floors += value
        return self
    def __radd__(self, value):
        self.number_of_floors += value
        return self
    def __iadd__(self, value):
        self.number_of_floors += value
        return self
house1 = House('ЖК Эльбрус',30)
house2 = House('ЖК Нью - Васюки',40)
print(house1)
print(house2)
print(house1 == house2)
house1 = house1 + 6
print(house1)
print(house1 == house2)
house1 += 5
print(house1)
house2 = 4 + house2
print(house2)
print(house1 > house2)
print(house1 >= house2)
print(house1 < house2)
print(house1 <= house2)
print(house1 != house2)