import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ('Arial', 20, 'bold')
grit_size = 8
turtle_list = []
score = 0
game_over = False

score_turtle = turtle.Turtle()
coundown_turtle = turtle.Turtle()

x_coordinates = [-40,-20, 0, 20, 40]
y_coordinates = [30, 10, -10, -30]

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("Dark Blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    score_turtle.setposition(0, y)
    score_turtle.write("Score: 0", move=False, align="center", font=FONT)

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", move=False, align="center", font=FONT)

        #print(x, y)

    t.onclick(handle_click)
    t.penup()
    t.shape('turtle')
    t.shapesize(2)
    t.color("dark green")
    t.goto(x * grit_size, y * grit_size)
    turtle_list.append(t)

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    coundown_turtle.hideturtle()
    coundown_turtle.color("Black")
    coundown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    coundown_turtle.setposition(0, y - 30)
    coundown_turtle.clear()

    if time > 0:
        coundown_turtle.clear()
        coundown_turtle.write(f"Time = {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        coundown_turtle.clear()
        hide_turtles()
        coundown_turtle.write(f"Game Over!!!", move=False, align="center", font=FONT)

def start():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)

start()
turtle.mainloop()
