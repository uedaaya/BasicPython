from math import sin
# --example--
# print(sin(0))
# >>>0 
# -----------
import math
math.pi
result = 0
h = math.pi/200
for number in range(1,101):
    parts = (h/2)*(sin((number-1)*h)+sin((number)*h))
    result += parts
print(result)  
    