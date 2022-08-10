from random import *

# python标准库 类名驼峰命名 其余单词间下划线
# 文件 与 异常
# 随机数
print(randint(0, 10))

players = ['a', 'b', 'c', 'd']
count = 0
while count <= 10:
    print(choice(players))
    count += 1
print("----------------读取------------------")
file_path = "file/pi_digits.txt"
file_path_1 = "file/pi_million_digits.txt"
with open(file_path) as file_object:
    contens = file_object.read()
print(contens.rstrip())
print("----------------------------------")
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())
print("----------------------------------")
with open(file_path_1) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
# print(pi_string)
print(f"{pi_string[:52]}...")
print(len(pi_string))

print("----------------------------------")
birthday = input("Enter your birthday,in the form yymmdd:")
print(birthday)
if birthday in pi_string:
    print("\nyes")
else:
    print("\nno, sorry")

print("----------------写入------------------")
# w 覆盖写入 r 只读 a 累加写入
file_path = "file/game_test.txt"
with open(file_path, 'w', encoding='utf-8') as file_object:
    file_object.write("I like play phone games.\n")
    file_object.write("SuchAs lol\n")
print("写入完成！")


def get_contens(file_path):
    try:
        with open(file_path, encoding='utf-8') as file_object:
            contens = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_path} does not exist.")
    else:
        words = contens.strip()
        num_words = len(words)
        print(contens)
        print(f"The file {file_path} has about {num_words} words.")


print("----------------分析文本------------------")
get_contens(file_path)

file_paths = ["file/game_test.txt", "file/game_test2.txt", "file/pi_digits.txt"]
for file_path in file_paths:
    get_contens(file_path)

print("----------------异常------------------")
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    print(5 / 0)
except ZeroDivisionError:
    pass            #静默失败

line = "row,Row,row,row your boat"
print(line.count("row"))
print(line.lower().count("row")) # 全小写