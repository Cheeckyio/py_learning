#this section is for while loops and nested loops
#while loop execute a block of code as long as a given condition
"""for loops guarantee a fixed number of iterations based on the elements in the sequence being iterated
 over.
while loops, on the other hand, provide more flexibility for handling an unknown number of iterations.
 The loop continues to iterate as long as the condition remains True.
 This can lead to zero iterations if the condition is False from the start."""
#USER INPUT VALIDATION
"""
age = 0
while age < 18:#the prompt will keep popping up until the input is greater than 18
    age = int(input("Enter your age: "))
print("you are old enough to proceed")    
"""

"""
#GUESSING GAME
secret_number = 10
guess = 0
guess_count = 0
while guess != secret_number:
    guess_count =+ guess
    guess = int(input("enter the number here: "))
print(f"You guessed it correct on the {guess_count} time")    
"""

#scenario 3
family = ["John", "felicia", "pius", "matthew", " evans", "bright", ]
name_found = False
while not name_found:
    name = input("Search for name in your list (or 'q' to quit): ")
    if name.lower() == "q":
        break# exits the loop after typing q
    if name in family:
        name_found = True
        print("Found the name")
    else:
        print("name not found")    
