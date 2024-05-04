from Contact import Contact
from DataLoader import DataLoader
from ContactView import ContactView
from ContactController import ContactController

#Demo
def Main():
    
    model = Contact("", "", "", "")
    view = ContactView()
    controller = ContactController(model, view)
    view.set_controller(controller)
    view.run()
    
if __name__ == "__main__":
    Main()