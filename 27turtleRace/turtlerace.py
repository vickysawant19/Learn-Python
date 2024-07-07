import turtle
import time

import random


WIDTH =500
HEIGHT =500
COLORS = ['red', 'green', 'blue', 'orange','yellow','black','purple','pink','brown','cyan']


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")


def get_number_of_turtle():
    turtle_number = 0
    while True:
        turtle_number = input(f"Enter the number of Turtle you want to race ( 2 - 10 ): ")

        if turtle_number.isdigit():
            turtle_number = int(turtle_number)
        else:
            print("Input in not numeric ---- Try again!")
            continue

        if 2<= turtle_number <= 10:
            return turtle_number
        else:
            print("Number not in range 2-10. try again")


    
def create_turtle(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        #set postion 
        racer.setpos(-WIDTH//2 + (i+1) * spacing,-HEIGHT//2 +20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = create_turtle(colors)
    while True:
        for turtle in turtles:
            distance = random.randrange(1,10)
            turtle.forward(distance)
            x,y = turtle.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(turtle)]



def main():
    turtle_number = get_number_of_turtle()
    print(turtle_number)
    init_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:turtle_number]
    winner = race(colors)
    print(f"winner is {winner}")

    

    

main()