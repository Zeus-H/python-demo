# 类
from com.variable.dao.car import Car,Battery


class Dog:
    """ 一次模拟小狗简单尝试 """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


class Pet(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sit(self):
        print(f"This my pet,It name is {self.name}")


my_dog = Dog('wang', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

my_dog.age = 7
print(f"My dog's {my_dog.age} years old.")

# 类的继承
my_pet = Pet('xing', 25)
my_pet.sit()
my_pet.roll_over()

my_car = Car('subalu', 'BRZ', 2022)
my_car.get_name()
my_battery = Battery(100)
my_battery.describe_battery()
