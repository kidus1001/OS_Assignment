import os

def helper_clear_screen ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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

users = {}

helper_clear_screen()
while True:
    
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
        else:
            print ("Invalid username or password! Try Again!")
        
        print ("Main loop and tasks . . . ")
        print ("Click 'Enter' to continue... ")
        input()
    elif choice == "3":
        helper_clear_screen()
        print ("Exiting the system. Goodbye!")
        break
    else:
        helper_clear_screen()
        print ("Invalid choice! Please try again.")