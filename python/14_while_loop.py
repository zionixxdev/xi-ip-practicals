# Practical 14 : Iteration with while Loop
# Informatics Practices (065) - Class XI
# To find the sum of the digits, the reverse and the number of digits of a number using a while loop.

n = 4729
temp, total, reverse, count = n, 0, 0, 0

while temp > 0:
    digit = temp % 10
    total += digit
    reverse = reverse * 10 + digit
    count += 1
    temp //= 10

print("Sum of digits :", total)
print("Reverse       :", reverse)
print("Number of digits :", count)