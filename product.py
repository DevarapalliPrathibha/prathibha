class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
    def display_product_details(self):
        print(self.name)
        print(self.price)
        print(self.deal_price)
        print(self.ratings)
    def get_deal_price(self):
        print(self.deal_price)
class electronic(Product):
    def set_warrenty(self,warrenty):
        self.warrenty = warrenty
    def get_warrenty(self):
        return self.warrenty
class grocery(Product):
        pass
class Order:
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address =delivery_address
    def add(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("quantity:{}".format(quantity))
    def display_total_bill(self):
        total_bill = 0
        for product,quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
            print("total_bill:{}".format(total_bill))
lap = electronic("lap",30000,25000,4)
order = Order("prime delivery","hyd")
order.add("milk",3)
order.add("lap",2)
print("++++")
order.display_order_details()
print("++++")
order.display_total_bill()















