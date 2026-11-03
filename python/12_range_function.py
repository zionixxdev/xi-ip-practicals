# Practical 12 : The range() Function
# Informatics Practices (065) - Class XI
# To study the working of range() by generating different sequences of numbers.

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(2, 11, 2)))
print(list(range(10, 0, -2)))
print("Sum 1 to 10 :", sum(range(1, 11)))
for i in range(1, 6):
    print(i ** 2, end=" ")