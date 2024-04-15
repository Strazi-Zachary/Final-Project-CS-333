from Contact import Contact
from ContactView import ContactView
from ContactController import ContactController
from DataLoader import DataLoader
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import os


class Test(unittest.TestCase):
    
    def setUp(self):
        self.dataLoader = DataLoader()
        self.model = Contact("", "", "", "")
        self.view = ContactView()
        self.controller = ContactController(self.model, self.view)
        self.view.set_controller(self.controller)
        
    def test_add_contact(self):
        self.controller.add_contact("Zack", "zack@test.com", "123 This St", "444-4444")
        self.assertEqual(len(self.controller.contacts), 1)
        
    def test_remove_contact(self):
        self.controller.remove_contact("Zack")
        self.assertEqual(len(self.controller.contacts), 0)
        
        removed = self.controller.remove_contact("Zack")
        self.assertFalse(removed)
        
        
    def test_get_option(self):
        input_Mock = MagicMock(return_value=1)
        self.view.get_option = input_Mock
        self.assertEqual(self.view.get_option(), 1)
        

    @patch('builtins.input', side_effect=["Zack", "zack@test.com", "123 This St", "444-4444"])
    def test_get_contact_details(self, mock_input):
        view = ContactView()
        name, email, address, phone = view.get_contact_details()

        self.assertEqual(name, 'Zack')
        self.assertEqual(email, 'zack@test.com')
        self.assertEqual(address, '123 This St')
        self.assertEqual(phone, '444-4444')
        
    def test_integration_1(self): #Tests between adding and removing a contact from the file
        self.controller.add_contact("Zack", "zack@test.com", "123 This St", "444-4444")
        self.controller.remove_contact("Zack")
        self.assertEqual(len(self.controller.contacts), 1)
        
    def test_integration_2(self): #Tests between adding and loading a contact an making sure it is in the created file
        self.controller.add_contact("Zack", "zack@test.com", "123 This St", "444-4444")
        contacts = self.dataLoader.load_contacts()
        added_contact = ("Zack", "zack@test.com", "123 This St", "444-4444")
        self.assertIn(added_contact, [(contact.name, contact.email, contact.address, contact.phone) for contact in contacts])
        self.controller.remove_contact("Zack")
    
    def test_integration_3(self): #Tests that a file is created when a contact is added
        self.controller.add_contact("Zack", "zack@test.com", "123 This St", "444-4444")
        file = "contacts.txt"
        self.assertTrue(os.path.exists(file))
        self.controller.remove_contact("Zack")
        
    def test_integration_4(self): #Tests between the model, loader, and display interactions
        self.dataLoader.load_contacts = MagicMock(return_value=[
        Contact("Zack", "zack@test.com", "123 This St", "444-4444"),
        Contact("Cherie", "cherie@test.com", "456 That St", "444-1255")])
        self.view.display_contacts()
        self.assertTrue(self.view.contacts)
      
    @patch('builtins.input', side_effect=["Zack", "zack@test.com", "123 This St", "444-4444"]) 
    def test_integration_5(self, mock_input):
        
        self.view.run()
        self.assertEqual(len(self.controller.contacts), 1)
        added_contact = self.controller.contacts[0]
        self.assertEqual(added_contact.name, 'Zack')
        self.assertEqual(added_contact.email, 'zack@test.com')
        self.assertEqual(added_contact.address, '123 Main St')
        self.assertEqual(added_contact.phone, '444-4444')
        
        
if __name__ == '__main__':
  unittest.main()