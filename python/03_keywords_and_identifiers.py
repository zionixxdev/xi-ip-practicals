# Practical 3 : Python Keywords and Identifiers
# Informatics Practices (065) - Class XI
# To display the keywords of Python and to check which of the given names are valid identifiers.

import keyword

print("Total keywords :", len(keyword.kwlist))
words = keyword.kwlist
for i in range(0, len(words), 12):
    print("  ", ", ".join(words[i:i + 12]))

names = ["student_name", "_marks", "class", "2total", "Roll-No"]
for name in names:
    if name in keyword.kwlist:
        print(name, "-> invalid : keyword")
    elif name[0].isdigit() or not name.isidentifier():
        print(name, "-> invalid : naming rule")
    else:
        print(name, "-> valid identifier")