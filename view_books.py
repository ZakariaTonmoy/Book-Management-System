def view_books(books):
    if not books:
        print("No book available.")
        return
    
    print("\n---List of Books---")
    for book in books:
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"ISBN: {book['isbn']}")
        print(f"Genre: {book['genre']}")
        print(f"Price: ${book['price']:.2f}")
        print(f"Quantity: {book['quantity']}")
        print("-" * 30)




