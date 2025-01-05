import time
import turtle

import scoreboard
import snake
import food

WALL = 300, -300
turt = turtle.Turtle()
s = turtle.Screen()
s.tracer(0)
s.setup(width=600, height=600)
s.title("Snake Game")
s.bgcolor("black")

snake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()
game_on = True

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

while game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score.count_score()

    head_pos = snake.head.pos()

    if head_pos[0] > 280 or head_pos[0] < -290 or head_pos[1] > 280  or head_pos[1] < -290:
        game_on = False
        score.game_over()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            score.game_over()


s.exitonclick()
