import sys

action = ""
direction = ""
text = ""
numberOfShifts = 0

alphabet = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    15: "p",
    16: "q",
    17: "r",
    18: "s",
    19: "t",
    20: "u",
    21: "v",
    22: "w",
    23: "x",
    24: "y",
    25: "z"
}

def helperGetKey (value):
    for key, v in alphabet.items():
        if v == value:
            return key
    return None

def inputFunc ():    
    global action, direction, text, numberOfShifts
    flag = False
    while not flag:
        print ("Do you want to Encrypt or Decrypt a message? (Enter E or D): ", end="")
        action = input()
        action = action.lower()
        if action != "e" and action != "d" or action == "":
            action = ""
            print ("Invalid input! Try again")
        else:
            flag = True
            if action == "d":
                flag = False
                while not flag:
                    msg = "decrypted"
                    print (f"Enter the text to be {msg}: ", end = "")
                    text = input()

                    if text == "":
                        print ("Text is empty! Try again!: ")
                    else:
                        flag = True
                        return action, direction, text, numberOfShifts
            
    flag = False
    while not flag:
        print ("Enter direction. (R or L): ", end="")
        direction = input()
        direction = direction.lower()
        if direction != "r" and direction != "l" or direction == "":
            print ("Invalid input! Try again") 
        else:
            flag = True
            
    flag = False
    while not flag:
        msg = ""
        if action == "e":
            msg = "encrypted"
        else:
            msg = "decrypted"
        print (f"Enter the text to be {msg}: ", end="")
        text = input()

        if text == "":
            print ("Text is empty! Try again!: ")
        else:
            flag = True
            
    
    flag = False
    while not flag:
        userInput = input ("Enter the key, a number other than 0 or multiples of 26: ").strip()
        
        if userInput == "":
            print("Invalid input! Try again! ")
            continue
        if not userInput.lstrip("-").isdigit():
            print("Invalid input! Try again! ")
            continue
        numberOfShifts = int(userInput)
        numberOfShifts %= 26
        if numberOfShifts == 0:
            print("Invalid input! Try again! ")
        else:
            if numberOfShifts < 0:
                numberOfShifts *= -1
            flag = True
    return action, direction, text, numberOfShifts

choice = True
while choice:
    action, direction, text, numberOfShifts = inputFunc ()
    encryptedText = ""
    
    if action == "e":
        if direction == "l":
            for ch in text:
                ePos = (helperGetKey(ch.lower()) - numberOfShifts) % 26
                cap = ""
                if ch.upper() == ch:
                    cap = "Upper"
                else:
                    cap = "Lower"
                if cap == "Upper":
                    encryptedText += alphabet[ePos].upper()
                else:
                    encryptedText += alphabet[ePos].lower()
        else:
            for ch in text:
                ePos = (helperGetKey(ch.lower()) + numberOfShifts) % 26
                cap = ""
                if ch.upper() == ch:
                    cap = "Upper"
                else:
                    cap = "Lower"
                if cap == "Upper":
                    encryptedText += alphabet[ePos].upper()
                else:
                    encryptedText += alphabet[ePos].lower()
        print("Encrypted text: ", encryptedText) 
    
    else:
        for shifts in range (1, 26):
            decryptedText = ""
            for ch in text:
                ePos = (helperGetKey(ch.lower()) - shifts) % 26
                cap = ""
                if ch.upper() == ch:
                    cap = "Upper"
                else:
                    cap = "Lower"
                if cap == "Upper":
                    decryptedText += alphabet[ePos].upper()
                else:
                    decryptedText += alphabet[ePos].lower()
            print(f"Decrypted text (C{shifts}): ",decryptedText) 
            
    
    flag = False
    while not flag:
        print("Do you want to continue? (y/n): ",end="")
        choice = input().lower()
        
        if choice == "" or choice != "y" and choice != "n":
            print("Invalid input! Try again!")
        elif choice == "n":
            sys.exit()
            break
        else:
            flag = True