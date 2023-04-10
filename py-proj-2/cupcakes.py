from abc import ABC, abstractmethod
import csv
from pprint import pprint


class Cupcake(ABC):

    def __init__(self, name, price, flavor, filling, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.filling = filling
        self.frosting = frosting
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for arg in args:
            self.sprinkles.append(arg)

    @abstractmethod
    def calculate_price(self, quantity):
        return self.price * quantity


class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return self.price * quantity


# my_cupcake = Cupcake("Boston Cream", 4.99, "original", "custard", "chocolate")
# my_cupcake.add_sprinkles("brownies", "chocolate")
# print(my_cupcake.sprinkles)

my_mini_cupcake = Mini("Bavarian Cream", 5.99, "original", "white chocolate")
my_mini_cupcake.add_sprinkles("rainbow")
print(my_mini_cupcake.size, my_mini_cupcake.name, my_mini_cupcake.price, my_mini_cupcake.flavor,
      my_mini_cupcake.frosting, my_mini_cupcake.sprinkles, my_mini_cupcake.calculate_price(3))


class Regular(Cupcake):
    size = "regular"

    def calculate_price(self, quantity):
        return self.price * quantity


class Large(Cupcake):
    size = "large"

    def calculate_price(self, quantity):
        return self.price * quantity


my_large_cupcake = Large("Vanilla", 3.99, "original", "cream", "vanilla cream")
my_large_cupcake.add_sprinkles("chocolate")
print(my_large_cupcake.size, my_large_cupcake.name, my_large_cupcake.price, my_large_cupcake.flavor, my_large_cupcake.filling,
      my_large_cupcake.frosting, my_large_cupcake.sprinkles, my_large_cupcake.calculate_price(2))


def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pprint(row)


read_csv("sample.csv")

cupcake1 = Regular("Stars and Stripes", 2.99,
                   "Vanilla", "Vanilla", "Chocolate")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)

cupcake_list = [cupcake1, cupcake2, cupcake3]


def write_new_csv(file, cupcake_list):
    with open(file, "w") as csvfile:
        fieldnames = ["size", "name", "price", "flavor",
                      "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for cupcake in cupcake_list:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor,
                                 "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor,
                                 "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


write_new_csv("sample.csv", cupcake_list)


def append_csv(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor",
                      "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor,
                             "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price,
                            "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


cupcake4 = Mini("Coconut", 3.99, "Vanilla", "Coconut")

append_csv("sample.csv", cupcake4)


def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None


def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor",
                      "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)


def delete_cupcake_csv(file, name):
    order_list = []
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        order_list = list(reader)
    with open(file, "w", newline="\n") as csvfile:
        for i in range(len(order_list)):
            if order_list[i]['name'] == name:
                del order_list[i]
                break
        fieldnames = ["size", "name", "price", "flavor",
                      "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for cupcake in order_list:
            writer.writerow(cupcake)
