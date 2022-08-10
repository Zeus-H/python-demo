# 输入
message = input("输入数值:")
print(f'{message}:'.title())

message = int(message)
print(f'\n是否大于10:{message > 10}')
print(f'余数:{message % 2}')

num = int(message)
if num <= 100:
    while num <= 100:
        print(num)
        num += 1

while message != 'exit':
    message = input("退出请输入'exit'你输入嘛:")
    print(message)

responses = {}
active = True
while active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes /no)")
    if repeat == 'no':
        active = False
print("\n --- Poll Results ---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}")

