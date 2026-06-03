import os
import random
from datetime import datetime

alphabet = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q",
            17:"R", 18:"S", 19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z"}

isAuthenticated = False
inputForED = ""
direction = ""
text = ""
numberOfShifts = 0
currentuser = None

def helperGetKey (value):
    for key, v in alphabet.items():
        if v == value:
            return key
    return None


def helper_clear_screen ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def encrypt_message (text, numberOfShifts, direction):
    encrypted_message = ""
    upper=True
    for char in text:
        if char != char.upper():
            upper=False
        char = char.upper()
        if char in alphabet.values():
            key = helperGetKey(char)
            if direction == "right":
                new_Key = (key + numberOfShifts) % 26
            else:
                new_Key = (key - numberOfShifts) % 26
            if upper:
                encrypted_message += alphabet[new_Key]
            else:
                encrypted_message += alphabet[new_Key].lower()
        else:
            encrypted_message += char
    return encrypted_message
            
def decrypt_all (text):
    for shifts in range (1, 26):
        decryptedText = ""
        for ch in text:
            if ch.upper() in alphabet.values():
                ePos = (helperGetKey(ch.upper()) - shifts) % 26
                cap = ""
                if ch.upper() == ch:
                    cap = "Upper"
                else:
                    cap = "Lower"
                if cap == "Upper":
                    decryptedText += alphabet[ePos].upper()
                else:
                    decryptedText += alphabet[ePos].lower()
            else:
                decryptedText += ch
        print(f"Decrypted text (C{shifts}): ",decryptedText)         
    
def encrypt_and_save_file ():
    if not os.path.exists ("Files"):
        os.makedirs ("Files")
    text = input ("Enter the message to encrypt and save: ")
    shift = random.randint(1, 25)
    direction = random.choice(["right", "left"])
    encrypted_message = encrypt_message(text, shift, direction)
    filename = input ("Enter the filename to save the encrypted message (Without including the extension): ")
    fullPath = os.path.join ("Files", filename+".txt")
    with open(fullPath, "w") as file:
        file.write(f"Shift: {shift}, Direction: {direction}\n")
        file.write(encrypted_message)
    print ("Message encrypted and saved to " + filename)
    return filename
    
    

def helper_print_header ():
    print ("====================================")
    print ("|                                  |")
    print ("|     Welcome to the Security      |")
    print ("|             System!              |")
    print ("|                                  |")
    print ("====================================")
    print ("|   1. Create an Account           |")
    print ("|   2. Login                       |")
    print ("|   3. Exit                        |")
    print ("====================================")


# def security_audit_log ():    


users = {}
auditLog = []

