# ITS 2801 Week 2
# Turtle version 1
### IMPORTANT:
# you need to install a linux package before this can work:
# in the terminal, type the command
#     sudo apt update
#     sudo apt install python3-tk
# at the prompt type the same password you use to log into the VM
# you will be asked
#     Do you want to continue? [Y/n]
# just hit enter at the prompt
###
# 
# The code below retriebves the screen width and height and turns the
# turtle to point up.
# Add code to:
# 1.) draw a black rectangle 50 pixels inside the screen border
# 2.) draw a red rectangle that is half the size of the first one, and
#     centered inside it.

# leave the next 3 lines as-is
import turtle

height = turtle.window_height()
width = turtle.window_width()

# 1. Get to Top Left Corner - 50 px
inset = 50
top_left_xinset = (width / 2) - inset
top_left_yinset = (height / 2) - inset

turtle.penup()

# Starts facing right
turtle.left(180)
turtle.forward(top_left_xinset)
turtle.right(90)
turtle.forward(top_left_yinset)

# 2. Set color, touchdown, and go to each remaining corner
outer_rect_width = width - inset * 2
outer_rect_height = height - inset * 2

turtle.color("black")
turtle.pendown()
turtle.right(90)
turtle.forward(outer_rect_width)
turtle.right(90)
turtle.forward(outer_rect_height)
turtle.right(90)
turtle.forward(outer_rect_width)
turtle.right(90)
turtle.forward(outer_rect_height)

# 3. Penup, return to center, set color

turtle.penup()
turtle.right(180)
turtle.forward(outer_rect_height / 2)
turtle.left(90)
turtle.forward(outer_rect_width / 2)
turtle.color('red')

# 4. Get to Top Left Corner of half-size rectangle incl inset

inner_rect_width = outer_rect_width / 2
inner_rect_height = outer_rect_height / 2

turtle.left(180)
turtle.forward(inner_rect_width/2)
turtle.right(90)
turtle.forward(inner_rect_height / 2)

# 5. Pendown, Go to remaining corners

turtle.pendown()
turtle.right(90)
turtle.forward(inner_rect_width)
turtle.right(90)
turtle.forward(inner_rect_height)
turtle.right(90)
turtle.forward(inner_rect_width)
turtle.right(90)
turtle.forward(inner_rect_height)

# 6. Read turtle documentation, because .goto exists...

# +++ Add your script here +++



# leave this line as-is
turtle.exitonclick()
