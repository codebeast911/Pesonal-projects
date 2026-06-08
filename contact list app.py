import json
import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.contacts = {}
        self.root = root
        self.root.title("Contact Book")
        
        self.load_contacts()
      
        # UI Elements
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1)
        
        
        self.label_phone = tk.Label(root, text="Phone:")
        self.label_phone.grid(row=1, column=0)
        self.entry_phone = tk.Entry(root)
        self.entry_phone.grid(row=1, column=1)
        
        self.label_address = tk.Label(root, text="Address:")
        self.label_address.grid(row=2, column=0)
        self.entry_address = tk.Entry(root)
        self.entry_address.grid(row=2, column=1)
        
        self.label_email = tk.Label(root, text="Email:")
        self.label_email.grid(row=3, column=0)
        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=3, column=1)
                
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=5, column=0, columnspan=2)
        
        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=6, column=0)
        self.entry_search = tk.Entry(root)
        self.entry_search.grid(row=6, column=1)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2)
        
        self.display_button = tk.Button(root, text="Display Contacts", command=self.display_contacts)
        self.display_button.grid(row=8, column=0, columnspan=2)
        
        self.save_button = tk.Button(root, text="Save Contacts", command=self.save_contacts)
        self.save_button.grid(row=9, column=0, columnspan=2)
    
    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()
        email = self.entry_email.get()
        social_media = self.entry_social_media.get()
        
        if name:
            self.contacts[name] = {
                "Phone": phone,
                "Address": address,
                "Email": email,
                "Social Media": social_media
            }
            messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
        else:
            messagebox.showwarning("Warning", "Name cannot be empty!")
    
    def display_contacts(self):
        contacts_str = "\n".join([f"{name}: {details}" for name, details in self.contacts.items()])
        messagebox.showinfo("Contacts", contacts_str if contacts_str else "No contacts found.")
    
    def search_contact(self):
        keyword = self.entry_search.get()
        found_contacts = [f"{name}: {details}" for name, details in self.contacts.items() if keyword.lower() in name.lower() or any(keyword.lower() in str(v).lower() for v in details.values())]
        messagebox.showinfo("Search Results", "\n".join(found_contacts) if found_contacts else "No matching contacts found.")
    
    def save_contacts(self, filename="contacts.json"):
        with open(filename, "w") as file:
            json.dump(self.contacts, file, indent=4)
        messagebox.showinfo("Success", "Contacts saved successfully.")
    
    def load_contacts(self, filename="contacts.json"):
        try:
            with open(filename, "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = {}

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
