
from DataLoader import DataLoader
from ContactController import ContactController


class ContactView():
    
    def set_controller(self, controller): #Sets controller to take argument as an object
        self.controller = controller
        
    def display_menu(self): #Displays menu
        print("----------------------Contact App------------------------")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Exit")
        
    def get_option(self): # Gets menu option
        option = input("Enter menu option: ")
        print("")
        
        return option.strip()
    
    
    def get_contact_details(self): # Returns contact name, email, etc.
        name = input("Enter name: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        phone = input("Enter phone: ")
        
        return name, email, address, phone
    
    def display_contacts(self): # Displays all contacts
        dataLoader = DataLoader()
        self.contacts = dataLoader.load_contacts()
        for contact in self.contacts:
            print(contact)
    
    def run(self): # Runs the app
        
        while True:
            self.display_menu()
            option = self.get_option()
            
            if option == '1':
                name, email, address, phone = self.get_contact_details()
                self.controller.add_contact(name, email, address, phone)
            
            elif option == '2':
                name = input("Enter the contact name you would like to remove, to remove the contact: ")
                self.controller.remove_contact(name)
                
            elif option == '3':
                self.display_contacts()
                
            elif option == '4':
                break
            
            else:
                print("Invalid choice. Please select a correct menu option")
                
     
    