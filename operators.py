x = [1, 2, 3]
y = [1, 2, 3]
z = x

if z is x:
    print("x and z are the same object in memory.")
elif x is y:
    print("x and y are the same object in memory.")
elif x == y:   
    print("x and y have the same content but are different objects in memory.")
else:
    print("x and y are different objects in memory.")