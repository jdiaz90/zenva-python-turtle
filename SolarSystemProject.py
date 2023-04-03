from turtle import *

# used to setup the screen for the live coding
Screen().setup(800, 500)

# set speed to 0 so the animation is instant
speed(0)

# set the background color to BLACK
Screen().bgcolor("black")

# create the ORANGE planet
color("orange")
begin_fill()
circle(60)
end_fill()

# move forwards
penup()
forward(100)
pendown()

# create the GREY planet
color("grey")
begin_fill()
circle(20)
end_fill()

# move forwards
penup()
forward(80)
pendown()

# create the RED planet
color("red")
begin_fill()
circle(40)
end_fill()

# move forwards
penup()
forward(90)
pendown()

# create the GREEN planet
color("green")
begin_fill()
circle(30)
end_fill()

# if you are using a local environment such as
# Visual Studio Code, add "done()" at the end
# to prevent the output window from closing 
done()