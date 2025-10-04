# DVD class will implement Resarvable interface and will extend LibraryItem class
from models.libraryitem import LibraryItem, Reservable

class DVD (LibraryItem, Reservable):
    # constructor
    def __init__(self, ItemID, Title, Author, Duration, Year):
        super().__init__(ItemID, Title, Author)
        self.Duration = Duration
        self.Year = Year

    # DVD class must implement all abstarct methods at LibraryItem class and the method at Reservable interface 
    def display_info(self):
        print (f"[DVD] {self.ItemID} {self.Title} by {self.Author} DVD year: {self.Year} DVD time duration: {self.Duration} minutes")

    def check_availability(self):
        return self.is_available
    
    def reserve(self, UserID):
        if self.is_reserved:
            raise Exception("DVD is already reserved!")
        self.is_reserved = True