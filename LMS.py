books = []

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }

    books.append(book)
    print("Book added successfully!")

def display_books():
    if not books:
        print("No books in the library.")
    else:
        print("Available books:")
        for book in books:
            if book["available"]:
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("ISBN:", book["isbn"])
                print("--------------------")

def search_book():
    title = input("Enter the title of the book you want to search: ")
    found_books = []
    for book in books:
        if book["title"] == title:
            found_books.append(book)

    if found_books:
        print("Book(s) found:")
        for book in found_books:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("ISBN:", book["isbn"])
            print("--------------------")
    else:
        print("Book not found.")

# Main program loop
while True:
    print("Library Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Library Management System!")
