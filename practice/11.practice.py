class Book:
    def __init__(self, title, author, pages, read):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = read
    
    def mark_as_read(self):
        self.read = True
    
    def get_info(self):
        status = "Already read!" if self.read else "Not read yet"
        return f"{self.title} by {self.author} ({self.pages} pages) - {status}"

# Create book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180, False)
book2 = Book("Python Basics", "Guido van Rossum", 250, False)

# Test without reading
print("Before marking as read:")
print(book1.get_info())
print(book2.get_info())

# Mark book1 as read
book1.mark_as_read()

# Test after reading
print("\nAfter marking book1 as read:")
print(book1.get_info())
print(book2.get_info())
