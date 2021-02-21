#find years to save to buy house with raise
#we are given .07 semi annual raise roi .04, dwon payment .25, cost of house is 1M,
#we have 36 months to save (3 years)
#use bisectional search to solve for portion of slary to save




annual_salary = float(input("Salary?"))
total_cost = float(1000000)
portion_down_payment = total_cost * .25
semi_annual_raise = float(0.07)
months_saved = 36
current_savings = 0

#
epsilon = 100  # want to be within 100 dollars
save = 1
min_savings = 0
max_savings = save
num_guesses = 1

guess = ( max_savings + min_savings ) / 2


while abs(current_savings - portion_down_payment) >= epsilon:
    #calculate savings after 36 months where guess is portion saved
    current_savings = 0
    annual_salary_mod = annual_salary
    for i in range(1, months_saved + 1):
        monthly_saving = (annual_salary_mod / 12) * guess
        current_savings = current_savings * (1 + .04 / 12)
        current_savings += monthly_saving
        if i % 6 == 0:
            annual_salary_mod = annual_salary_mod * (1 + semi_annual_raise)

    if current_savings < portion_down_payment:
        min_savings = guess
    else:
        max_savings = guess
    guess = (max_savings + min_savings) / 2
    num_guesses += 1

print(guess)
print(num_guesses)



"""
while current_savings < portion_down_payment:
    monthly_saving = (annual_salary / 12) * portion_saved
    current_savings = current_savings * (1 + .04 / 12)
    current_savings += monthly_saving
    months_saved += 1
    if months_saved % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
print(months_saved)
"""