
price_tv = 750000
quantity_sold = 65
purchase_cost = 30000000

# Sales 
sales = price_tv * quantity_sold

# Discount

if sales >= 30000000 :
    discount = sales *0.15

elif sales >= 20000000 :
    discount = sales *0.10
else:
    discount = sales *0.05


sales_atfter_discount = sales - discount

print("Price tv:", price_tv)
print("Quantity sold:", quantity_sold)
print("Purchase cost:", purchase_cost)
print("Sales:", sales)
print("Sales after discount:", sales_atfter_discount)
