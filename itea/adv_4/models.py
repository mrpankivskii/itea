class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f'{self.restaurant_name} the restaurant with {self.cuisine_type} food')

    def open_restaurant(self):
        print('work time from 10:00 till 23:30')

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self):
        self.number_served += 1


class IceCreamStand(Restaurant):
    def __init__(self, flavors="chocolate, lime, kiwi, cherry"):
        self.flavors = flavors

    def flavors_describe(self):
        print(f'Chose your flavor: {self.flavors}')


class BinaryTree:

    def __init__(self):
        self.root = None

    def add_node(self, node):
        if self.root:
            self.root.add_node(node)
        else:
            self.root = node

    def __contains__(self, item):
        if not self.root:
            return False
        else:
            return item in self.root


class Node:

    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def add_node(self, node):
        if node.value < self.value:
            if self.left_node:
                self.left_node.add_node(node)
            else:
                self.left_node = node
        elif node.value > self.value:
            if self.right_node:
                self.right_node.add_node(node)
            else:
                self.right_node = node

    def __contains__(self, node):
        if self.value == node.value:
            return True
        if self.value < node.value:
            if self.right_node:
                return node in self.right_node
            return False
        elif self.value > node.value:
            if self.left_node:
                return node in self.left_node
            return False
