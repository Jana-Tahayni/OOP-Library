class User: 
    def __init__(self, UserID, Name, Email):
        self.UserID = UserID
        self.Name = Name
        self.Email = Email
        self.barrowedItems = []
    
    def display_info (self):
        print (f"ID: {self.UserID} Name: {self.Name} Email: {self.Email}")
        