# Basic classe snad Object
# class Car:
#     brand=None
#     model=None
# my_car=Car()
# print(my_car)



class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        print(self)
    
         

my_car=Car("Toyota","Corolala")
print(my_car.brand)

my_new_car=Car("Tata","Safari")
print(my_new_car)