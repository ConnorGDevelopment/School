# In this script we "manually" control the turtle
# Your script takes input from the user in an infinite loop
# Input from the user is in the form 
# code,value
# for example "f,100" means forward 100, "r,22.5" means right 22.5 degrees, etc.
###
# Your script must handle:
# f,number -- forward by that number
# l,number -- turn left by that number
# r,number -- turn right by that number
# c,color -- switch to the named color
# u -- pen up
# d -- pen down
# q -- quit
###
# The code must be accepted in upper and lower case
# User errors must not cause the script to crash or the loop to exit. Use try/except as needed.
#
# *** Extra credit: when the user type an unrecognized code, print a help message with the allowed codes
###
# Setup (we don;t need the screen dimensions, just good practice)
import turtle
height = turtle.window_height()
width = turtle.window_width()
#
# The input loop as we set it up in class
# 

# Used to play command_text() once on start
is_dirty = False

while True:
    def command_text():
        print('Available Commands')
        print('f,number -- Move forward by X pixels')
        print('l,number -- Turn left by X degrees')
        print('r,number -- Turn right by X degrees')
        print('c,color -- Change pen color to X')
        print('u -- Lift pen from canvas')
        print('d -- Touch pen to canvas')
        print('q -- Exit')
        
    if(is_dirty == False):
        command_text()
        is_dirty = True
        
    answer = input("> ")
    tokens = answer.split(",")
    if tokens[0].lower() == "q":
        break
        
    func_to_run = False
    
    # In JS, I would normally use a switch statement so I looked up the equivalent for Python
    func_letter = tokens[0].lower()
    
    # Match function based on first token
    match func_letter:
        case 'f':
            func_to_run = turtle.forward
        case 'l':
            func_to_run = turtle.left
        case 'r':
            func_to_run = turtle.right
        case 'c':
            func_to_run = turtle.color
        case 'u':
            func_to_run = turtle.penup
        case 'd':
            func_to_run = turtle.pendown
        case _ :
            print('First Value is not a valid command')
            command_text()
        
    # Handle functions with numeric param
    if(['f', 'l', 'r'].count(func_letter) > 0):
        distance = 0
        try:
            distance = float(tokens[1])
            
            try:
                func_to_run(distance)
            except:
                print('An unexpected error happened, please contact support')
                command_text()
        except:
            print('Second Value could not be converted to a number')

    # Handle functions with string param
    elif(func_letter == 'c'):
        color = tokens[1]
        
        try:
            # If tokens[1] is a color, then float() should error because it can't convert to number
            color = float(tokens[1])
            # If float(tokens[1]) works then it is an invalid color input
            print('Second Value could not be converted to a color')
            command_text()
        except:
            try:
                color = color.lstrip()
                func_to_run(color)
            except:
                print('An unexpected error happened, please contact support')
                command_text()
    # Handle functions without param
    else:
        try:
            func_to_run()
        except:
            print('An unexepected error happened, please contact support')
            command_text()
    
   
            
            
# Fill in the remainder of the loop
# Note - we do NOT need exitonclick, the loop holds the graphics until exit