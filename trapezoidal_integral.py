
from math import sin
# --example--
# print(sin(0))
# >>>0 
# -----------
import math
math.pi
def tra_rule(f, a = 0 ,b = 1 ,n = 100):
    h = (b - a) / n
    ans = 0
    for k in range(1, n + 1):
        x = a + (k - 1) * h
        F = (h / 2) * (f(x) + f(x + h))
        ans += F
        return ans

ans_1 = tra_rule(math.sin, 0 , math.pi / 2 , 50)
print(ans_1)

ans_2 = tra_rule(lambda x: 4 / (1 + x**2) , 0 , 1 , 100)
print(ans_2)

ans_3 = tra_rule(lambda x: math.pi ** (1 / 2) * math.exp(-x**2) , -100 , 100 , 1000)
print(ans_3)

    
        
    