# TODO
i = 1
while True:
    e = (1 / 2 )**i
    if 1 + e == 1: 
        e = (1 / 2 )**(i - 1)
        break
    i += 1
print( e )