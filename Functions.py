from turtle import *

def say_hello (name):
  print("How are you " + name)

say_hello("Bob")
say_hello("Steve")
say_hello("Mary")
say_hello("Rob")

# using Turtle
def move_and_turn (distance, angle):
  forward(distance)
  right(angle)

move_and_turn(100, 45)
move_and_turn(50, 90)

# if you are using a local environment such as
# Visual Studio Code, add "done()" at the end
# to prevent the output window from closing 
done()