# Practical 15 : String Operations and Index Slicing
# Informatics Practices (065) - Class XI
# To perform the common operations on a string and to extract substrings using slicing.

text = "Informatics Practices"

print("Length  :", len(text))
print("First   :", text[0], "| Last :", text[-1])
print("Upper   :", text.upper())
print("Slice   :", text[0:11], "|", text[12:])
print("Reverse :", text[::-1])
print("Step 2  :", text[::2])
print("Count a :", text.count("a"))
print("Replace :", text.replace("Practices", "Skills"))
print("Split   :", text.split())