# Practical 6 : Input and Output Statements
# Informatics Practices (065) - Class XI
# To read data from the keyboard using input() and to display a report using print().

name = input("Name    : ")
roll = int(input("Roll No.: "))
eng = float(input("English : "))
maths = float(input("Maths   : "))
ip = float(input("IP      : "))

total = eng + maths + ip
print("Total   :", total, "| Average :", round(total / 3, 2))
print("Result  :", "PASS" if total / 3 >= 33 else "FAIL")