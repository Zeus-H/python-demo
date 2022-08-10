import json

# load 加载  dump 存储

nums = [2, 3, 4, 5, 6, 7, 8, 9]
file_path = 'file/numbers.json'
# 写入
with open(file_path, 'w') as f:
    json.dump(nums, f)

# 读取
with open(file_path) as f:
    nums = json.load(f)
print(nums)

file_path = "file/username.json"
while True:
    content = input("What is your name? ").title()
    if content == 'Exit' or content == 'Quit':
        print("End!!!!")
        break
    else:
        with open(file_path, 'a') as f:
            json.dump(content, f)
            print(f"We'll remember you when you com back, {content}!")

# 文件不存在就会新建
file_path = "file/usercontent.json"
try:
    with open(file_path) as f:
        content = json.load(f)
except FileNotFoundError:
    content = input("What is your name? ")
    with open(file_path, 'w') as f:
        json.dump(content, f)
        print(f"We'll remember you when you com back, {content}!")
else:
    print(f"Welcome back,{content}!")

print("------------------------------------------------")

def greet_user(num):
    file_path = f'file/username{num}.json'
    try:
        with open(file_path) as f:
            content = json.load(f)
    except FileNotFoundError:
        content = input("What is your name? ")
        with open(file_path, 'w') as f:
            json.dump(content, f)
            print(f"We'll remember you when you com back, {content}!")
    else:
        print(f"Welcome back,{content}!")

# 执行
greet_user(1)


def get_username():
    file_path = 'file/username1.json'
    try:
        with open(file_path) as f:
            content = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return content

def greet():
    username = get_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name ?")
        file_path = 'file/username.json'
        with open(file_path,'a') as f:
            json.dump(username,f)
            print(f"We'll remember you when you com back, {content}!")

# 执行
greet()