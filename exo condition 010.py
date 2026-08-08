
price_tv = 1250000
quantity_sold = 74
purchase_cost = 63000000

# Sales
sales = price_tv * quantity_sold

# Discount

if sales > 95000000 :
    discount = sales *0.25
elif sales > 85000000 :
    discount = sales *0.18
elif sales > 75000000 :
    discount = sales *0.12
elif sales > 65000000 :
    discount = sales *0.08
else :
    discount = 0

sales_after_discount = sales - discount

# commission 

commission = sales_after_discount *0.05
sales_after_commission = sales_after_discount - commission

# VAT

vat = sales_after_commission *0.18
sales_after_vat = sales_after_commission - vat

# Profit

profit = sales_after_vat - purchase_cost
profit_per_tv = profit / quantity_sold

# Employee bonus

if profit > 28000000 :
    employee_bonus = 3000000
elif profit > 20000000 :
    employee_bonus = 2000000
elif profit > 12000000 :
    employee_bonus = 1000000
else:
    employee_bonus = 0

# Final profit

final_profit = profit + employee_bonus

# Company ranking

if final_profit > 40000000 :
    company_ranking = "Diamond company"
elif final_profit > 30000000 :
    company_ranking = "Platinum company"
elif final_profit > 20000000 :
    company_ranking = "Gold company"
else :
    company_ranking = "Silver company"

# Director reward

if quantity_sold >= 100 :
    director_reward = "Diamond reward"
elif quantity_sold >= 80 :
    director_reward = "Platinum reward"
elif quantity_sold >= 60 :
    director_reward = "Gold reward"
else :
    director_reward = "Silver reward"


print("Price tv:", price_tv)
print("Quantity sold:", quantity_sold)
print("Purchase cost:", purchase_cost)
print("Sales:", sales)
print("Discount:", discount)
print("Sales after discount:", sales_after_discount)
print("Commission", commission)
print("Sales after commission", sales_after_commission)
print("VAT:", vat)
print("Sales after vat:", sales_after_vat)
print("Profit:", profit)
print("Profit per tv:", profit_per_tv)
print("Employee bonus:", employee_bonus)
print("final profit:", final_profit)
print("Company ranking:", company_ranking)
print("Director reward:", director_reward)