"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Reeve Donner

********* HEY, READ THIS FIRST **********

This pattern is called "Evil Eye Orbs". The colorful dots capture movment 
while remaining absolutley still-due to the placement of dots and contrast of the color palette.
The actual meaning of this globally ancient synbol is to cast a curse upon all who are seen by it.
The abnormal variations in color represent the idea evil is within all things, religions, shapes,
colors, etc. The actual affliction of evil exists in everything, but your perception of evil (and
the orbs) influences how you chose to integrate it into your life. 

"""
import turtle
import random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) 
panel = turtle.Screen().bgcolor('black')#600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
#define varibles
#define varibles
turtle.Turtle()
turtSize = (20)
colors = [(0,0,255),(255,153,51), (0,255,255),(204,255,255), (255,153,255)]

#set up color palette
turtle.up()
turtle.shape("turtle")
turtle.speed(10)

###big circles
#draw first two sets of big blue circles 
turtle.goto(-280,200)#location of first two rows

#repeats the drawing of seven circles for two rows of circles
for i in range (2):
    turtle.color(random.choice(colors)) #random generation of colors every time code is run
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(10)
    turtle.right(180)
    turtle.up()
 #draw sets 3 and 4 of big blue circles   
 #location of middle two rows
turtle.goto(-275,-38)

#repeats the drawing of seven circles for two rows of circles    
for i in range (2):
    turtle.color(random.choice(colors)) #random generation of colors every time code is run
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(10)
    turtle.right(180)
    turtle.up()
    
#draw last two sets of big blue circles
turtle.goto(-270,-275)#location of last two rows

#repeats the drawing of seven circles for two rows of circles
for i in range (2):
    turtle.color(random.choice(colors)) #random generation of colors every time code is run
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    
###medium circles   
#set up pen
turtle.up()
turtle.shape("turtle")
turtle.speed(10)

#draw first two sets of medium orange circles 
turtle.goto(-280,210)#location of first two rows

#repeats the drawing of seven circles for two rows of circles
for i in range (2):
    turtle.color(random.choice(colors)) #random generation of colors every time code is run
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(5)
    turtle.right(180)
    turtle.up()

#draw sets 3 and 4 of medium circles   
turtle.goto(-275,-48)#location of middle two rows

#repeats the drawing of seven circles for two rows of circles    
for i in range (2):
    turtle.color(random.choice(colors)) #random generation of colors every time code is run
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(5)
    turtle.right(180)
    turtle.up()
    
#draw last two sets of medium circles
turtle.goto(-270,-285)#location of last two rows

#repeats the drawing of seven circles for two rows of circles
for i in range (2):
    turtle.color(random.choice(colors)) #random generation of colors every time code is run
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.up()
    
###small circles   

turtle.up()
turtle.shape("turtle")
turtle.speed(10)

#draw first two sets of small circles 
turtle.goto(-280,220)#location of first two rows

#repeats the drawing of seven circles for two rows of circles
for i in range (2):
    turtle.color(random.choice(colors))#random generation of colors every time code is run
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(5)
    turtle.right(180)
    turtle.up()

#draw sets 3 and 4 of small circles   
turtle.goto(-275,-58) #location of middle two rows 

#repeats the drawing of seven circles for two rows of circles   
for i in range (2):
    turtle.color(random.choice(colors)) #random generation of colors every time code is run
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(5)
    turtle.right(180)
    turtle.up()
    
#draw last two sets of small circles
turtle.goto(-270,-295) #location of last two rows

#repeats the drawing of seven circles for two rows of circles
for i in range (2):
    turtle.color(random.choice(colors)) #random generation of colors every time code is run
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.forward(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
   
    
   
    





# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
# turtle.done()

