print()
print("Coffee order demo")

keep_going = ""
while keep_going == "":
    
    want_coffee = input("Do you want hot chocolate?")
    if want_coffee != "yes":
        print("wrong answer, you always want hot chocolate")
        continue
    
    else:
        print()
        print("Good choice")
        print()
        break
    
print()
print("End of program")
print()