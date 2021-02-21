#newton-raphoson for square root
#find x such that x**2 - 24 is within epsilon of  0
epsilon = 0.01
y = 24.0
guess = y/2
while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y) / (2*guess))
print(f"Square root of {y} is about {guess}")