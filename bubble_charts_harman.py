

#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N9920811
#    Student name: HARMANJEET SINGH
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  BUBBLE CHARTS
#
#  This task tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function,
#  "draw_bubble_chart".  You are required to complete this function
#  so that when the program is run it produces a bubble chart,
#  using data stored in a list to determine the positions and
#  sizes of the icons.  See the instruction sheet accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#  



#-----Preamble and Test Data-----------------------------------------#
#
#

# Module provided
#
# You may use only the turtle graphics functions for this task;
# you may not import any other modules or files.

from turtle import *


# Given constants
#
# These constant values are used in the main program that sets up
# the drawing window; do not change any of these values.

max_value = 350 # maximum positive or negative value on the chart
margin = 25 # size of the margin around the chart
legend_width = 400 # space on either side of the window for the legend
window_height = (max_value + margin) * 2 # pixels
window_width = (max_value + margin) * 2 + legend_width # pixels
font_size = 12 # size of characters on the labels in the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
tick_size = 5 # size of the ticks on either side of the axes, in pixels


# Test data
#
# These are the data sets that you will use to test your code.
# Each of the data sets is a list containing the specifications
# for several icons ("bubbles") to display on the screen.  Each
# such list element specifies one icon using four values:
#
#    [icon_style, x_value, y_value, z_value]
#
# The 'icon_style' is a character string specifying which icon to
# to display.  Possible icons are named 'Icon 0' to 'Icon 4'.
# The final three values are integers specifying the icon's values
# in three dimensions, x, y and z.  The x and y values will be in
# the range -350 to 350, and determine where to place the icon on
# the screen.  The z value is in the range 0 to 350, and determines
# how big the icon must be (i.e., its widest and/or highest size on
# the screen, in pixels).

# The first icon in three different sizes
data_set_00 = [['Icon 0', -200, 200, 20],
               ['Icon 0', 200, 200, 120],
               ['Icon 0', 0, 0, 100]]

# The second icon in four different sizes
data_set_01 = [['Icon 1', -200, 200, 20],
               ['Icon 1', 200, 200, 120],
               ['Icon 1', 200, -200, 60],
               ['Icon 1', 0, 0, 100]]

# The third icon in five different sizes
data_set_02 = [['Icon 2', -200, 200, 300],
               ['Icon 2', -200, -200, 30],
               ['Icon 2', 200, -200, 90],
               ['Icon 2', 200, 200, 120],
               ['Icon 2', 0, 0, 100]]

# The fourth icon in four different sizes
data_set_03 = [['Icon 3', -200, 200, 300],
               ['Icon 3', -200, -200, 30],
               ['Icon 3', 200, -200, 90],
               ['Icon 3', 0, 0, 100]]

# The fifth icon in four different sizes
data_set_04 = [['Icon 4', 200, 200, 190],
               ['Icon 4', -200, -200, 10],
               ['Icon 4', 200, -200, 90],
               ['Icon 4', 0, 0, 100]]

# The next group of data sets test all five of your icons
# at the same time

# All five icons at the same large size
data_set_05 = [['Icon 0', -200, 200, 200],
               ['Icon 1', 200, 200, 200],
               ['Icon 2', 200, -200, 200],
               ['Icon 3', -200, -200, 200],
               ['Icon 4', 0, 0, 200]]

# All five icons at another size, listed in a different order
data_set_06 = [['Icon 4', 0, 0, 150],
               ['Icon 3', -200, -200, 150],
               ['Icon 2', -200, 200, 150],
               ['Icon 1', 200, 200, 150],
               ['Icon 0', 200, -200, 150]]

# All five icons arranged diagonally, at increasing sizes
data_set_07 = [['Icon 0', -200, -200, 15],
               ['Icon 1', -100, -100, 50],
               ['Icon 2', 0, 0, 100],
               ['Icon 3', 100, 100, 120],
               ['Icon 4', 200, 200, 180]]

# An extreme test in which all five icons are VERY small
data_set_08 = [['Icon 0', -100, -80, 5],
               ['Icon 2', 100, -100, 1],
               ['Icon 3', 10, 30, 2],
               ['Icon 1', 100, 100, 0],
               ['Icon 4', 200, 200, 4]]

# The next group of data sets are intended as "realistic" ones
# in which all five icons appear once each at various sizes in
# different quadrants in the chart

# Data occurs in all four quadrants
data_set_09 = [['Icon 0', -265, -80, 50],
               ['Icon 2', 100, -146, 78],
               ['Icon 3', -50, 130, 69],
               ['Icon 1', 210, 100, 96],
               ['Icon 4', 200, 300, 45]]

