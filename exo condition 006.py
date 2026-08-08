
price_phone = 425000
quantity_sold = 96
purchase_cost = 28500000

# Sales
sales = price_phone *quantity_sold

if sales > 45000000 :
    discount = sales *0.18
elif sales > 35000000 :
    discount = sales *0.12
elif sales > 25000000 :
    discount = sales *0.07
else:
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


print("price phone:", price_phone)
print("Quantity sold:", quantity_sold)
print("Purchase cost:", purchase_cost)
print("Sales:", sales)
print("Sales after discount :", sales_after_discount)
print("Commission:", commission)
print("Sales after commission:", sales_after_commission)
print("VAT:", vat)
print("Sales after vat:", sales_after_vat)
print("Profit",profit)
print("profit per phone:", profit_per_phone)


# Profit

if profit > 12000000 :
    print("Exellent profit")
elif profit > 7000000 :
    print("Good profit")
elif profit > 2000000 :
    print("Average profit")
else:
    print("Low profit")