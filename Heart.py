import turtle  
from math import pi , cos , sin 

window = turtle.Screen()   

def draw_heart(w ,h, iteration = 0) :        
    color = ['#c00000' , '#ff3334'  , '#ff6f76' ]    

    if iteration  == 3 : 
        return 
    t = turtle.Turtle()        
    t.hideturtle()
    t.pensize(2.5)  
    a = 0   
    t.up()  
    t.fillcolor(color[iteration] ) 
    t.begin_fill()  
    while a < 2 * pi :       
        x = (16  * sin(a) ** 3  ) * w  
        y = (13 * cos(a)-5*cos(2*a) - 2* cos(3*a) - 2*cos(3*a) - cos(4 * a )) * h 
        t.goto(x,y)    
        a+=0.02   
        t.down()     
    t.end_fill() 
    
    draw_heart(w - 3 , h - 2   , iteration + 1  )        

    #draw text  
    t.up() 
    t.setpos(0,0)
    t.write("Happy Valentines <3 ",align = 'center'  ,font=("Verdana",21, "bold" )) 
    t.down() 

draw_heart(18, 15)
