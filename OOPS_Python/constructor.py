class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name: str,price: float,quantity=1) :# here name: str means we have declared the data type of name

        # assert keyword are use to run validations to the recieved arguments
        assert price>=0,f"price is not greater than zero!"
        assert quantity>=0,f"quantity is not greater than zero!"

        self.name = name
        self.price = price
        self.quantity = quantity
        
        # actions ot execute
        Item.all.append(self)
    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price = self.price*self.pay_rate

    def __repr__(self) -> str:
        return f"Item('{self.name}',{self.price},{self.quantity})"



item1 = Item("phone",100,5)
item2 = Item("Laptop",1000)#here we have provided default value so you don't need to pass the quantity parameter
item3 = Item("Cable",10,5)
item4 = Item("Mousee",50,5)
item5 = Item("Keyboard",75,5)


print(item1.name)
print(item1.quantity)


print(item2.name)
print(item2.quantity)

print(item1.calculate_total_price())
print("price after discount: ")

item1.apply_discount()
print(item1.calculate_total_price())

# magic attribute
# print(Item.__dict__)#all the attributes of class level will be shown 
print(item1.__dict__)#all the attributes of instance level wiill be shown


item2.pay_rate = 0.7 #here we are changing pay rate of item2
print(item2.calculate_total_price())
print("price after discount: ")
item2.apply_discount()
print(item2.calculate_total_price())

print(Item.all)#listing obj in class 
for i in Item.all:
    print(i.name)