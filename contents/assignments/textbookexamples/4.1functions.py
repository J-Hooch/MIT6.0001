def max(x, y):
    if x > y:
        return x
    else:
        return y
max(3,2)  #this will return 3 or x

def isin(x, y):
    if x in y:
        return True
    else:
        return False

#print(str(isin("ape", "poop, ape")))

#scoping
def f(x):
    y = 1
    x = x + y
    print(f"x = {x}")
    return x
x = 3
y = 2
z = f(x)
print(f"z = {z}")
print(f"x = {x}")
print(f"y = {y}")
