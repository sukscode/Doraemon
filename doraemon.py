from textwrap import fill
from turtle import *
def ankle(x,y):
    penup()
    goto(x,y)
    pendown()
    
def eyes():
    fillcolor("#ffffff")
    begin_fill()
    
    tracer(False)
    a=2.5
    for i in range (120):
        if 0 <= i < 30 or 60 <= i <90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()  
  
def daari():
    ankle(-32,135)
    seth(165)
    fd(60)
    
    ankle(-32,125)
    seth(180)
    fd(60)
    
    ankle(-32,115)
    seth(193)
    fd(60)

    ankle(37,135)
    seth(0)
    fd(60)
    
    
    ankle(37,125)
    seth(0)
    fd(60)
    
    ankle(37,115)
    seth(-13)
    fd(60)
    
def mukh():
    ankle(5,148)
    seth(270)
    fd(100)
    seth(0)
    circle(120,50)
    seth(230)
    circle(-120,100)

def scarf():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5,90)
    fd(10)
    circle(-5,90)
    fd(207)
    circle(-5,90)
    fd(10)
    circle(-5,90)
    end_fill()
    
def nose():
    ankle(-10,158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()
    
def black_eyes():
    seth(0)
    ankle(-20,195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()
    
    pensize(6)
    ankle(20,205)
    seth(75)
    circle(-10,150)
    pensize(3)
    
    ankle(-17,200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    ankle(0,0)
    
def face():
    fd(183)
    lt(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120,100)
    seth(180)
    #print(pos())
    fd(121)
    pendown()
    seth(215)
    circle(120,100)
    end_fill()
    ankle(63.56,218.24)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)


    
    
        
if __name__=='__main__':
    screensize(800,600,"#f0f0f0")
    pensize(3)
    speed(9)
    Doraemon()
    ankle(100,-300)
    mainloop()
    
