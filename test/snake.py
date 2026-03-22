import turtle
import time
import random

WIDTH, HEIGHT = 600, 600
MOVE_SPEED = 0.1

screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("贪吃蛇（Snake）")
screen.bgcolor("black")
screen.tracer(0)

snake = [turtle.Turtle(shape="square") for _ in range(3)]
for i, segment in enumerate(snake):
    segment.penup()
    segment.color("green")
    segment.goto(-20 * i, 0)

food = turtle.Turtle(shape="circle")
food.color("red")
food.penup()
food.goto(100, 0)

score = 0
high_score = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, HEIGHT // 2 - 40)
pen.write(f"得分: {score}  最高分: {high_score}", align="center", font=("Arial", 16, "normal"))

direction = "right"


def set_direction(new_dir):
    global direction
    opposite = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if new_dir != opposite.get(direction):
        direction = new_dir


def move_snake():
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)

    head = snake[0]
    if direction == "up":
        head.sety(head.ycor() + 20)
    elif direction == "down":
        head.sety(head.ycor() - 20)
    elif direction == "left":
        head.setx(head.xcor() - 20)
    elif direction == "right":
        head.setx(head.xcor() + 20)


screen.listen()
screen.onkey(lambda: set_direction("up"), "Up")
screen.onkey(lambda: set_direction("down"), "Down")
screen.onkey(lambda: set_direction("left"), "Left")
screen.onkey(lambda: set_direction("right"), "Right")


def reset_game():
    global score, direction
    for segment in snake:
        segment.goto(1000, 1000)
    snake.clear()
    for _ in range(3):
        segment = turtle.Turtle(shape="square")
        segment.penup()
        segment.color("green")
        snake.append(segment)
    for i, segment in enumerate(snake):
        segment.goto(-20 * i, 0)
    direction = "right"
    score = 0


def update_score():
    pen.clear()
    pen.write(f"得分: {score}  最高分: {high_score}", align="center", font=("Arial", 16, "normal"))


while True:
    screen.update()
    move_snake()

    head = snake[0]
    if head.distance(food) < 15:
        food.goto(random.randint(-WIDTH//2 + 20, WIDTH//2 - 20) // 20 * 20,
                  random.randint(-HEIGHT//2 + 20, HEIGHT//2 - 20) // 20 * 20)
        new_segment = turtle.Turtle(shape="square")
        new_segment.penup()
        new_segment.color("green")
        snake.append(new_segment)
        score += 10
        high_score = max(high_score, score)
        update_score()

    if head.xcor() > WIDTH // 2 - 10 or head.xcor() < -WIDTH // 2 + 10 or head.ycor() > HEIGHT // 2 - 10 or head.ycor() < -HEIGHT // 2 + 10:
        reset_game()
        update_score()

    for segment in snake[1:]:
        if head.distance(segment) < 10:
            reset_game()
            update_score()
            break

    time.sleep(MOVE_SPEED)

screen.mainloop()