helper_clear_screen()
while isAuthenticated == False:
    
    helper_print_header()
    choice = input(" -> Enter your choice: ")
    if choice == "1":
        helper_clear_screen()
        print ("=" * 40)
        print ("           Create an Account")
        print ("=" * 40)
        
        print ("Enter your username: ", end="")
        username = input ()
        if username in users:
            print ("Username already exists! Try Again!")
        else:
            print ("Enter your password: ", end="")
            password = input ()
            users[username] = password
            print ("Account created successfully!")
            auditLog.append("Time: " + str(datetime.now()) + " - - - Account created for user: " + username)
        print ("Click 'Enter' to continue... ")
        input()
    elif choice == "2":
        helper_clear_screen()
        print ("=" * 40)
        print ("                  Login")
        print ("=" * 40)
        
        print ("Username: ", end="")
        username = input()
        print ("Password: ", end="")
        password = input()
        if username in users and users[username] == password:
            print ("Login successful! Welcome, " + username + "!")
            auditLog.append("Time: " + str(datetime.now()) + " - - - User logged in: " + username)
            isAuthenticated = True
        else:
            print ("Invalid username or password! Try Again!")
            auditLog.append("Time: " + str(datetime.now()) + " - - - Failed login attempt for username: " + username)
        
        while isAuthenticated:
            currentuser = username
            print ("=" * 40)
            print ("                  Menu")
            print ("=" * 40)
            print ("Welcome, " + currentuser + "!\n")
            print("1. Caesar Cipher - Encrypt Message")
            print("2. Caesar Cipher - Decrypt Message")
            print("3. Caesar Cipher - Brute Force Decrypt")
            print("4. Save Encrypted Message to File")
            print("5. Load and Decrypt File")
            print("6. View Security Audit Log")
            print("7. Logout")
            print("8. Exit")
            print ("=" * 40)
            print ("Enter a number to select an option: ", end="")
            option = input()
            
            if option == "1":
                helper_clear_screen()
                print ("You selected: Ceasar Cipher - Encrypt Message")
                text = input("Enter the message to encrypt: ")
                numberOfShifts = int(input("Enter the number of shifts: "))
                direction = input("Enter the direction (r/l): ")
                if direction.lower() == "r" or direction.lower() == "R":
                    direction = "right"
                elif direction.lower() == "l" or direction.lower() == "L":
                    direction = "left"
                else:
                    print ("Invalid direction! Defaulting to right.")
                    direction = "right"
                encrypted_message = encrypt_message(text, numberOfShifts, direction)
                print ("Encrypted Message: " + encrypted_message)
                auditLog.append("Time: " + str(datetime.now()) + " - - - Message encrypted: " + text)
                print ("Click 'Enter' to continue... ")
                input()
            elif option == "2":
                helper_clear_screen()
                print ("You selected: Ceasar Cipher - Decrypt Message")
                text = input("Enter the message to decrypt: ")
                numberOfShifts = int(input("Enter the number of shifts: "))
                direction = input("Enter the direction (r/l): ")
                if direction.lower() == "r" or direction.lower() == "R":
                    direction = "right"
                elif direction.lower() == "l" or direction.lower() == "L":
                    direction = "left"
                else:
                    print ("Invalid direction! Defaulting to Left.")
                    direction = "left"
                decrypted_message = encrypt_message(text, numberOfShifts, direction)
                print ("Decrypted Message: " + decrypted_message)
                auditLog.append("Time: " + str(datetime.now()) + " - - - Message decrypted: " + text)
                print ("Click 'Enter' to continue... ")
                input()
            elif option == "3":
                helper_clear_screen()
                text = input("Enter the message to brute force decrypt: ")
                decrypt_all(text)
                auditLog.append("Time: " + str(datetime.now()) + " - - - Message brute force decrypted: " + text)
                print ("Click 'Enter' to continue... ")
                input()
                
            elif option == "4":
                filename = encrypt_and_save_file()
                auditLog.append("Time: " + str(datetime.now()) + " - - - File encrypted and saved: " + filename + ".txt")
                print ("Click 'Enter' to continue... ")
                input()

            elif option == "5":
                helper_clear_screen ()
                print ("You selected: Load and Decrypt File")
                filename = input ("Enter the filename to load (Without including the extension): ")
                fullPath = os.path.join ("Files", filename+".txt")
                if os.path.exists(fullPath):
                    with open(fullPath, "r") as file:
                        first_line = file.readline().strip()
                        shift_info = first_line.split(", ")
                        shift = int(shift_info[0].split(": ")[1])
                        direction = shift_info[1].split(": ")[1]
                        encrypted_message = file.read().strip()
                        decrypted_message = encrypt_message(encrypted_message, shift, "left" if direction == "right" else "right")
                        print ("Decrypted Message: " + decrypted_message)
                        auditLog.append("Time: " + str(datetime.now()) + " - - - File loaded and decrypted: " + filename + ".txt")
                print ("Click 'Enter' to continue... ")
                input()
            
            elif option == "6":
                helper_clear_screen()
                print ("You selected: View Security Audit Log")
                for action in auditLog:
                    print (action)
                print ("Click 'Enter' to continue... ")
                input()
            
            elif option == "7":
                helper_clear_screen()
                print ("Logging out. Goodbye, " + currentuser + "!")
                auditLog.append("Time: " + str(datetime.now()) + " - - - User logged out: " + currentuser)
                isAuthenticated = False
                currentuser = None
                print ("Click 'Enter' to continue... ")
                input()
                
            elif option == "8":
                helper_clear_screen()
                print ("Exiting the system. Goodbye!")
                auditLog.append("Time: " + str(datetime.now()) + " - - - User exited the system: " + currentuser)
                break
            else:
                helper_clear_screen()
                print ("Invalid option! Please try again.")
                print ("Click 'Enter' to continue... ")
                input()
        
    elif choice == "3":
        helper_clear_screen()
        print ("Exiting the system. Goodbye!")
        break
    
    else:
        helper_clear_screen()
        print ("Invalid choice! Please try again.")