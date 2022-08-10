import four_one
from four_one import make_pizza as mp
from four_one import *


# 定义函数
def user():
    print("Hello!")


def user_1(name):
    print(f"Hello! {name}")


def user_2(pet, name):
    print(f"I have a {pet}.")
    print(f"My {pet}'s name is {name.title()}")


def user_3(name, pet='dog'):
    print(f"I have a {pet}.")
    print(f"My {pet}'s name is {name.title()}")


def get_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


def get_name_1(first_name, last_name, middle_name=''):
    full_name = f"{first_name} {last_name} {middle_name}"
    return full_name.title()


def build_person(first_name, last_name):
    return {'first_name': first_name, 'last_name': last_name}


# 任意的形参
def pizza(*param):
    print(param)


# 任意的形参
def pizza_1(first, last, **param):
    param['first_name'] = first
    param['last_name'] = last
    print(param)


# 执行函数
user()
user_1("Jason")
user_2('cat', "mimi")
user_2(name='wang', pet="dog")
user_3(name='xing')
name = get_name("Jason", "Huang")
print(f"My name is {name}")
name = get_name_1("Jason", "world", "Huang")
name_1 = get_name_1("Jason", "Huang")
print(f"My name is {name}")
print(f"My name is {name_1}")
musician = build_person("Jason", "Huang")
print(musician)
pizza('a', 'b', 3, 'c')
pizza_1('jason', ' world', location='a', field='b')

four_one.make_pizza(10, 'haha')
four_one.make_pizza(6, 'haha', 'xixi')
mp(12, 'haha', 'xixi', 'qiqi')

four_one.make()