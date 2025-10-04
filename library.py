from models.book import Book
from models.dvd import DVD
from models.magazine import Magazine
from models.user import User
from models.libraryitem import Reservable
from exceptions.itemNotAvailableError import ItemNotAvailableError
from exceptions.itemNotFoundError import ItemNotFoundError
from exceptions.userNotFoundError import UserNotFoundError


class Library:
    def __init__(self):
        self.items = []
        self.users = []
# Method to load all data from files
    def Load (self):
        try:
            with open("items.txt", "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    item_type = parts[0]
                    item_id = parts[1]
                    title = parts[2]
                    author = parts[3]
                    available = parts[-2] == 'True'  # negative indexing to count from the end 
                    reserved = parts[-1] == 'True'   # in the file, True or False are strings, not booleans. so we compare them this way to store the boolean value

                    if item_type == "Book":
                        page_num = int(parts[4])
                        generation = parts[5]
                        item = Book(item_id, title, author, page_num, generation)
                    elif item_type == "DVD":
                        duration = int(parts[4])
                        year = int(parts[5])
                        item = DVD(item_id, title, author, duration, year)
                    elif item_type == "Magazine":
                        year = int(parts[4])
                        company = parts[5]
                        item = Magazine(item_id, title, author, year, company)
                    else:
                        continue

                    item.is_available = available
                    item.is_reserved = reserved
                    self.items.append(item)

            with open("users.txt", "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    user_id = parts[0]
                    name = parts[1]
                    email = parts[2]
                    borrowed = parts[3].split(",") if parts[3] else []  # split if not empty
                    user = User(user_id, name, email)
                    user.barrowedItems = borrowed
                    self.users.append(user)

        except Exception as e:
            print(f"Error loading data: {e}")

# Method to store all data in the files
    def Store (self):
        try:
            with open("items.txt", "w") as f:
                for item in self.items:
                    base = f"{item.__class__.__name__}|{item.ItemID}|{item.Title}|{item.Author}"
                    if isinstance(item, Book):
                        extra = f"{item.PageNum}|{item.Generation}"
                    elif isinstance(item, DVD):
                        extra = f"{item.Duration}|{item.Year}"
                    elif isinstance(item, Magazine):
                        extra = f"{item.Year}|{item.Company}"
                    else:
                        continue
                    line = f"{base}|{extra}|{item.is_available}|{item.is_reserved}\n"
                    f.write(line)

            with open("users.txt", "w") as f:
                for user in self.users:
                    borrowed = ",".join(user.barrowedItems)
                    line = f"{user.UserID}|{user.Name}|{user.Email}|{borrowed}\n"
                    f.write(line)

        except Exception as e:
            print(f"Error saving data: {e}")

    def AddUser(self, name, email):
        user_id = str(len(self.users) + 1)
        new_user = User(user_id, name, email)
        self.users.append(new_user)
        return new_user
    
    def RemoveUser(self, user_id):
        for i, user in enumerate(self.users):
            if user.UserID == user_id:
                del self.users[i]
                return
        raise UserNotFoundError("User not found!")
    
    def AddItem(self, item_type, item_id, title, author, *args):
        if item_type == "Book":
            if len(args) != 2:
                raise Exception("Book requires page_num and generation")
            item = Book(item_id, title, author, int(args[0]), args[1])
        elif item_type == "DVD":
            if len(args) != 2:
                raise Exception("DVD requires duration and year")
            item = DVD(item_id, title, author, int(args[0]), int(args[1]))
        elif item_type == "Magazine":
            if len(args) != 2:
                raise Exception("Magazine requires year and company")
            item = Magazine(item_id, title, author, int(args[0]), args[1])
        else:
            raise Exception("Unsupported item type")

        self.items.append(item)

    def RemoveItem(self, item_id):
        for i, item in enumerate(self.items):
            if item.ItemID == item_id:
                del self.items[i]
                return
        raise ItemNotFoundError("Item not found!")


    def FindItem(self, item_id):
        for item in self.items:
            if item.ItemID == item_id:
                return item
        raise ItemNotFoundError("Item not found!")
    
    def FindUser(self, user_id):
        for user in self.users:
            if user.UserID == user_id:
                return user
        raise UserNotFoundError("User not found!")

    def BorrowItem(self, user_id, item_id):
        user = self.FindUser(user_id)
        item = self.FindItem(item_id)
        if not item.check_availability():
            raise ItemNotAvailableError("Item not available")
        item.is_available = False
        user.barrowedItems.append(item_id)

    def ReturnItem(self, user_id, item_id):
        user = self.FindUser(user_id)
        item = self.FindItem(item_id)
        item.is_available = True
        if item_id in user.barrowedItems:
            user.barrowedItems.remove(item_id)

    def ReserveItem(self, user_id, item_id):
        item = self.FindItem(item_id)
        if isinstance(item, Reservable):
            item.reserve(user_id)
        else:
            raise Exception("Item cannot be reserved")

        
   