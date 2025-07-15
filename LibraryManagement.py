class Library:
    def __init__(self,):
        self.noBooks=0
        self.books=[]
    
    def addBook(self, book):
        self.books.append(book)
        self.noBooks += 1

    def showInfo(self):
        print(f"The Library has {self.noBooks} books. List of books available: {', '.join(self.books)}")

l1=Library()
l1.addBook("The Great Gatsby")
l1.addBook("1984")
l1.addBook("To Kill a Mockingbird")
l1.showInfo()