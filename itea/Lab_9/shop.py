class Shop:
    numbers_of_units = 0
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type

    def describe_shop(self):
        print("my.shop - {}\ntype of shop is - {}\n".format(self.shop_name, self.store_type))


    def open_shop(self):
        print("shop is open")


    def set_numbers_of_units(self,number):
        self.numbers_of_units = number


    def Increment_numbers_of_unit(self,number_inc):
        self.numbers_of_units += number_inc


    def describe_shop(self):
        print("my.shop - {}\ntype of shop is - {}\n".format(self.shop_name, self.store_type))


    def open_shop(self):
        print("shop is open")


    def set_numbers_of_units(self,number):
        self.numbers_of_units = number


    def Increment_numbers_of_unit(self,number_inc):
        self.numbers_of_units += number_inc

class Discount(Shop):
    discount_products = ['0', '1', '2', '3']

    def get_discount_products(self):
        print(self.discount_products)
