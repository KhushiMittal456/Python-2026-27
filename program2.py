basic_salary = float(input("Enter basic salary: "))

DA = basic_salary * 0.10
HRA = basic_salary * 0.20

gross_salary = basic_salary + DA + HRA

tax = gross_salary * 0.05

net_salary = gross_salary - tax

print("DA =", DA)
print("HRA =", HRA)
print("Gross Salary =", gross_salary)
print("Tax Deduction =", tax)
print("Net Salary =", net_salary)
