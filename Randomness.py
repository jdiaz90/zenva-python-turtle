from random import *
from turtle import *

random_num = randrange(1, 100)
print(random_num)

forward(randrange(20, 100))
right(randrange(0, 360))
forward(randrange(20, 100))

# if you are using a local environment such as
# Visual Studio Code, add "done()" at the end
# to prevent the output window from closing 
done()