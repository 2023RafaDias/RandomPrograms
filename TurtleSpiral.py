import turtle
screen = turtle.Screen()
spiral = turtle.Turtle()
screen.bgcolor("black")
screen.setup(800,800)
spiral.speed(10)
col = ["yellow","blue","white","green"]
c = 0
for i in range(50):
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(col[c])
    if c ==3:
        c = 0
    else:
        c+=1
