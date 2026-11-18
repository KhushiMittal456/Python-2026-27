maths = float(input("Enter marks in Mathematics: "))
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))
total = maths + physics + chemistry
percentage = total / 3
if maths >= 60 and physics >= 50 and chemistry >= 50 and percentage >= 60:
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")
print("Overall Percentage =", percentage)