'''Write a Python program for department library which has N books, write functions for 
following: 
a) Delete the duplicate entries 
b) Display books in ascending order based on cost of books 
c) Count number of books with cost more than 500.  
d) Copy books in a new list which has cost less than 500. '''

class Book:
    def __init__(self, title, cost):
        self.title = title
        self.cost = cost

    def __repr__(self):
        return f"Book(title='{self.title}', cost={self.cost})"

# Function to delete duplicate entries from the list of books
def delete_duplicates(books):
    unique_books = []
    seen_titles = set()
    for book in books:
        if book.title not in seen_titles:
            unique_books.append(book)
            seen_titles.add(book.title)
    return unique_books

# Function to display books in ascending order based on cost
def display_books_ascending(books):
    sorted_books = sorted(books, key=lambda book: book.cost)
    for book in sorted_books:
        print(book)

# Function to count number of books with cost more than 500
def count_books_above_500(books):
    count = sum(1 for book in books if book.cost > 500)
    book_title=[book.title for book in books if book.cost > 500]

    return count,book_title

# Function to copy books with cost less than 500 to a new list
def copy_books_below_500(books):
    below_500_books = [book for book in books if book.cost < 500]
    return below_500_books

# Function to get book details from the user
def get_books():
    books = []
    number_of_books = int(input("Enter the number of books: "))
    for i in range(number_of_books):
        print(f"\nEnter details for book {i + 1}:")
        title = input("Enter book title: ")
        pages = int(input("Enter cost of books : "))
        books.append(Book(title, pages))
    return books

books = get_books()

# Removing duplicate books
books = delete_duplicates(books)
print("Books after removing duplicates:")



# Displaying books in ascending order based on cost
print("\nBooks in ascending order based on cost:")
display_books_ascending(books)

# Counting books with cost more than 500
count = count_books_above_500(books)
print(f"\nNumber of books with cost more than 500: {count}")


# Copying books with cost less than 500 to a new list
below_500_books = copy_books_below_500(books)
print(f"\nBooks with cost less than 500: ")
for book in below_500_books:
    print(book)






