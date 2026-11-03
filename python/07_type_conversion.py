# Practical 7 : Explicit Type Conversion (Typecasting)
# Informatics Practices (065) - Class XI
# To convert values from one data type to another using int(), float() and str().

a, b, c = "45", "3.14", 2025

print(int(a), type(int(a)))
print(float(b), type(float(b)))
print(str(c), type(str(c)))
print(int(float(b)), "-> fraction removed")
print(int(a) + 100)
print(bool(0), bool(1), bool(""), bool("IP"))