
price_phone = 1450000
quantity_sold = 88
purchase_cost = 79000000

# Sales

sales = price_phone * quantity_sold

# Discount

if sales > 120000000 :
    discount = sales *0.22
elif sales > 100000000 :
    discount = sales *0.18
elif sales > 80000000 :
    discount = sales *0.12
elif sales > 60000000 :
    discount = sales *0.08
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
profit_per_phone = profit / quantity_sold

# Employee bonus

if profit > 35000000 :
    employee_bonus = 3500000
elif profit > 25000000 :
    employee_bonus = 2500000
elif profit > 15000000 :
    employee_bonus = 1500000
else :
    employee_bonus = 0

# Final profit

final_profit = profit + employee_bonus

# Company ranking

if final_profit >= 40000000 and quantity_sold >= 80 :
    company_ranking ="Elite company"
elif final_profit >= 30000000 and quantity_sold >= 70 :
    company_ranking = "Platinum company"
elif final_profit >= 20000000 and quantity_sold >= 50 :
    company_ranking ="Gold company"
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
    director_reward = "Silver bonus"


print("Price phone:", price_phone)
print("Profit per phone:", profit_per_phone)
print("Quantity sold:", quantity_sold)
print("Purchase cost:", purchase_cost)
print("Sales:", sales)
print("Discount:", discount)
print("Sales after discount:", sales_after_discount)
print("Commission:", commission)
print("Sales after commission:", sales_after_commission)
print("VAT:", vat)
print("sales after vat:", sales_after_vat)
print("Profit:", profit)
print("Employee bonus:", employee_bonus)
print("Final profit:", final_profit)
print("Company ranking:", company_ranking)
print("Director reward:", director_reward)




