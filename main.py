from turtle import Turtle, Screen
import time
import random
from snake import Snake

snake = Snake(3)
snake.generate_screen()
snake.generate_snake()
snake.update_score_board()
snake.draw_walls()
food = snake.generate_food()
snake.screen.update()

snake.game_on()

##segment_1 = Turtle("square")
##segment_1.color("white")
##
##segment_2 = Turtle("square")
##segment_2.color("white")
##segment_2.goto(-20,0)
##
##segment_3 = Turtle("square")
##segment_3.color("white")
##segment_3.goto(-40,0)
#

snake.screen.exitonclick()