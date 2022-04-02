# clock module
import turtle as t

hours = 4
minutes = 45
seconds = 5

def printTime():
    print( f"{hours:02}:{minutes:02}:{seconds:02}" )


# draw clock with turtle
def drawClock():
    t.pensize(10)               # draw circle
    t.pencolor("black")
    t.circle(100)               # radius circle 100 pix
    t.left(90)
    t.penup()
    t.forward(100)

def drawHoursClock():           # pen for hours
    t.pendown()                 
    t.pensize(6)
    t.pencolor("violet")
    t.right(hours * 30)
    t.forward(70)

    t.penup()                   # pen reset
    t.right(180)
    t.forward(70)
def drawMinutes():
    t.pendown()             # pen minutes
    t.pensize(4)
    t.pencolor("red")
    t.right(180 - hours * 30)
    t.right(minutes * 6)
    t.forward(90)

    t.penup()                   # pen reset for sec.
    t.right(180)
    t.forward(90)

def drawSeconds():
    t.pendown()
    t.right(180 - minutes * 6)  #pen for sec.
    t.pensize(3)
    t.pencolor("blue")
    t.right(seconds * 6)
    t.forward(85)



    input("Hit enter to exit")
