# Practical 9 : Relational and Logical Operators
# Informatics Practices (065) - Class XI
# To evaluate relational and logical expressions in Python.

a, b, c = 10, 20, 15

print(a > b, a < b, a == c, a != c)
print(b >= c, b <= c)
print((a < b) and (b > c))
print((a > b) or (b > c))
print(not (a == c))
age = 17
print("Can vote :", age >= 18 and age <= 120)