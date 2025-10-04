# class Book will implement Reservable interface, and will extend LibraryItem class. [Book is subclass]
from models.libraryitem import LibraryItem, Reservable

class Book (LibraryItem, Reservable): 
    # constructor
    def __init__(self, ItemID, Title, Author, PageNum, Generation):
        super().__init__(ItemID, Title, Author)
        self.PageNum = PageNum
        self.Generation = Generation

# Book class must implement all abstract methods in LibraryItem class, and the methode at Reservable interface
    def display_info(self):
        print (f"[Book] {self.ItemID} {self.Title} by {self.Author} Generation: {self.Generation} Number of pages: {self.PageNum}")

    def check_availability(self):
        return self.is_available
    
    def reserve(self, UserID):
        if self.is_reserved: 
            raise Exception("Book is already reserved!")
        self.is_reserved = True
    