# All data appears in the top quadrants
data_set_10 = [['Icon 4', -265, 80, 140],
               ['Icon 2', 100, 146, 24],
               ['Icon 1', 10, 30, 99],
               ['Icon 0', 210, 100, 75],
               ['Icon 3', 200, 300, 65]]

# All data appears in the top right quadrant
data_set_11 = [['Icon 3', 265, 80, 140],
               ['Icon 1', 100, 146, 24],
               ['Icon 2', 20, 30, 109],
               ['Icon 4', 210, 205, 75],
               ['Icon 0', 200, 300, 65]]

# All data appears in the bottom left quadrant
data_set_12 = [['Icon 2', -265, -110, 130],
               ['Icon 3', -100, -146, 34],
               ['Icon 0', -25, -40, 73],
               ['Icon 1', -210, -200, 75],
               ['Icon 4', -180, -320, 65]]

# Another case where data appears in all four quadrants
data_set_13 = [['Icon 4', -265, 80, 96],
               ['Icon 3', 100, -46, 54],
               ['Icon 2', 50, 30, 89],
               ['Icon 1', -210, -190, 75],
               ['Icon 0', 250, 300, 123]]

# Yet another set with data in all four quadrants
data_set_14 = [['Icon 1', 212, -165, 90],
               ['Icon 2', 153, -22, 125],
               ['Icon 3', 84, 208, 124],
               ['Icon 4', -105, -58, 85],
               ['Icon 0', -62, 274, 57]]


# A random test - it produces a different data set each time you run
# your program!
from random import randint
max_rand_coord = 300
min_size, max_size = 20, 200

data_set_15 = [[icon,
                randint(-max_rand_coord, max_rand_coord),
                randint(-max_rand_coord, max_rand_coord),
                randint(min_size, max_size)]
               for icon in ['Icon 0', 'Icon 1', 'Icon 2', 'Icon 3', 'Icon 4']]

# Finally, just for fun, a random test that produces a montage
# by plotting each icon twenty times (which obviously doesn't
# make sense as a real data set)
data_set_16 = [[icon,
                randint(-max_rand_coord, max_rand_coord),
                randint(-max_rand_coord, max_rand_coord),
                randint(min_size, max_size)]
               for icon in ['Icon 0', 'Icon 1', 'Icon 2', 'Icon 3', 'Icon 4'] * 20]

#***** If you want to create your own test data sets put them here


# Each data appears in the each quadrants and one at the origin
data_set_17 = [['Icon 4', 130, 100, 150],
               ['Icon 2', 0, 0, 100],
               ['Icon 1', -100, 100, 100],
               ['Icon 0', 130, -100, 150],
               ['Icon 3', -100, -100, 100]]
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the task by replacing the dummy function below with
#  your code

######## CHEVROLETT
def draw_chevrolett(xcoord, ycoord, size):

    # moving turtle to desired  location
    penup()
    goto(xcoord, ycoord)
    setheading(270)
    forward(size / 4)
    pendown()

    
    setheading(0)     # pointing towards east
    width(size / 100) # defining width of pen
    color("black")    # defining colour

    # draw lines to form CHEVROLETT LOGO and
    # fill it with orange colour
    # draw first line
    begin_fill()
    forward(size / 8)

    # draw second line
    left(90) # point turtle towards north
    forward(size / 8)

    # draw third line
    right(90) # point turtle towards east
    forward(size / 3)

    # draw fourth line
    left(70) # point turtle towards north-east
    forward(size / 4)

    # draw fifth line
    left(110) # point turtle towards west
    forward(size / 2.35)

    # draw sixth line
    right(90) # point turtle towards north
    forward(size / 8)

    # draw seventh line 
    left(90) # point turtle towards west
    forward(size / 4)

    # draw eighth line 
    left(90) # point turtle towards south
    forward(size / 8)

    # draw ninth line
    right(90) # point tutle towards west
    forward(size / 3)

    #draw tenth line 
    left(70) # point turtle towards south-west
    forward(size / 4)

    # draw eleventh line
    left(110) # point turtle towards east
    forward(size / 2.35)

    # draw twelveth line
    right(90) # point turtle towards south
    forward(size / 8)

    # draw thirteenth line
    left(90) # point towards east
    forward(size / 7)

    color("orange")

    end_fill()

########## End of Chevrolett function

    

