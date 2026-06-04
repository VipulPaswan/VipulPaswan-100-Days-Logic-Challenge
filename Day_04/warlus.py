# Old way
line = input("Enter text: ")
while line != "exit":
    print(f"You entered: {line}")
    line = input("Enter text: ")

# With Walrus Operator
while (line := input("Enter text: ")) != "exit":
    print(f"You entered: {line}")
    
    
    
    
    
    
    
    
    
    
    
