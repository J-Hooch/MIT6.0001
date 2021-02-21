def g(x):
    def h():
        x = 'abc'
    x += 1
    print(f"g: x = {x}")
    h() #no return is just none
    return x

x = 3
z = g(x)

#h returns none so z = g(x) = x = 4