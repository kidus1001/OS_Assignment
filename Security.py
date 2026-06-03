import os
import random
from datetime import datetime
import hashlib
import getpass

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
    for ch in text:
        if ch.upper() in alphabet.values():
            if direction == "right":
                ePos = (helperGetKey(ch.upper()) + numberOfShifts) % 26
            else:
                ePos = (helperGetKey(ch.upper()) - numberOfShifts) % 26
            cap = ""
            if ch.upper() == ch:
                cap = "Upper"
            else:                
                cap = "Lower"
            if cap == "Upper":
                encrypted_message += alphabet[ePos].upper()
            else:
                encrypted_message += alphabet[ePos].lower()
        else:
            encrypted_message += ch
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
    print ("\n")
    print ("=" * 40)
    print ("Message encrypted and saved to " + filename)
    print ("=" * 40)
    return filename
    
    

def helper_print_header ():
    helper_clear_screen()
    print ("\n\n====================================")
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
            helper_clear_screen()
            print ("\n")
            print ("=" * 40)
            print ("Username already exists! Try Again!")
            print ("=" * 40)
        else:
            password = getpass.getpass("Enter your password: ")
            confirmPassword = getpass.getpass("Confirm your password: ")
            if password != confirmPassword:
                print ("\n")
                print ("=" * 40)
                print ("Passwords do not match! Try Again!")
                print ("=" * 40)
                print ("Click 'Enter' to continue... ")
                input()
                continue
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            users[username] = password_hash
            helper_clear_screen()
            print ("\n")
            print ("=" * 40)
            print ("Account created successfully!")
            print ("=" * 40)
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
        password = getpass.getpass("Password: ")
        if username in users and users[username] == hashlib.sha256(password.encode()).hexdigest():
            helper_clear_screen()   
            print ("\n")
            print ("=" * 40)
            print ("Login successful! Welcome, " + username + "!")
            print ("=" * 40)
            auditLog.append("Time: " + str(datetime.now()) + " - - - User logged in: " + username)
            isAuthenticated = True
        else:
            helper_clear_screen()
            print ("\n")
            print ("=" * 40)    
            print ("Invalid username or password! Try Again!")
            print ("=" * 40)
            auditLog.append("Time: " + str(datetime.now()) + " - - - Failed login attempt for username: " + username)
        
        while isAuthenticated:
            currentuser = username
            helper_clear_screen()
            print ("=" * 40)
            print ("                  Menu")
            print ("=" * 40)
            print ("\n👤 Welcome, " + currentuser + "!\n")
            print("1. Caesar Cipher - Encrypt Message")
            print("2. Caesar Cipher - Decrypt Message")
            print("3. Caesar Cipher - Brute Force Decrypt")
            print("4. Save Encrypted Message to File")
            print("5. Load and Decrypt File")
            print("6. View Security Audit Log")
            print("7. Settings")
            print("8. Exit")
            print ("=" * 40)
            print ("Enter a number to select an option: ", end="")
            option = input()
            
            if option == "1":
                helper_clear_screen()
                print ("\nYou selected: Ceasar Cipher - Encrypt Message")
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
                helper_clear_screen()
                print ("=" * 40)
                print ("Encrypted Message: " + encrypted_message)
                print ("=" * 40)
                auditLog.append("Time: " + str(datetime.now()) + " - - - Message encrypted: " + text)
                print ("Click 'Enter' to continue... ")
                input()
            elif option == "2":
                helper_clear_screen()
                print ("\nYou selected: Ceasar Cipher - Decrypt Message")
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
                helper_clear_screen()
                print ("=" * 40)
                print ("Decrypted Message: " + decrypted_message)
                print ("=" * 40)
                auditLog.append("Time: " + str(datetime.now()) + " - - - Message decrypted: " + text)
                print ("Click 'Enter' to continue... ")
                input()
            elif option == "3":
                helper_clear_screen()
                text = input("Enter the message to brute force decrypt: ")
                print("\n")
                print ("=" * 40)
                print("Brute Force Decryption Results: \n")
                decrypt_all(text)
                print ("=" * 40)
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
                filename = input ("\nEnter the filename to load (Without including the extension): ")
                fullPath = os.path.join ("Files", filename+".txt")
                if os.path.exists(fullPath):
                    with open(fullPath, "r") as file:
                        first_line = file.readline().strip()
                        shift_info = first_line.split(", ")
                        shift = int(shift_info[0].split(": ")[1])
                        direction = shift_info[1].split(": ")[1]
                        encrypted_message = file.read().strip()
                        decrypted_message = encrypt_message(encrypted_message, shift, "left" if direction == "right" else "right")
                        helper_clear_screen()
                        print ("\n")
                        print ("=" * 40)
                        print ("Decrypted Message: " + decrypted_message)
                        print ("=" * 40)
                        auditLog.append("Time: " + str(datetime.now()) + " - - - File loaded and decrypted: " + filename + ".txt")
                print ("Click 'Enter' to continue... ")
                input()
            
            elif option == "6":
                helper_clear_screen()
                print ("=" * 40)
                print ("        View Security Audit Log")
                print ("=" * 40)
                print ("\n")
                print ("*" * 40)
                print ("Audit Log:")
                for action in auditLog:
                    print (action)
                print ("*" * 40)
                print ("Click 'Enter' to continue... ")
                input()
            
            elif option == "7":
                while currentuser is not None:
                    helper_clear_screen()
                    print ("=" * 40)
                    print ("                 Settings")
                    print ("=" * 40)
                    setting_choice = input ("1. Change Password\n2. Logout\n3. Back to Menu\n\nEnter your choice: ")
                    if setting_choice == "1":
                        new_password = getpass.getpass("Enter your new password: ")
                        if hashlib.sha256(new_password.encode()).hexdigest() == users[currentuser]:
                            helper_clear_screen()
                            print ("\n")
                            print ("=" * 40)
                            print ("New password cannot be the same as the old password! Try Again!")
                            print ("=" * 40)
                            print ("Click 'Enter' to continue... ")
                            input()
                            continue
                        confirmPassword = getpass.getpass("Confirm your password: ")
                        if new_password != confirmPassword:
                            helper_clear_screen()
                            print ("\n")
                            print ("=" * 40)
                            print ("Passwords do not match! Try Again!")
                            print ("=" * 40)
                            print ("Click 'Enter' to continue... ")
                            input()
                            continue
                        
                        users[currentuser] = hashlib.sha256(new_password.encode()).hexdigest()
                        helper_clear_screen()
                        print ("\n")
                        print ("=" * 40)
                        print ("Password changed successfully!")
                        print ("=" * 40)
                        auditLog.append("Time: " + str(datetime.now()) + " - - - Password changed for user: " + currentuser)
                        print ("Click 'Enter' to continue... ")
                        input()
                    elif setting_choice == "2":
                        helper_clear_screen()
                        print("\n")
                        print ("=" * 40)
                        print ("Logging out. Goodbye, " + currentuser + "!")
                        print ("=" * 40)
                        auditLog.append("Time: " + str(datetime.now()) + " - - - User logged out: " + currentuser)
                        isAuthenticated = False
                        currentuser = None
                        print ("Click 'Enter' to continue... ")
                        input()
                    elif setting_choice == "3":
                        helper_clear_screen()
                        print("\n")
                        print ("=" * 40)
                        print ("Exiting the system. Goodbye!")
                        print ("=" * 40)
                        break
                    
            elif option == "8":
                helper_clear_screen()
                print("\n")
                print ("=" * 40)
                print ("Exiting the system. Goodbye!")
                print ("=" * 40)
                auditLog.append("Time: " + str(datetime.now()) + " - - - User exited the system: " + currentuser)
                break
            else:
                helper_clear_screen()
                print ("\n")
                print ("=" * 40)
                print ("Invalid option! Please try again.")
                print ("=" * 40)
                print ("Click 'Enter' to continue... ")
                input()
        
    elif choice == "3":
        helper_clear_screen()
        print("\n")
        print ("=" * 40)
        print ("Exiting the system. Goodbye!")
        print ("=" * 40)
        break
    
    else:
        helper_clear_screen()
        print ("\n")
        print ("=" * 40)
        print ("    Invalid choice! Please try again.")
        print ("=" * 40)
        print ("Click 'Enter' to continue... ")
        input()