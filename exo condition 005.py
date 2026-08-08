
price_laptop = 760000
quantity_sold = 78
purchase_cost = 40000000

sales = price_laptop * quantity_sold

 # Discount

if sales > 40000000 :
    discount = sales *0.15
elif sales > 25000000 :
    discount = sales *0.10
else :
    discount = 0

sales_after_discount = sales - discount

# Commission

commission = sales_after_discount *0.05
sales_after_commission = sales_after_discount - commission

# VAT
vat = sales_after_commission *0.18
sales_after_vat = sales_after_commission - vat

# Profit

profit = sales_after_vat - purchase_cost
profit_per_laptop = profit / quantity_sold


print("Price laptop:", price_laptop)
print("Quantity sold:", quantity_sold)
print("Purchase cost:", purchase_cost)
print("Sales", sales)
print("Discount:", discount)
print("sales_after_discount:", sales_after_discount)
print("Commission:", commission)
print("Sales after commission:", sales_after_commission)
print("VAT", vat)
print("Sales after vat:", sales_after_vat)
print("Profit:", profit)
print("Profit per laptop:", profit_per_laptop)

if profit > 40000000 :
    print("high profit")
elif profit > 35000000 :
    print("Medium profit")
else : 
    print("Low profit")





