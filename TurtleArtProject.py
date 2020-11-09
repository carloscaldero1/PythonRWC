'''import turtle

screen = turtle.Screen()
t = turtle.Turtle()'''


#Shape Functions
#Actually did this part last
def drawSquare():
    import turtle
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.width(5)
    for i in range(4):
        t.fd(100)
        t.rt(90) #or t.fd(360/4)
    #screen.exitonclick()  #To exit turtle screen just click on it
def drawTriangle():
    import turtle
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.width(5)
    for i in range(3):
        t.fd(100)
        t.lt(120) #or t.fd(360/3)
    
def drawCircle():
    import turtle
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.width(5)
    t.circle(100)
    
def drawHexagon():
    import turtle
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.width(5)
    for i in range(6):
        t.fd(100)  
        t.rt(60) #or t.fd(360/6)
       
    
def drawOctagon():
    import turtle
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.width(5)
    for i in range(8):
        t.fd(100)  
        t.rt(45) #or t.fd(360/8)
     



shapeList = ['square', 'triangle', 'circle', 'hexagon','octagon']
print("I can draw shapes")
print("I can draw a square, a triangle, a circle, a hexagon, or an octagon")
print(" ")

while True:
    shapeEntered = input("What shape would you like to see? (must be all lowercase) ")
    if shapeEntered not in shapeList:
        print("You entered an invalid shape or mispelled, do not forget it has to be all lowercase")
        print(" ")
        continue
    else:
        print("Open Turtle Window to view drawing")
        break
if shapeEntered == 'square':
    drawSquare()
    #print("square") #for testing purposes before actually defining functions
elif shapeEntered == 'triangle':
    drawTriangle()
    '''import turtle
    screen = turtle.Screen()  #Could also put turtle inside function!! Will pop up in window when conditional above is true
    t = turtle.Turtle()'''
    #print("triangle") #for testing purposes before actually defining functions
elif shapeEntered == 'circle':
    drawCircle()
    #print("circle") #for testing purposes before actually defining functions
elif shapeEntered == 'hexagon':
    drawHexagon()
    #print("Hexagon") #for testing purposes before actually defining functions
else:
    drawOctagon()
    #print("Octagon") #for testing purposes before actually defining functions
       










'''
t.pu()
t.goto(-200,200)
t.pd()

t.fillcolor("red") #To make turtle red
t.color("red") 
t.begin_fill()
for i in range(8):
    t.width(3)
    t.rt(45)
    t.fd(100)
t.begin_fill()
   

screen.exitonclick()  #To exit turtle screen just click on it



# Set the background color
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create our turtle
t = turtle.Turtle()
t.color("black")
t.shape("turtle")
'''
'''
t.pu()
t.lt(180)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.pd()
'''
'''
t.pu()
#t.goto(-200,200)
t.goto(-300,100)
t.pd()
for i in range(4):
    t.width(5)
    t.fd(300)
    t.rt(90)

t.lt(45)
t.fd(210)
t.rt(90)
t.fd(210)
t.rt(45)
t.fd(300)
'''








