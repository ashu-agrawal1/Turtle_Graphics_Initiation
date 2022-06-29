import turtle

window = turtle.Screen( )
window.bgcolor("BLACK")
#Create the turtle with name rob
rob = turtle.Turtle()
rob.shape("turtle")
rob.color ("RED")
x=0
colors= ['yellow','purple','cyan','red','orange','pink','light green']
for i in range(1,200):
		x+=1.5
		rob.forward(100+x)
		rob.color(colors[i%7])
		rob.left(88)
turtle.done()