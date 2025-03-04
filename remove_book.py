def remove_book(books):
    isbn = input("enter the ISBN of the book to remove: ")
    for book in books:
        if book["isbn"] == isbn:
            books.remove(book)
            print("Book removed Successfully.")
            return books
    print("Error: Book not found!")
    return books    