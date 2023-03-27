# get user's lists and split them
wholeList = input("Enter first list: ").split(", ")+input("Enter second list: ").split(", ")+input("Enter first list: ").split(", ")
for elem in set(wholeList):  # loop for getting unique elements to check their number
    if (wholeList).count(elem)>1:
        print(elem, end = ", ")

