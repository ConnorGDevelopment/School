# Week 3 - Drawing squares using functions and loops
# - Your script will draw a number of squares - the exact number is set by the constant "STEPS"
# - The first square will have its top/left corner in the top/left corner of the window
# - Each subsequent square will have its top/left corner touch the bottom/right corner of the previous square
# - The size of the squares must be computed so the last square touches either the side or th bottom of the screen
# - No portion of any square shall be drawn outside the window
# - The line color of the squares will be determined, in order, by the colors listed in "COLORS"
# - If there are more squares than colors, the final squares will all use the last available color

# COLORS can be modified at will - your script must continue to run correctly as long as it contains at least one color
COLORS = ("black","blue","green","brown2","darkmagenta","darkorange","red")
# STEPS can be modified at will - your script must run correctly as long as it is set between 1 and 50
STEPS = 15

# Keep the next 3 lines to get the environment set up
import turtle
height = turtle.window_height()
width = turtle.window_width()

#+++  Your script starts here - note the hints provided +++

# This is the function you need to define.
# The function will draw one square.
# The passed variables are:
# - the size (length of the sides) of the square
# - a list with 2 numbers for the x and y coordinates of the top/left corner of the square
# - the color for this square
# this functions does not return a value
# You can use differnt names for the passed variables if you like
# As we did in class, you might start with just the size variable and make sure the function draws a square
def draw_box(my_size,start_location,my_color):
    # remove the "pass" line below before you start on the function - it is needed to run with an empty function
    # Set Color, Lift, Go to Start
    turtle.color(my_color)
    turtle.penup()
    turtle.goto(start_location[0], start_location[1])
    turtle.pendown()
    
    # Right
    turtle.seth(0)
    turtle.forward(my_size)
    
    # Down
    turtle.seth(270)
    turtle.forward(my_size)
    
    # Left
    turtle.seth(180)
    turtle.forward(my_size)
    
    # Up
    turtle.seth(90)
    turtle.forward(my_size)
    
    

# you need to compute a few variables:
#
# fit the squares:
# sizex = the width of the window divided by the number of squares
# sizey = the height of the window divided by the number of squares
#  The squares need to fit into the window, compute
#  size = use either the min or the max function

size = min(turtle.window_height(), turtle.window_width()) / STEPS

# create variable to hold the position for the next square, the one below would be in the center of the screen,
# you need to replace the "0"s with the correct values for the first square.
top_left = [
    -turtle.window_width() / 2,
    turtle.window_height() / 2
]

# Start your loop here
# Loop as many times as defined by STEPS
# In the loop:
# - select the color; use the min or the max function to make sure you don't ask for a color that does not exist
# - call your function to draw the square
# - update the top_left variable to the starting position of the next square

for step in range(STEPS):   
    # I was originally trying to make the color wrap around by using a ternary operator (I use these a lot in JS)
    # Where it uses COLORS[step] if step is a valid index
    # And COLORS[step - the number of times its wrapped around]
    # I had issues with the math initially but then realized that I was just trying to calculate a remainder
    color = COLORS[step % len(COLORS)]
    draw_box(size, top_left, color)
    top_left = [top_left[0] + size, top_left[1] - size]


# leave this line as-is
turtle.exitonclick()
