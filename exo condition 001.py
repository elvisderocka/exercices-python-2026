
price_laptop = 650000
quantity_sold = 54
purchase_cost = 25000000

# Sales 
sales = price_laptop * quantity_sold

# Discount

if sales >= 20000000 : 

     discount = sales *0.10
else :
     discount = sales *0.06

sales_after_discount = sales - discount

# Commission
commission = sales_after_discount *0.05
sales_after_commission = sales_after_discount - commission

# VAT
vat = sales_after_commission *0.18
sales_after_vat = sales_after_commission - vat

# Transport
transport_cost = sales_after_vat *0.02
sales_after_transport = sales_after_vat - transport_cost

# Storage
storage_cost = sales_after_transport *0.01
sales_after_storage = sales_after_transport - storage_cost

# Profit
profit = sales_after_storage - purchase_cost
profit_per_laptop = profit / quantity_sold



print("Sales:", sales)
print("Discount:", discount)
print("Sales after discount:", sales_after_discount)
print("Commission:", commission)
print("Sales after commission:", sales_after_commission)
print("VAT:", vat)
print("Sales after vat:", sales_after_vat)
print("Transport:", transport_cost)
print("Sales after transport:", sales_after_transport)
print("Storage:", storage_cost)
print("Sales after storage:", sales_after_storage)
print("Profit:", profit)
print("Profit per laptop:", profit_per_laptop)

