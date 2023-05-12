'''This script creates a SQLite database called 'bookstore.db', and defines several functions to manipulate the data in the database.
The database stores information about books such as their title, author, publisher, price, and quantity.
The functions defined include adding a new book to the database, updating the price of a book, deleting a book from the database, searching for a book in the database, and viewing all books in the database.'''

import sqlite3

# Connect to the database
db = sqlite3.connect('bookstore.db')
cursor = db.cursor()

# Create a table for storing book information
cursor.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY,
              title TEXT,
              author TEXT,
              publisher TEXT,
              price FLOAT,
              quantity INTEGER)''')

# Define a function to add a new book to the database
def add_books():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    publisher = input("Enter publisher name: ")
    price = float(input("Enter book price: R "))
    quantity = int(input("Enter book quantity: "))
    cursor.execute('''INSERT INTO books (title, author, publisher, price, quantity) 
                      VALUES (?, ?, ?, ?, ?)''', (title, author, publisher, price, quantity))
    db.commit()
    print("book succesfully added to the database.")


# Define a function to update the price of a book
def update_book_price():
    title = input("Enter the title of the book you want to update: ").lower()
    new_price = float(input("Enter the new price for the book: R "))
    cursor.execute('''UPDATE books SET price = ? WHERE lower(title) = ?''', (new_price, title))
    db.commit()
    print("Book updated successfully.")

# Define a function to delete a book from the database
def delete_book():
    title = input("Enter the title of the book you want to delete: ").lower()
    cursor.execute('''DELETE FROM books WHERE LOWER(title) = ?''', (title,))
    db.commit()
    print("book deleted successfully.")

# Define a function to search for a book in the database
def search_books():
    #Prompt the user to enter the title of the book they want to search for, and convert it to lowercase
    title = input("Enter the title of the book you want to search for: ").lower()
    # Execute a SQL query to retrieve all books with titles that match the lowercase version of the user's input
    cursor.execute('''SELECT * FROM books WHERE lower(title) = ?''', (title,))
    #Fetch the first result of the query
    book = cursor.fetchone()
    #If a matching book was found, print its details
    if book:
        print(f"Book found: Title: {book[1]}, Author: {book[2]}, Publisher: {book[3]}, Price: {book[4]}")
    #If no matching book was found, inform the user
    else:
        print(f"No book found with title '{title}'.")

#create a function tht views all the books
def view_all():
    cursor.execute('''SELECT * FROM books''')
    books = cursor.fetchall()
    if books:
        for book in books:
            print(f"Title: {book[1]}, Author: {book[2]}, Publisher: {book[3]}, Price: {book[4]}")
    else:
        print("No books found in the database.")    

# Prompt the user for input and perform the requested operation
while True:
    print("Welcome to the bookstore database!")
    print("Please select an option below by entering a number?")
    print("1. Add a new book")
    print("2. Update book information")
    print("3. Delete a book")
    print("4. Search for a book")
    print("5. View All")
    print("6.Quit")

    choice = input("ENTER INPUT: ")
    #Prompt the user to add a new book
    if choice == "1":
        add_books()

    # Prompt the user to update the price of a book
    elif choice == "2":
        update_book_price()

    #Prompt the user to delete a book from the database
    elif choice == "3":
        delete_book()

    # Prompt the user to search for a book in the database
    elif choice == "4":
        search_books()
        
    #Prompt the user to view all the books
    elif choice == "5":
        print("View all")
        view_all()
        
    # Quit the program
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue

# Close the database connection
db.close()