####### BMW
def draw_bmw(xcoord, ycoord, size):

    # moving turtle to desired  location
    penup()
    goto(xcoord, ycoord)
    setheading(270)
    forward(size / 2)
    pendown()
    
    setheading(0)    # pointing towards east
    color("black")   # defining colour
    width(size / 40) # defining width of pen

    # draw a circle and fill it 
    # with black colour
    begin_fill()
    circle(size / 2)
    color("black")
    end_fill()

    # move turtle to desired location to
    # draw an inner  circle 
    setheading(90)
    penup()
    forward(size / 10)
    pendown()

    # draw an inner circle and fill
    # it with white colour
    setheading(0) # point turtle towards east
    begin_fill()
    circle((size / 2) - (size / 10))
    color("white")
    end_fill()


    # move turtle to desired location to
    # draw first segment of circle
    penup()
    left(90)
    forward(size / 100)
    right(90)
    pendown()

    # draw first segment of circle and fill it with
    # blue colour
    width(size / 100) # defining width of pen
    color("blue") #defining colour of segment
    begin_fill()
    circle(((size / 2) - ((size / 10) + (size / 80))), 90)
    left(90)
    forward((size / 2) - ((size / 10) + (size / 80)))
    left(90)
    forward((size / 2) - ((size / 10) + (size / 80)))
    color("blue")
    end_fill()

    # move turtle to desired location to
    # draw second segment of circle
    setheading(90) # point turtle towards north
    forward((size / 2) - (size / 11))

    # draw second segment of circle and fill it with
    # blue colour
    begin_fill()
    forward((size / 2) - ((size / 10)+ (size / 40)))
    setheading(180)
    circle(((size / 2) - (size / 10)), 90)
    setheading(0)
    forward((size / 2) - (size / 10))
    color("blue")
    end_fill()

############ End of BMW function


############ VOLKSWAGEN

def draw_vw(xcoord, ycoord, size):

    # moving turtle to desired  location
    penup()
    goto(xcoord, ycoord)
    setheading(270)
    forward(size / 2)
    pendown()

    setheading(0)  # pointing towards east
    color("black") # defining colour
    width(size / 20) # defining width of pen

    # draw a circle and fill it 
    # with red colour
    begin_fill()
    color("yellow")
    circle(size / 2)
    end_fill()

    color("black") #defining colour of pen to draw lines

    # move turtle to the desired location
    # to draw the lines(V and W)
    penup()
    setheading(90)
    forward((size / 2) - (size / 10))
    pendown()

    # draw V
    # draw first line of V
    setheading(120) # point turtle towards north-west
    forward((size / 2) + (size / 12))

    # move turtle back to the desired location
    # to draw second line of V
    right(180)
    forward((size / 2) + (size / 12))

    # draw first line of V
    setheading(60) # point turtle towards north-east
    forward((size / 2) + (size / 12))

    # draw W
    # draw first line of W
    right(180)
    forward(size)

    # move turtle back to the desired location
    # to draw second line of W
    right(180)
    forward((size / 2) - (size / 10))

    # draw second line of W
    setheading(300) # point turtle towards south-east
    forward((size / 2) - (size / 10))

    # draw third line of W
    setheading(60) # point turtle towards north-east
    forward((size / 2)  + (size / 12))

    # move turtle back to the desired location
    # to draw fourth line of W
    right(180)
    forward((size / 2)  + (size / 12))

    setheading(120)
    forward((size / 2)  - (size / 10))

    setheading(240)
    forward((size / 2) - (size /  10))

    # draw fourth line of W
    setheading(120) # point turtle towards north-west
    forward((size / 2)  + (size / 12))

############# End of VOLKSWAGEN function    
    
############# MERCEDES

def draw_mercedes(xcoord, ycoord, size):

    # moving turtle to desired  location
    penup()
    goto(xcoord, ycoord)
    setheading(270)
    forward(size / 2)
    pendown()

    setheading(0)    # pointing towards east
    color("red")     # defining colour
    width(size / 15) # defining width of pen

    # draw a circle and fill it 
    # with black colour
    begin_fill()
    circle(size / 2)
    color("white")
    end_fill()
    
    # move turtle to desired location 
    # to draw the lines
    setheading(90)
    penup()
    forward(size)
    pendown()

    color("red") # define colour of pen to draw lines
    

    # draw first line
    setheading(270) # point turtle towards south
    forward(size - (size / 1.7))
    
    

    # draw second line
    setheading(215) # point turtle towards south-west
    forward((size / 2) + (size / 20))

    # move turtle to the centre
    right(180)
    forward((size / 2) + (size / 20))

    # draw third line
    setheading(325) # point turtle towards south-east
    forward((size / 2) + (size / 20))

