class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    def addBook(self, book):
        self.books.append(book)  
        self.noBooks = len(self.books) 
    def showInfo(self):
        print(f" the library has {self.noBooks} books are {self.books} ")   


l1 = Library()

l1.addBook("harry poter")
l1.addBook("harry poter3")
l1.addBook("harry poter2")


l1.showInfo()
