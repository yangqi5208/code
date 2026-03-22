# 打印 "helloworld"
print("helloworld")
# 初始化计数器
count = 0
# 初始化总和
total = 2
# 当总和小于10时循环
while total < 10:
    # 每次增加2
    total += 2
    # 计数器加1
    count += 1
# 打印结果
print(f"需要加 {count} 次")



# 设置变量a为3
a=3
# 设置变量b为4
b=4
# 计算勾股定理中的斜边
c=(a**2+b**2)**0.5
# 打印c的值
print("c =", c)


# 设置x为10
x = 10
# 设置y为2.5
y = 2.5
# 打印x
print("x =", x)
# 打印y
print("y =", y)

# 求解方程组：3x + 4y = 10, x - y = 6
# 导入sympy库
import sympy
# 定义符号变量x和y
x, y = sympy.symbols('x y')
# 求解方程组
sol = sympy.solve([3*x + 4*y - 10, x - y - 6], [x, y])
# 打印x的解
print("x =", sol[x])
# 打印y的解
print("y =", sol[y])

a = 1
b = 2
c = (a**2 + b**2)**0.5

print("c =", c)



