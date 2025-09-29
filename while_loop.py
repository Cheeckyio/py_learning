#this section is for while loops and nested loops
#while loop execute a block of code as long as a given condition
"""for loops guarantee a fixed number of iterations based on the elements in the sequence being iterated
 over.
while loops, on the other hand, provide more flexibility for handling an unknown number of iterations.
 The loop continues to iterate as long as the condition remains True.
 This can lead to zero iterations if the condition is False from the start."""
#USER INPUT VALIDATION
age = 0
while age < 18:
    age = int(input("Enter your age: "))
print("you are old enough to proceed")    