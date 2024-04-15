from Contact import Contact



class DataLoader():
    
    def save_contact(self, contacts): # Saves a contact after being added
        
        try:
            with open("contacts.txt", "a") as f:
                f.write(f"Name: {contacts.name}, Email: {contacts.email}, Address: {contacts.address}, Phone: {contacts.phone}\n")
        
        except IOError as e:
            print("An error occured.")
 
            
    def save_all(self, contacts): # saves all contacts for removal
        
        try:
            with open("contacts.txt", "w") as f:
                for contact in contacts:
                    f.write(f"Name: {contact.name}, Email: {contact.email}, Address: {contact.address}, Phone: {contact.phone}\n")
        
        except IOError as e:
           print("An error occured.") 
        
    def load_contacts(self): #Loads the contacts.txt file
        contacts = []
        
        try:
            with open("contacts.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",") #Splits the line by commas
                    name = parts[0][6:].strip() # Gets name, email, address, phone
                    email = parts[1][7:].strip()
                    address = parts[2][9:].strip()
                    phone = parts[3][7:].strip()
                    contact = Contact(name, email, address, phone)
                    contacts.append(contact)
                    
        except IOError as e:
            print("An error occured.")
            
        return contacts