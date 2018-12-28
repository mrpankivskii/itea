from shop import Shop, Discount


if __name__ == "__main__":
    store = Shop(shop_name="store", store_type="internet shop")
    store2 = Shop(shop_name="store2", store_type="internet shop2")
    store3 = Shop(shop_name="store3", store_type="internet shop3")
    print(store)
    store.describe_shop()
    store.open_shop()
    print(store.numbers_of_units)
    store.set_numbers_of_units(100)
    print(store.numbers_of_units)
    store.Increment_numbers_of_unit(5)
    print(store.numbers_of_units)
    store_discount = Discount("discount_store", "internet_shop")
    store_discount.get_discount_products()
