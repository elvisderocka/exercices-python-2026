
price_printer = 285000
quantity_sold = 185
purchase_cost = 35000000

# Sales 
sales = price_printer * quantity_sold

# Discount
if sales > 60000000 :
    discount = sales *0.18
elif sales > 50000000 :
    discount = sales *0.12
elif sales > 40000000 :
    discount = sales *0.8
elif sales > 30000000 :
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
profit = sales_after_vat - quantity_sold
profit_per_printer = profit / quantity_sold

if profit > 20000000 :
    bonus = 2000000
elif profit > 1500000 :
    bonus = 1200000
    if profit > 8000000 :
        bonus = 600000
    else :
        bonus = 0

# Final profit
final_profit = profit + bonus

if final_profit > 25000000 : 
    print("Outstanding company")
elif final_profit > 18000000 :
    print("Exellent company")
elif final_profit > 10000000 :
    print("Good company")
else :
    print("Average company")

# Prime of director
if quantity_sold > 180 :
    director_bonus = ("gold bonus")
elif quantity_sold > 120 :
    director_bonus = ("silver bonus")
else:
    director_bonus = ("No bonus")



print("Price printer:", price_printer)
print("Quantity sold:", quantity_sold)
print("purchase cost:", purchase_cost)
print("Sales:", sales)
print("Discount:", discount)
print("Sales after discount:", sales_after_discount)
print("Commission:", commission)
print("Sales after commission:", sales_after_commission)
print("VAT:", vat)
print("Sales after vat:", sales_after_vat)
print("Profit:", profit)
print("profit per printer:", profit_per_printer)
print("bonus:", bonus)
print("Final profit:", final_profit)
print("Director bonus:", director_bonus)

