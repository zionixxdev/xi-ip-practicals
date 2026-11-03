# Practical 17 : Dictionaries (Key-Value Mapping)
# Informatics Practices (065) - Class XI
# To create a dictionary of a student's record and to add, update and delete its items.

student = {"Roll No": 2, "Name": "Aditya", "Marks": 87}

print(student)
print("Name :", student["Name"], "| Items :", len(student))

student["Class"] = "XI-A"
student["Marks"] = 91
print("After add and update :", student)

del student["Class"]
print("After deleting Class :", student)

for key, value in student.items():
    print("  ", key, ":", value)