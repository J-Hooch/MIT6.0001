#find years to save to buy house

annual_salary = float(input("Salary?"))
portion_saved = float(input("Portion savings percent?"))
total_cost = float(input("House cost?"))

portion_down_payment = total_cost * .25
monthly_saving = (annual_salary / 12) * portion_saved
current_savings = 0
months_saved = 0
while current_savings < portion_down_payment:
    current_savings = current_savings * (1 + .04 / 12)
    current_savings += monthly_saving
    months_saved += 1
print(months_saved)
