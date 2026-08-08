
price_tablet = 315000
quantity_sold = 145
purchase_cost = 36000000

# Sales
sales = price_tablet * quantity_sold

# Discount
if sales  > 50000000 :
    discount = sales *0.20
elif sales > 40000000 :
    discount = sales *0.15 
elif sales > 30000000 :
    discount = sales *0.10
elif sales > 20000000 : 
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

if profit > 18000000 :
    print("oustandig profit")
elif profit > 12000000 :
    print("Exellent profit")
elif profit > 7000000 :
    print("Good profit")
elif profit > 3000000 :
    print("Average profit")
else :
    print("No profit")

print("Price tablet:", price_tablet)
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
print("Profit per tablet:", profit_per_tablet)



