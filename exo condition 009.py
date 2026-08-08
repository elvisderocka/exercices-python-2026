
price_computeur = 850000
quantity_sold = 68
purchase_cost = 42000000

# Sales 
sales = price_computeur * quantity_sold

# Discount 

if sales > 70000000 :
    discount = sales *0.20
elif sales > 60000000 :
    discount = sales *0.15
elif sales > 50000000 :
    discount = sales *0.10
elif sales > 40000000 :
    discount = sales *0.05
else :
    discount = 0

sales_after_discount = sales - discount

# Commission 
commission = sales_after_discount *0.06
sales_after_commission = sales_after_discount - commission

# VAT
vat = sales_after_commission *0.18
sales_after_vat = sales_after_commission - vat

# Profit
profit = sales_after_vat - purchase_cost
profit_per_compateur = profit / quantity_sold

# Employee bonus
if profit > 20000000 :
    employee_bonus = 2500000
elif profit > 15000000 :
    employee_bonus = 1500000
elif profit > 8000000 :
    employee_bonus = 800000
else :
    employee_bonus = 0

# final profit
final_profit = profit + employee_bonus 

# Company rankig
 
if final_profit >= 30000000 :
    company_ranking = "Platinum company"
elif final_profit >= 22000000 :
    company_ranking = "Gold company"
elif final_profit >= 15000000 :
    company_ranking = "Silver company" 
else :
    company_ranking = "Bronze company"


# Director reward
if quantity_sold >= 80 :
    director_reward = "Diamond reward"
elif quantity_sold >= 60 :
    director_reward = "Gold reward"
elif quantity_sold >= 40 :
    director_reward = "Silver reward"
else :
    director_reward = "No reward"


print("Price computer:", price_computeur)
print("Quantity sold:", quantity_sold)
print("Purchase cost:", purchase_cost)
print("Sales:", sales)
print("Discount:", discount)
print("Sales after discount:", sales_after_discount)
print("Commission:", commission)
print("Sales after commission:", sales_after_commission)
print("VAT:", vat)
print("Sales after vat:", sales_after_vat)
print("Profit:", profit)
print("Profit per computer:", profit_per_compateur)
print("Employee bonus:", employee_bonus)
print("Final profit:", final_profit)
print("Company rankig:", company_ranking)
print("Director reward:", director_reward)

