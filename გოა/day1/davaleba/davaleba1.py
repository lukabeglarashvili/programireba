from turtle import *

color("blue")
#we eant to paint a  house
speed(10)
#step 1:   draw a   spuare
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end  of  squore
#drowing a door
forward(70)
color("yellow")
begin_fill()
left(90)

forward(120)#height of door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
left (30)    
color ("purple")      
forward(70)     

#window
color("green")
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#window 2
penup()
goto (200, 125)
pendown()
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

exitonclick()