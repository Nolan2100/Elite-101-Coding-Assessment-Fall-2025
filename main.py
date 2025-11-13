from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# A function to view all books that are currently available
# Output should include book ID, title, and author
def view_available_books():
    for book in library_books:
        if book['available'] == True:
            print(f"Book ID: {book['id']}, Book Title: {book['title']}, Book Author: {book['author']}")

# -------- Level 2 --------
# A function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books():
    search = input("Enter author or genre to search: ").lower()
    for book in library_books:
        if search in book['author'].lower() or search in book['genre'].lower():
            print(book)

# -------- Level 3 --------
# A function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def checkout():
    book_id = input("Enter the book ID to checkout: ").strip()
    if not book_id:
        print("Book ID cannot be empty.")
        return
    for book in library_books:
        if book['id'] == book_id:
            if book['available']:
                book['available'] = False
                book['due_date'] = (datetime.now() + timedelta(weeks=2)).strftime("%m-%d-%y")#used ai to understand the datetime format
                book['checkouts'] += 1
                print(f"Book '{book['title']}' checked out successfully. Due date: {book['due_date']}")
            else:
                print(f"Book '{book['title']}' is already checked out. Due date: {book['due_date']}")
            return
    print("Book ID not found.")

# -------- Level 4 --------
# A function to return a book by ID
# Set its availability to True and clear the due_date
def return_book():
    book_id = input("Enter the book ID to return: ").strip()
    if not book_id:
        print("Book ID cannot be empty.")
        return
    for book in library_books:
        if book['id'] == book_id:
            if not book['available']:
                book['available'] = True
                book['due_date'] = None
                print(f"Book '{book['title']}' returned successfully.")
            else:
                print(f"Book '{book['title']}' was not checked out.")
            return
    print("Book ID not found.")

# A function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def list_overdue_books():
    today = datetime.now().date()
    for book in library_books:
        if not book['available'] and book['due_date']:
            due_date = datetime.strptime(book['due_date'], "%Y-%m-%d").date()#used ai to understand the datetime format
            if due_date < today and book['available'] == False:
                print(f"Overdue Book ID: {book['id']}, Title: {book['title']}, Due Date: {book['due_date']}")

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.
def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View Available Books")
        print("2. Search Books by Author or Genre")
        print("3. Checkout a Book")
        print("4. Return a Book")
        print("5. List Overdue Books")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            view_available_books()
        elif choice == '2':
            search_books()
        elif choice == '3':
            checkout()
        elif choice == '4':
            return_book()
        elif choice == '5':
            list_overdue_books()
        elif choice == '6':
            print("Thanks for using the library system, Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()