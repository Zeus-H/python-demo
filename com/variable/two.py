print(6 + 3)
print(6 - 3)
print(6 * 3)
print(6 / 3)
print(6 / 3)
print(3 ** 2)
print(3 ** 3)

print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)

print(0.2 + 0.1)
print(3 * 0.1)

num = 1_000_000
print(num)

# 对列表进行操作
bicycles = ['a', 'b', 'c']
print(bicycles)
print(bicycles[0].title())
print(f"jason world {bicycles[0]}".title())

bicycles[0] = 'd'
print(bicycles)

bicycles.append('a')
print(bicycles)
bicycles.insert(1, 'e')
print(bicycles)
del bicycles[0]
print(bicycles)
# 删除末尾 popped 取出/弹出
bicycles_1 = bicycles.pop()
print(bicycles)
print(bicycles_1)
print(bicycles.pop(0))
bicycles.remove('c')
print(bicycles)

bicycles = ['a', 'c', 'b']
bicycles.sort()
print(bicycles)
# 倒序
bicycles.sort(reverse=True)
print(bicycles)
print(sorted(bicycles))
# 倒序打印
bicycles = ['a', 'c', 'b']
bicycles.reverse()
print(bicycles)

# 遍历
bicycles = ['a', 'b', 'c', 'd']
print(bicycles)
for bicycle in bicycles:
    print(bicycle)

for value in range(1, 5):
    print(value)

# 打印偶数 从2开始 11结束 不断加2
num = list(range(2, 11, 2))
print(num)
# 统计
num = list(range(0, 10))
print(num)
print(min(num))
print(max(num))
print(sum(num))

# 列表解析 value**2 平方根
num = [value ** 2 for value in range(1, 11)]
print(num)

# 切片
num = list(range(0, 10))
print(num)
print(num[0:3])
print(num[3:6])
print(num[:4])
print(num[2:])
print(num[-2:])

# 复制
num_1 = num[:]
num.append("10")
print(num_1)
print(num)
num.pop()

# 这样的复制 其实是引用了同一个地址
num_2 = num
num.append("10")
print(num_2)
print(num)

num = (1, 2)
print(num)
print(num[0])
print(num[1])

cars = list(range(0, 10))
print(cars)
for car in cars:
    if car == 6:
        print('six'.title())
    else:
        print(car)

num = 10
if num != 1 and num != 2 or num < 3:
    print(f'{num}:不是1,2,3')
elif num > 10:
    print(f'{num} 大于10')
else:
    print(num)

string = []
if string:
    print(string)
else:
    print('空的啦！')

# 是否包含
nums = list(range(0, 10))
print(10 in nums)
print(0 in nums)
print(0 not in nums)

# 字典
map = {'a':'1','b':2}
print(map)
print(map['b'])
map['c'] = 3
print(map)
map['b'] ='2'
print(map)
del map['c']
print(map)
map_1 = map.get('a')
print(map_1)

for key,value in map.items():
    print(f'key:{key},value:{value}')

for name,languages in map.items():
    print(f'name:{name},languages:{languages}')

for k in map.keys():
    print(f'k:{k},v:{map[k]}')

for v in map.values():
    print(f'v:{v}')

if 'a' in map.keys():
    print('包含在里面')