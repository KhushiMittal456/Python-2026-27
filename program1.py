marks = []
for i in range(5):
    m = float(input("Enter marks: "))
    marks.append(m)
total = sum(marks)
average = total / 5
percentage = (total / 500) * 100
print("Marks =", marks)
print("Total Marks =", total)
print("Average Marks =", average)
print("Percentage =", percentage, "%")