############## End of MERCEDES function 

    

    
#############AUDI

def draw_audi(xcoord, ycoord, size):

    # moving turtle to desired  location
    penup()
    goto(xcoord , ycoord)
    setheading(270)
    forward(size / 4)
    pendown()
    
    color("black") # defining colour
    width(size / 50) # defining width of pen

    # draw a rectangle and fill it 
    # with black colour 
    begin_fill()
    left(90)
    forward(size / 2)
    left(90)
    forward(size / 2)
    left(90)
    forward(size)
    left(90)
    forward(size / 2)
    left(90)
    forward(size / 2)
    color("green")
    end_fill()
    
    # move turtle to desired location
    # to draw rings
    penup()
    setheading(180)
    forward(size / 4)
    setheading(90)
    forward(size / 7)
    pendown()

    # define colour of pen to draw rings
    color("white")
    setheading(0)

    # draw first ring
    circle(size / 8)

    penup()
    forward(size / 6)
    pendown()

    # draw second ring
    circle(size / 8)

    penup()
    forward(size / 6)
    pendown()

    # draw third ring
    circle(size / 8)

    penup()
    forward(size / 6)
    pendown()

    # draw fourth ring
    circle(size / 8)

############# End of AUDI function

############# Draw LEGEND

def draw_legend():
    
    global audi_drawn, mercedes_drawn, vw_drawn, bmw_drawn, chevrolett_drawn

    # Move turtle to desired location to draw a
    # rectangular box 
    penup()
    goto(370, 200)
    pendown()

    color("black") # define colour of pen
    width(2)       # define width of pen
    setheading(0)  # point turtle towards east

    # draw a rectangular box
    forward(180)
    right(90)
    forward(400)
    right(90)
    forward(180)
    right(90)
    forward(400)

    # move to appropriate location to write title of LOGOS
    penup()
    goto(380, 175)
    pendown()

    # write the title
    write("Automobile Makes",font = ("Arial",12, "bold"))

    # Display audi in legend only if its LOGO is drawn on the screen 
    if audi_drawn:

        # draw the logo
        draw_audi(410, 140, 50)

        # move turtle to appropriate location
        # to write name of LOGO
        penup()
        goto(450, 135)
        pendown()
        color("black")

        # write the name AUDI
        write("AUDI",font = ("Arial",10, "normal"))

    # Display mercedes in legend only if its LOGO is drawn on the screen
    if mercedes_drawn and audi_drawn:

        # draw the logo
        draw_mercedes(410, 70, 50)

        # move turtle to appropriate location
        # to write name of LOGO
        penup()
        goto(450, 65)
        pendown()
        color("black")

        # write the name MERCEDES
        write("MERCEDES",font = ("Arial",10, "normal"))

    # draw mercedes in the first psition in the legend
    # if it is the only logo drawn on the screen
    elif mercedes_drawn and not audi_drawn:

        # draw the logo
        draw_mercedes(410, 140, 50)

        # move turtle to appropriate location
        # to write name of LOGO
        penup()
        goto(450, 135)
        pendown()
        color("black")

        # write the name MERCEDES
        write("MERCEDES",font = ("Arial",10, "normal"))

    # Display vw in legend only if its LOGO is drawn on the screen
    if vw_drawn and audi_drawn and mercedes_drawn: 

        # draw the logo
        draw_vw(410, 0, 50)

        # move turtle to appropriate location
        # to write name of LOGO
        penup()
        goto(450, -5)
        pendown()
        color("black")

        # write the name VOLKSWAGEN
        write("VOLKSWAGEN",font = ("Arial",10, "normal"))

    # draw vw in the first psition in the legend
    # if it is the only logo drawn on the screen
    elif vw_drawn and not audi_drawn and not mercedes_drawn:

        # draw the logo
        draw_vw(410, 140, 50)

        # move turtle to appropriate location
        # to write name of LOGO
        penup()
        goto(450, 135)
        pendown()
        color("black")

        # write the name VOLKSWAGEN
        write("VOLKSWAGEN",font = ("Arial",10, "normal"))
     

    # Display bmw in legend only if its LOGO is drawn on the screen
    if bmw_drawn and audi_drawn and mercedes_drawn and vw_drawn:

        # draw the logo
        draw_bmw(410, -70, 50)

        # move turtle to appropriate location
        # to write name of LOGO
        penup()
        goto(450, -75)
        pendown()
        color("black")

        # write the name BMW
        write("BMW",font = ("Arial",10, "normal"))

    # draw bmw in the first psition in the legend
    # if it is the only logo drawn on the screen
    elif bmw_drawn and not chevrolett_drawn and not audi_drawn and not mercedes_drawn and not vw_drawn:
        # draw the logo
        draw_bmw(410, 140, 50)

        # move turtle to appropriate location
        # to write name of LOGO
        penup()
        goto(450, 135)
        pendown()
        color("black")

        # write the name BMW
        write("BMW",font = ("Arial",10, "normal"))

    # Display chevrolett in legend only if its LOGO is drawn on the screen
    if chevrolett_drawn and audi_drawn and mercedes_drawn and vw_drawn and bmw_drawn:
        # draw the logo
        draw_chevrolett(410, -140, 50)

        # move turtle to appropriate location
        # to write name of LOGO
        penup()
        goto(450, -145)
        pendown()
        color("black")

        # write the name CHEVROLETT
        write("CHEVROLETT",font = ("Arial",10, "normal"))

    # draw chevrolett in the first psition in the legend
    # if it is the only logo drawn on the screen
    elif chevrolett_drawn and not audi_drawn and not mercedes_drawn and not vw_drawn and not bmw_drawn:

        # draw the logo
        draw_chevrolett(410, 140, 50)

        # move turtle to appropriate location
        # to write name of LOGO
        penup()
        goto(450, 135)
        pendown()
        color("black")

        # write the name CHEVROLETT
        write("CHEVROLETT",font = ("Arial",10, "normal"))

                        

