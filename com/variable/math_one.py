from math import fabs  # 导入数学模块
from time import perf_counter  # 导入时间模块


# 计算圆周率 8位以后耗时太久
def Bar(i):  # 动态文本条
    N = pow(10, level)
    a = int((i / N) * 50)
    b = 50 - a
    Y, N = '*' * a, '.' * b
    print("\r计算中：{:3.0f}% [{}->{}] {:.2f}s"
          .format(2 * a, Y, N, perf_counter()), end='')


level = eval(input('计算Pi精确到小数点后几位数：'))
print('\n{:=^70}'.format('计算开始'))
a, b, pi, tmp = 1, 1, 0, 1
i = 0
'''
a 分子  |  b 分母  |  pi 圆周率
tmp 存储a/b的值    |  i  执行进度
'''
perf_counter()  # 开始计时
while (fabs(tmp) >= pow(10, -level)):  # 计算Pi
    pi += tmp
    b += 2
    a = -a
    tmp = a / b
    i += 2
    Bar(i)  # 调用函数，实时显示计算进度

print('\n{:=^70}'.format('计算完成'))
print('\nPi的计算值为：{}'.format(round(pi * 4, level)))  # 输出计算结果
