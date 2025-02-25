import turtle
import random


win = turtle.Screen()
win.title("Giigle Vigilant")
win.bgcolor("black")
win.setup(width=600, height=800)
win.tracer(0)

#Score

def update_score():
    score_display.clear()
    score_display.write("Score: {}".format(score), align = "left",font=("Courier", 12, "normal"))
    
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-290, 260)
update_score()

#Player 

player = turtle.Turtle()
player.shape("turtle")
player.color("orange")
player.penup()
player.speed(0)
player.goto(0, -250)
player.setheading(90)
player_speed = 30
bullet_speed = 1

def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -290:
        x = -290
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 290:
        x = 290
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state== "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

#Controls

win.listen()
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")
win.onkey(fire_bullet, "space")

#Player guns

bullet = turtle.Turtle()
bullet.shape("circle")
bullet.color("yellow")
bullet.penup()
bullet.speed(10)
bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
bullet.hideturtle()
bullet_state ="ready"

#Invanders

num_invaders = 5
invaders = []
for _ in range(num_invaders):
    invader = turtle.Turtle()
    invader.shape("square")
    invader.color("red")
    invader.penup()
    invader.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(100, 250)
    invader.goto(x,y)
    invaders.append(invader)
invader_speed = 2

#Invaders movement

def move_invaders():
    for invader in invaders:
        y = invader.ycor()
        y -= invader_speed
        invader.sety(y)
        if player.distance(invader)<20:
            player.hideturtle()
            invader.hideturtle()
            print("GAME OVER!!!")
            win.bye()
        if y < -290:
            player.hideturtle()
            invader.hideturtle()
            print("GAME OVER!!!")
            win.bye()
    win.update()
    win.ontimer(move_invaders, 100)
    
move_invaders()

while True:
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)
        #Check hit on invader 
        for invader in invaders:
            if bullet.distance(invader) < 15:
                bullet.hideturtle()
                bullet_state = "ready"
                x = random.randint(-290, 290)
                y = random.randint(100,250)
                invader.goto(x,y)
                score = +10
            if y >290:
                bullet.hideturtle()
                bullet_state = "ready"
    win.update()
