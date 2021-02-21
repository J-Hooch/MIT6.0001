
x = 25
epsilon = 0.01
#step = epsilon ** 2
numGuesses = 0
low = 0
high = max(1, x)
ans = (high + low) / 2
while abs(ans**2 - x) >= epsilon:
    print(f"low = {low}, high ={high} , ans = {ans}")
    numGuesses += 1

    if ans**2 < x :
        low = ans
    else:
        high = ans
    ans = (high + low) / 2
print(numGuesses)
print(f" {ans} is close to square root of {x}")