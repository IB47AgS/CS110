"""
Emma Liao
Project 5_Refactored Turtle Scene

In this improved version of my Project 4, I made the code better by: breaking up the large main function into smaller functions, makes the code easier to read and change. 
Creating reusable functions for things that appear multiple times, like clouds and trees.
Using what we learned in class about making code more organized.
This refactoring did not add new features but made the codebase more organized and easier to understand.
"""

import turtle

def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def draw_triangle(t, x, y, size):
    jump_to(t, x, y)
    t.fillcolor("limegreen")
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.right(120)
    t.end_fill()

def draw_mountain(t, x, y, size):
    jump_to(t, x, y)
    t.fillcolor("grey")
    t.begin_fill()
    t.goto(x + size / 2, y + size)
    t.goto(x + size, y)
    t.goto(x, y)
    t.end_fill()

def draw_sun(t, x, y, radius):
    jump_to(t, x, y)
    t.fillcolor("gold")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_cloud(t, x, y):
    for i in range(4):
        jump_to(t, x + i * 30, y)
        t.fillcolor("white")
        t.begin_fill()
        t.circle(25)
        t.end_fill()
    
def draw_multiple_clouds(t, positions):
    for x, y in positions:
        draw_cloud(t, x, y)

def draw_tree(t, x, y):
    jump_to(t, x, y)
    t.fillcolor("saddlebrown")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()

    jump_to(t, x - 10, y + 50)
    t.fillcolor("forestgreen")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def draw_multiple_trees(t, positions):
    for x, y in positions:
        draw_tree(t, x, y)

def draw_wavy_river(t, x, y, wave_radius, num_waves):
    jump_to(t, x, y)
    t.setheading(0)
    t.fillcolor("deepskyblue")
    t.begin_fill()

    for _ in range(num_waves):
        t.circle(wave_radius, 62)   
        t.circle(-wave_radius, 62)  

    t.right(90)
    t.forward(40)

    for _ in range(num_waves):
        t.circle(-wave_radius, 78)
        t.circle(wave_radius, 78)

    t.right(90)
    t.forward(40)

    t.end_fill()


def draw_background(t):
    t.screen.bgcolor("skyblue")
    draw_sun(t, 200, 180, 40)
def draw_houses(t):
    draw_triangle(t, 80, -62, 60)
    draw_triangle(t, -45, -55, 50)
def draw_mountains(t):
    draw_mountain(t, -240, -120, 280)
    draw_mountain(t, -50, -90, 240)
    draw_mountain(t, 100, -100, 260)


def draw_scene(t):
    draw_background(t)

    cloud_positions = [(-200, 180), (20, 200)]
    draw_multiple_clouds(t, cloud_positions)

    draw_mountains(t)

    draw_wavy_river(t, -400, -250, 22, 8)

    tree_positions = [(-180, -80), (-60, -90), (60, -90)]
    draw_multiple_trees(t, tree_positions)

    draw_houses(t)

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    draw_scene(t)
    screen.mainloop()

if __name__ == '__main__':
    main()