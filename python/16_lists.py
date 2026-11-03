# Practical 16 : Lists Manipulation
# Informatics Practices (065) - Class XI
# To create a list and to add, insert, remove, modify, sort and reverse its elements.

marks = [78, 85, 92, 66, 74]
print(marks)
print("Sum :", sum(marks), "Max :", max(marks), "Min :", min(marks))

marks.append(88)
print("append :", marks)
marks.insert(2, 95)
print("insert :", marks)
marks.remove(66)
print("remove :", marks)
marks.sort()
print("sort   :", marks)