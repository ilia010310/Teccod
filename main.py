import math


def from_list_to_unique_list(some_list: list):
    new_list = list(set(some_list))
    return new_list


def from_nums_to_list(x: int, y: int):
    '''Функция принимающая 2 различных числа и
    возвращает список челых чисел от меньшего к большему ВКЛЮЧИТЕЛЬНО'''
    if x < y:
        my_list = [i for i in range(x, y + 1)]
        return my_list
    my_list = [i for i in range(y, x + 1)]
    return my_list


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        if isinstance(other_point, Point):
            dx = self.x - other_point.x
            dy = self.y - other_point.y
            return math.sqrt(dx ** 2 + dy ** 2)

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


def sort_list_of_strings_up(some_list: list):
    return sorted(some_list, key=lambda x: len(x))


def sort_list_of_strings_down(some_list: list):
    return sorted(some_list, key=lambda x: len(x), reverse=True)


# tests
# 1
my_list1 = [1, 1, 1, 2, 2, 3, 10]
print(from_list_to_unique_list(my_list1))

# 2

a = 1
b = 49
print(from_nums_to_list(a, b))

# 3

point1 = Point(1, 2)
point2 = Point(4, 6)

print("Координаты первой точки:", point1.get_coordinates())
print("Координаты второй точки:", point2.get_coordinates())
point1.set_coordinates(3, 5)
print("Новые координаты первой точки:", point1.get_coordinates())

distance = point1.distance(point2)
print("Растояние между 1 и 2 точками:", distance)

# 4

my_list4 = ['1', '22', '4444', '7777777', '333', '999999999', '88888888', '55555', '666666']

print(sort_list_of_strings_up(my_list4))
print(sort_list_of_strings_down(my_list4))
