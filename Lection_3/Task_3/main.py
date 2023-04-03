def info():
    print('Possible operations: "create", "delete", "show", "showList", "edit", "exit"')

def addNewBook(bookList):
    newBook = {}
    newBook["name"] = input("Enter new book's name: ")
    newBook["author"] = input("Enter new book's author: ")
    newBook["pagesNum"] = int(input("Enter new book's number of pages: "))
    newBook["genre"] = input("Enter new book's genre: ")
    newBook["cover"] = input("Enter new book's cover: ")
    bookList.append(newBook)   

def delBook(bookList):
    searchName = input("Enter name of book to delete it: ")
    try:
        del bookList[getIndex((searchName))]
    except:
        print("No books with this name!")


def getIndex(searchName): # Function that returns index with name
    for book in bookList:
        if bookList[bookList.index(book)]["name"]==searchName:
            return bookList.index(book)

def showBook(bookList):
    searchName = input("Enter name of book to find it: ")
    try:
        print(bookList[getIndex((searchName))])
    except: 
        print("No books with this name!")

def editBook(bookList):
    searchName = input("Enter name of book to edit it: ")
    key = input("Enter what do you want to edit: ")
    value = input("Enter the changes: ")
    try:
        bookList[getIndex((searchName))][key] = value
    except:
        print("No books with this name!")

bookList = list() # created list for dictionaries

info()

while True:
    nextStep = input("What is the next step?: ")
    match nextStep:
        case "create":
            # creating new dict for book
            addNewBook(bookList)
            #deleting book with name
        case "delete":
            delBook(bookList)
            # show dict with name
        case "show":
            showBook(bookList)
            # edit dict's value with name and key
        case "edit":
            editBook(bookList)    
            # show whole list
        case "showList":
            print(bookList)
            # breaks the loop
        case "exit":
            break
            # exeption 
        case _:
            print("Invalid operation!")