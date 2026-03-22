# 求解方程组：
# 3x + 4y = 40
# 3x - 4y = 20

x = 10
y = 2.5

print("x =", x)
print("y =", y)

print("helloworld")

# 求解：
# a² + b² = 25
# a - b = 1

import sympy

a, b = sympy.symbols('a b', real=True)
sol_ab = sympy.solve([a**2 + b**2 - 25, a - b - 1], [a, b])
print("a,b 的解：", sol_ab)

print(sympy.__version__)

x=(2**2+5)/3.6
print("x =", x)