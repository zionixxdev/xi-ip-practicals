# Practical 13 : Iteration with for Loop
# Informatics Practices (065) - Class XI
# To print the multiplication table of a number, the sum of the first n natural numbers and the factorial of n using a for loop.

n = int(input("Enter a number : "))

for i in range(1, 6):
    print(n, "x", i, "=", n * i)

total = sum(range(1, n + 1))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Sum 1 to", n, "=", total)
print("Factorial =", fact)