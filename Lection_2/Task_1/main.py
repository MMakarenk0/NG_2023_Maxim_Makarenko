# Input a sequence of elements
txt = input("Enter a sequence of elements separated by commas: ")

# Separation of elements by commas and writing in a list
elements = list(txt.split(", "))

# Input element to find and counting those items in the list
searchElem = input("Enter element to find it: ")
searchNum = elements.count(searchElem)

# Output number of 
if searchNum > 1:
    print(f"{searchNum} elements found")
elif searchNum == 1:
    print(f"{searchNum} element found")
else:
    print("No elements found")



