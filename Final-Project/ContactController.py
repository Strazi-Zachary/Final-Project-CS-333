from Contact import Contact
from DataLoader import DataLoader


class ContactController():
    
    def __init__(self, model, view): #Constructor
        self.model = model
        self.view = view
        self.contacts = []
        
    def add_contact(self, name, email, address, phone): #Adds contact to contacts.txt
        contact = Contact(name, email, address, phone)
        self.contacts.append(contact) #Adds contact to list
        dataLoader = DataLoader()
        dataLoader.save_contact(contact) #Saves contact
        print("Contact added successfully. \n")
        
    def remove_contact(self, name): #Removes contact from contacts.txt
        removed = False
        dataLoader = DataLoader()
        self.contacts = dataLoader.load_contacts()
        
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                removed = True
                break
            
        if removed:
            dataLoader.save_all(self.contacts)
            print("Contact removed successfully. \n")
        else:
            print("Contact not found. \n")
                
        return removed