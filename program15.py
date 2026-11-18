data = float(input("Enter monthly data usage in GB: "))
if data <= 2:
    bill = data * 50
elif data <= 5:
    bill = (2 * 50) + ((data - 2) * 40)
elif data <= 10:
    bill = (2 * 50) + (3 * 40) + ((data - 5) * 30)
else:
    bill = (2 * 50) + (3 * 40) + (5 * 30) + ((data - 10) * 20)
print("Total Bill =", bill)