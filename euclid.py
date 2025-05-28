import random

def euclid(a,b):
    while b != 0:
        a, b = b, a % b
    return a
    if a % b == 1:
        return False
    print("tagainiso")

print(euclid(10,20))
print(euclid(14,91))
print(euclid(91,14))

count = 0
for a in range(100000):
    a = random.randint(1,10001)
for b in range(100000):
    b = random.randint(1,10001)
    if euclid(a, b) == 1:
        count += 1

print(count/100000)