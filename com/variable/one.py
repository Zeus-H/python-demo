message = "Hello world"
print(message)

print("# 首字母大小 全大写 全小写")
name = "jaSon world"
print(name.title())
print(name.upper())
print(name.lower())

print("# 要在字符中使用变量值， 引号前要加字母f format 作用：识别花括号")
first_name = "jason"
last_name = "world"
full_name = f"{first_name} {last_name}"
print(full_name.title())
print(f"Hello {full_name.title()}")
massage_2 = f"Hello {full_name.title()}!"
print(massage_2)
print("Hello,{} {}!".format(first_name, last_name).title())

print("# \\t 空格符 \\n 换行符")
print("hello:\n\tjason\tworld!".title())

print("# rstrip 删除末尾空格 lstrip 删除开头空格 strip 删除两边空格")
print(" hello: jason world! ".title().rstrip())
print(" hello: jason world! ".title().lstrip())
print(" hello: jason world! ".title().strip())