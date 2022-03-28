print()
print("*****looping demo******" )
print()

for item in range(0, 5 ):
    print(item)
    
 # ask the user if they ant to keep going...
    keep_going = input("enter to keep looping, or any key to quit")   
 
    # end loop if user presses enter
    
    if keep_going != "":
            break
        
print()
print("we are done")    
print()