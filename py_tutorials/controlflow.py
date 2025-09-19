#Tutorials from mainly pynative ot w3schools
"""flow control is the order in which statements or 
blocks of code are executed at runtime based on a condition.
control flows are divided into three categories
1.CONDITIONAL STATEMENTS(if , if else, if elif else, nested if else)--acts depending 
on a condition being true or false

2.TRANSFER STATEMENTS (break, continue,pass)
used to alter a programs way of executiion

3.Iterative STATEMENTS (for and while loop)---terative statements allow us to
execute a block of code repeatedly as long as the condition is True
"""

#if condtions execute if the condtion given is true
"""
number = 6
if number > 5:
    print(number * number)
"""
    
    
"""    
#if else ---this checks if the (if) condition is false...then it runs
name = input("Enter your name: ")
if name == "matthew":
    print("You are right")
else:
    print("Change your name")    
"""

#IF ELIF ELSE STATEMENT
#These are used when we want to test two possible situations..
# but only one can be evaluated
"""
age = 12
if age < 4:
    print("The price is $20")
elif age < 8:
    print("The price is $30") 
else:
    print("The price is $40")       
# for the second example you only need to print once because of it structure
"""

"""
age = 12
if age < 4:
    price = 20
elif age < 8:
    price = 30
else:
    price = 40             
print(f"The price of the particular age is ${price}")    
"""

#Multiple elif statements are used when the condtions are more or complex
temperature = 75

if temperature > 90:
    print("Very hot - stay indoors")
elif temperature > 80:
    print("Hot - light clothing")
elif temperature > 70:          # This matches
    print("Warm - comfortable")
elif temperature > 60:
    print("Mild - light jacket")
elif temperature > 50:
    print("Cool - jacket needed")
else:
    print("Cold - bundle up")
#the program executes the first true condition which is > 70    

#OMIITING THE ELSE BLOCK
# Sometimes an else block is useful; sometimes it is clearer to use an additional
#elif statement that catches the specific condition of interest
#When this is done every block of code must be true/or satisfy a conditon to be execute
""""
age = 20
if age < 4:
    price = 20
elif age < 16:
    price = 30
elif age == 20:
    price = 40             
print(f"The price of the particular age is ${price}")    
"""

#TO TEST FOR MULTIPLE TURE STATEMENTS WE USE MULTIPLE IF CONDITONS
#IF ELSE EXECUTES THE FIRST TRUE CONDITION
score = 85
if score >= 80:
    print("Good job!")        # ✅ Executes (85 >= 80)
if score >= 70:  
    print("Passing grade")    # ✅ Also executes (85 >= 70)
if score >= 60:
    print("Above average")    # ✅ Also executes (85 >= 60)
 
 
#NESTED IF STATEMENTS
#useful for making a series of decisions
#SIMPLE NESTED
age = 25
has_license = True

if age >= 18:                    # No print here
    if has_license:
        print("You can drive!")  # Only inner prints
    else:
        print("Get a license first")
else:
    print("Too young to drive")
 
 
#MULTIPLE INNER ACTIONS
score = 85
bonus_available = True

if score >= 70:                  # No print for passing
    if score >= 90:
        print("Excellent! A grade")
    elif score >= 80:
        print("Good job! B grade") 
        if bonus_available:      # Another nested level
            print("Bonus points added!")
    else:
        print("You passed with C grade")
else:
    print("Failed - need to retake")    
    
#
weather = "sunny"
temperature = 75

if weather == "sunny":           # No print here
    if temperature > 80:
        print("Perfect beach day!")
    elif temperature > 65:
        print("Great weather for a walk!")
    else:
        print("Sunny but chilly")
else:                           # No print here either
    if temperature > 70:
        print("Warm but not sunny")
    else:
        print("Cold and gloomy")    
        
        
    