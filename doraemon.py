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
    
    
    
if __name__=='__main__':
    screensize(800,600,"#f0f0f0")
    pensize(3)
    speed(9)
    Doraemon()
    ankle(100,-300)
    mainloop()
    
