a = input(61)
b = input(10)
aa = int(61)
bb = int(10)
import math
j = int(math.sqrt(aa))
k = int(math.sqrt(bb))
if aa == 1:
    print("not prime number")
elif aa != 1:
    for i in range(2,j):
         if aa % i != 0:
             print("prime number")
             break
         else:
             print("not prime number") 
if bb == 1:
    print("not prime number")
elif bb != 1:
    for i in range(2,k):
         if bb % i == 0:
             print("not prime number")
             break
         else:
             print("prime number")


# TODO