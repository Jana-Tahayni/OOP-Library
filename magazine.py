# Magazine class is a subclass for parentclass LibraryItem class 
from models.libraryitem import LibraryItem

class Magazine (LibraryItem):
    def __init__(self, ItemID, Title, Author, Year, Company):
        super().__init__(ItemID, Title, Author)
        self.Year = Year
        self.Company = Company

    # Magazine class must impplement all abstarct methods at LibraryItem class
    def check_availability(self):
        return self.is_available
    
    def display_info(self):
        print (f"[Magazine] {self.ItemID} {self.Title} by {self.Author} through {self.Company} at {self.Year}")

