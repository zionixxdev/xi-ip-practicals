# Practical 10 : Conditional Constructs (if, if-else)
# Informatics Practices (065) - Class XI
# To take a decision in a program using the if and if-else constructs.

num = int(input("Enter a number : "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

marks = float(input("Enter marks : "))
if marks >= 33:
    print("Result : PASS")
else:
    print("Result : FAIL")