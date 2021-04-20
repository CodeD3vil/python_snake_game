from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("background.gif")
screen.title("Snake Game")
screen.tracer(0)
screen.register_shape("apple.gif")
screen.register_shape("snake_head.gif")
screen.register_shape("snake_head_right.gif")
screen.register_shape("snake_head_up.gif")
screen.register_shape("snake_head_down.gif")
screen.register_shape("snake.gif")
screen.register_shape("try_again.gif")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

CURSOR_SIZE = 20
FONT_SIZE = 24
FONT = ('Lato', FONT_SIZE, 'bold')

button = Turtle()
button.hideturtle()
button.penup()
button.goto(0, 0)
button.showturtle()
button.write("Press 'Space' to start the game", align='center', font=FONT)


def snake_game():
    game_is_on = True
    button.clear()
    button.hideturtle()
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.new_food()
            snake.grow_snake()
            scoreboard.increase_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 230 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()


def start_game():
    screen.onkey(snake_game, "space")
    button.onclick(snake_game)


start_game()
screen.mainloop()
