

import re

def menu(): #this function prints the menu
    
    print("Welcome to the Contact Management System!\n")
    print("Menu: \n")
    print("1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit\n")


def add_contact(contact_dict, name, contact_type, info): #this function adds contacts to the dictionary
    contact_dict[name] = {}
    contact_dict[name]["Phone number"] = "N/A"
    contact_dict[name]["Email"] = "N/A"
    contact_dict[name]["Additional info"] = "N/A"
    
    contact_dict[name][contact_type] = info

def edit_contact(contact_dict, name, contact_type, info): #this function allows you to edit the info
    
    contact_dict[name][contact_type] = info
    
def delete_contact(contact_dict, name): #this function deletes the contact
    del contact_dict[name]
    
def display_all(contact_dict): #this function prints all the contacts
    
    print(contact_dict)
    
def search(contact_dict, name): #this function searches for the contact
    
    exist = check_key(contact_dict, name)
    
    if (exist):
        print(contact_dict[name])
    else:
        print("This contact does not exist")
        
def export(contact_dict, filename): #this function exports the contacts into a file
    
    file = open(filename, "w")
    for name, info in contact_dict.items():
        file.write(name)
        file.write("\n")
        file.write("Phone number")
        file.write("\n")
        num = contact_dict[name]["Phone number"]
        file.write(num)
        file.write("\n")
        
        file.write("Email")
        file.write("\n")
        email = contact_dict[name]["Email"]
        file.write(email)
        file.write("\n")
        
        file.write("Additional info")
        file.write("\n")
        add = contact_dict[name]["Additional info"]
        file.write(add)
        file.write("\n")
        
        file.write("-----------------")
        file.write("\n")
        
    file.close()
    
def import_contact(contact_dict, filename): #this function imports contacts into the dictionary
    
    file = open(filename, "r")
    
    for line in file:
        name, num, email, info = line.strip().split(':')
        
        contact_dict[name] = {}
        contact_dict[name]["Phone number"] = num
        contact_dict[name]["Email"] = email
        contact_dict[name]["Additional info"] = info
        
    file.close()

    
def check_key(contact_dict, key): #this function checks if the task exists in the todo list
    if key in contact_dict: 
        return True
        
    else: 
        return False
    
def check_label(contact_type): #this function checks with the type is valid
    
    if (contact_type == "Phone number" or contact_type == "Email" or contact_type == "Additional info"):
        
        return True
    else:
        
        return False

def check_email(info): #this function checks the email format
    
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", info)
    return emails
    
    
def valid_input(): #this function makes sure the user enters a valid input
    while True:
        try:
            user_input = int(input("\nWhich task do you want to do? "))
            if user_input not in range(1, 9):
                raise ValueError
            return user_input
        except ValueError:
            print("Please enter a valid number between 1 and 8")
            
        finally: 
            print("----------------------------------------------")

contact_dict = {}
menu()
user_input = valid_input()

while (user_input != 8): #loops until user wants to quit
    if (user_input == 1):
        
        name = input("Enter the name of the contact you wish to add: ")
        exist = check_key(contact_dict, name)
        
        if exist:
            print("This contact already exist")
        else:
            type = input("What type of contact are you adding (Phone number, Email, Additional info)? ")
            
            label = check_label(type)
            if label:    
                info = input("Enter in their contact: ")
                if type == "Email":
                    email = check_email(info)
                    if email != []:
                        add_contact(contact_dict, name, type, email)
                    else:
                        print("Incorrect email format")
                else:
                    add_contact(contact_dict, name, type, info)
            else:
                print("Please choose only the following contact type (same spelling): Phone number, Email, Additional info")
                
    elif (user_input == 2):
        name = input("Enter the name of the contact you wish to edit: ")
        
        exist = check_key(contact_dict, name)
        
        if exist:
            type = input("What type of contact are you editing (Phone number, Email, Addition info)? ")
            
            label = check_label(type)
            if label:    
                info = input("Enter in their contact: ")
                if type == "Email":
                    email = check_email(info)
                    if email != []:    
                        edit_contact(contact_dict, name, type, email)
                    else:
                        print("Incorrect email format")
                else:
                    edit_contact(contact_dict, name, type, info)
            else:
                print("Please choose only the following contact type (same spelling): Phone number, Email, Additional info")
                
        else:
            print("This contact does not exist")
    
    elif (user_input == 3):
        name = input("Enter the name of the contact you wish to delete: ")
        
        exist = check_key(contact_dict, name)
        
        if exist:
            delete_contact(contact_dict, name)
        else:
            print("This contact does not exist")
        
    
    elif (user_input == 4):
        name = input("Enter the name of the contact you wish to find: ")
        search(contact_dict, name)
    
    elif (user_input == 5):
        
        display_all(contact_dict)
        
    elif (user_input == 6):
        filename = input("What filename do you want to export your contacts to: ")
        export(contact_dict, filename)
        
    elif (user_input == 7):
        filename = input("What filename do you want to import your contacts from: ")
        import_contact(contact_dict, filename)
        
    menu()
    user_input = valid_input()   
    
    