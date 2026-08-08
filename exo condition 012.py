
price_tablet = 720000
quantity_sold = 96
purchase_cost = 48000000

# Sales 
sales = price_tablet * quantity_sold

# Discount
if sales > 80000000 :
    discount = sales *0.20
elif sales > 70000000 :
    discount = sales *0.15
elif sales > 60000000 :
    discount = sales *0.10
elif sales > 50000000 :
    discount = sales *0.05
else :
    discount = 0

sales_after_discount = sales - discount

# Commission
commission = sales_after_discount *0.07
sales_after_commission = sales_after_discount - commission

# VAT
vat = sales_after_commission *0.18
sales_after_vat = sales_after_commission - vat

# Profit
profit = sales_after_vat - purchase_cost
profit_per_tablet = profit / quantity_sold

# Employee bonus
if profit > 30000000 :
    employee_bonus = 3000000
elif profit > 22000000 :
    employee_bonus = 2000000
elif profit > 14000000 :
    employee_bonus = 1000000
else :
    employee_bonus = 0

# Final profit
final_profit = profit + employee_bonus

# Company ranking
final_profit = profit + employee_bonus
if final_profit >= 40000000 and quantity_sold >= 90 :
    company_ranking = "Diament company"
elif final_profit >= 30000000 and quantity_sold >= 70 :
    company_ranking = "Platinum company"
elif final_profit >=20000000 and quantity_sold >= 50 :
    company_ranking = ("Gold company")
else :
    company_ranking = "Silver company"

# Director reward
if quantity_sold >= 100  or final_profit >= 45000000 :
     director_reward = "Diament reward"
elif quantity_sold >= 80 or final_profit >= 35000000 :
     director_reward = "Platinum reward"
elif quantity_sold >= 60 or final_profit >= 25000000 :
    director_reward = "Good reward"
else :
    director_reward = "Silver reward"

print("Price tablet:", price_tablet)
print("Profit per tablet:", profit_per_tablet)
print("Quantity sold:", quantity_sold)
print("Purchase cost:", purchase_cost)
print("Sales:", sales)
print("Commission:", commission)
print("Sales after commission:", sales_after_commission)
print("Vat:", vat)
print("Sales after vat:", sales_after_vat)
print("profit:", profit)
print("Employee bonus:", employee_bonus)
print("Final profit:", final_profit)
print("Company ranking:", company_ranking)
print("Director reward:", director_reward)
