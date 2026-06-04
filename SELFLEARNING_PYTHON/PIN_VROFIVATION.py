#pin vrifaction 
print("------------- PIN VERIFICATION -------------\n")
correct_pin = "1234"        

for attempt in range(3):  
    entered_pin = input("Enter your 4-digit PIN: ").strip()

    if entered_pin == correct_pin:
        print("PIN verified successfully. Access granted.")
        break
    else:
        print("Incorrect PIN. Try again.\n")    
else:                                                                                       
    print("Too many incorrect attempts. Access denied.")                                    
## python -u "PIN_VROFIVATION.py"                                                                                                           