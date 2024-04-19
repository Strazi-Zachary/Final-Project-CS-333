

class Contact():
    
    def __init__(self, name, email, address, phone):
        self.name = name 
        self.email = email 
        self.address = address 
        self.phone = phone 
        
    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nPhone: {self.phone}\n"