############ END of LEGEND


# variables to store boolean values to draw legend
audi_drawn = False
mercedes_drawn = False
vw_drawn = False
bmw_drawn = False
chevrolett_drawn = False

def draw_bubble_chart(data_set):
    
    global audi_drawn, mercedes_drawn, vw_drawn, bmw_drawn, chevrolett_drawn

    for data in data_set:

        if data[0] == "Icon 0":
            draw_audi(data[1], data[2], data[3])

            #display audi in legend
            audi_drawn = True

        elif data[0] == "Icon 1":
            draw_mercedes(data[1], data[2], data[3])

            #display mercedes( in legend
            mercedes_drawn = True

        elif data[0] == "Icon 2":
            draw_vw(data[1], data[2], data[3])

            #display vw in legend
            vw_drawn = True

        elif data[0] == "Icon 3":
            draw_bmw(data[1], data[2], data[3])

            #display bmw in legend
            bmw_drawn = True

        elif data[0] == "Icon 4":
            draw_chevrolett(data[1], data[2], data[3])

            #display chevrolett in legend
            chevrolett_drawn = True            

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the drawing environment, ready for you
# to start drawing your bubble chart.  Do not change any of
# this code except the lines marked '*****'
    
# Set up the drawing window with enough space for the grid and
# legend
setup(window_width, window_height)
title('Bubble Chart') #***** Choose a title appropriate to your icons

# Draw as quickly as possible by minimising animation
hideturtle()     #***** You may comment out this line while debugging
                 #***** your code, so that you can see the turtle move
speed('fastest') #***** You may want to slow the drawing speed
                 #***** while debugging your code

# Choose a neutral background colour                    
bgcolor('grey')

# Draw the two axes
pendown() # assume we're at home, facing east
forward(max_value)
left(180) # face west
forward(max_value * 2)
home()
setheading(90) # face north
forward(max_value)
left(180) # face south
forward(max_value * 2)
penup()

# Draw each of the tick marks and labels on the x axis
for x_coord in range(-max_value, max_value + 1, grid_size):

    if x_coord != 0: # don't label zero

        goto(x_coord, -tick_size)
        pendown()
        goto(x_coord, tick_size)
        penup()
        write(str(x_coord), align = 'center',
              font=('Arial', font_size, 'normal'))
        
# Draw each of the tick marks and labels on the y axis
for y_coord in range(-max_value, max_value + 1, grid_size):

    if y_coord != 0: # don't label zero

        goto(-tick_size, y_coord)
        pendown()
        goto(tick_size, y_coord)
        penup()
        goto(tick_size, y_coord - font_size / 2) # Allow for character height
        write('  ' + str(y_coord), align = 'left',
              font=('Arial', font_size, 'normal'))

# Call the student's function to display the data set
draw_bubble_chart(data_set_17) #***** Change this for different data sets

# call the legend function to display LEGEND
draw_legend()

# Exit gracefully
hideturtle()
done()

#
#--------------------------------------------------------------------#




