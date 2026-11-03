# Practical 11 : Multi-way Conditional Branching (if-elif-else)
# Informatics Practices (065) - Class XI
# To assign a grade to a student on the basis of marks using the if-elif-else chain.

marks = float(input("Enter marks : "))

if marks >= 90:
    grade = "A1"
elif marks >= 80:
    grade = "A2"
elif marks >= 70:
    grade = "B1"
elif marks >= 33:
    grade = "C1"
else:
    grade = "E"

print("Marks :", marks, "| Grade :", grade)