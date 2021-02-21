#find years to save to buy house with raise

annual_salary = float(input("Salary?"))
portion_saved = float(input("Portion savings percent?"))
total_cost = float(input("House cost?"))
semi_annual_raise = float(input("Raise percent?"))

portion_down_payment = total_cost * .25

current_savings = 0
months_saved = 0
while current_savings < portion_down_payment:
    monthly_saving = (annual_salary / 12) * portion_saved
    current_savings = current_savings * (1 + .04 / 12)
    current_savings += monthly_saving
    months_saved += 1
    if months_saved % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
print(months_saved)
