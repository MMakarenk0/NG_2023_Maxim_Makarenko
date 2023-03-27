def getIndex(searchName): # Function that returns index with name
    i = 0
    while i < len(bookList):
        if bookList[i]["name"]==searchName:
            return i
        i+=1
    print("No books with this name!")

bookList = list() # created list for dictionaries

print('Possible operations: "create", "delete", "show", "showList", "edit", "exit"')
while True:
    nextStep = input("What is the next step?: ")
    match nextStep:
        case "create":
            # creating new dict for book
            newDict = {}
            newDict["name"] = input("Enter new book's name: ")
            newDict["author"] = input("Enter new book's author: ")
            newDict["pagesNum"] = int(input("Enter new book's number of pages: "))
            newDict["genre"] = input("Enter new book's genre: ")
            newDict["cover"] = input("Enter new book's cover: ")
            bookList.append(newDict)
            #deleting book with name
        case "delete":
            searchName = input("Enter name of book to delete it: ")
            
            del bookList[getIndex((searchName))]
            # show dict with name
        case "show":
            searchName = input("Enter name of book to find it: ")
            print(bookList[getIndex((searchName))])
            # edit dict's value with name and key
        case "edit":
            searchName = input("Enter name of book to edit it: ")
            key = input("Enter what do you want to edit: ")
            value = input("Enter the changes: ")
            bookList[getIndex((searchName))][key] = value
            # show whole list
        case "showList":
            print(bookList)
            # breaks the loop
        case "exit":
            break
            # exeption 
        case _:
            print("Invalid operation!")


        

