num = int(input("Enter an integer: "))

original = num
count = 0
sum = 0

# Count the number of digits
temp = num

while temp > 0:
    count = count + 1
    temp = temp // 10

# Calculate the sum of powers of digits
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10

# Check Armstrong number
if sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")