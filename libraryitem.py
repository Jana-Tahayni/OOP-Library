from abc import ABC, abstractmethod


class LibraryItem (ABC):   # Since LibraryItem class is an abstract class, it extends ABC 
    # constructor
    def __init__(self, ItemID, Title, Author):
        self.ItemID = ItemID
        self.Title = Title
        self.Author = Author
        self.is_available = True
        self.is_reserved = False


    # Abstarct Methods
    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def check_availability(self):
        pass


# inferface (full abstract class) with name Reservable
class Reservable (ABC): 
    # reserve method 
    def reserve(self, UserID):
        pass
