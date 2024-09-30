from turtle import Turtle, Screen
import time
import random

class Snake:
    def __init__(self, number_segments):
        self.segments = []
        self.number_segments = number_segments
        self.pixel_size=20
        self.refresh_rate = 0.1
        self.head_color = "green"
        self.body_color = "white"
        self.score = 0
        self.head_position = (0,0)
        self.scoreboard = Turtle()
        self.walls = Turtle()
        self.scoreboard.up()
        self.screen_size={"x": 600, "y": 600}
        self.game_is_on = True

    def generate_screen(self):
        """Generates an screen where the game is located"""
        self.screen = Screen ()
        self.screen.setup(width=self.screen_size["x"], height = self.screen_size["y"],startx=400, starty=200)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkey(fun=self.move_up, key="Up")
        self.screen.onkey(fun=self.move_down, key="Down")
        self.screen.onkey(fun=self.move_left, key="Left")
        self.screen.onkey(fun=self.move_right, key="Right")

    def generate_food(self):
        x = random.randint(-14,14)*self.pixel_size
        y = random.randint(-14,14)*self.pixel_size
        self.food_position = (x, y)
        self.food = Turtle("square")
        self.food.color("red")
        self.food.penup()
        self.food.goto(self.food_position)
        self.food.speed(0)    
    
    def draw_walls(self):
        self.walls.color("white")
        self.walls.penup()
        self.walls.width(20)
        self.walls.setpos(-self.screen_size["x"]/2,self.screen_size["y"]/2)
        self.walls.pendown()
        self.walls.forward(self.screen_size["x"])
        self.walls.seth(270)
        self.walls.forward(self.screen_size["y"])
        self.walls.seth(180)
        self.walls.forward(self.screen_size["x"])
        self.walls.seth(90)
        self.walls.forward(self.screen_size["y"])
        self.wall_limit_x=abs((self.screen_size["x"])/2)
        self.wall_limit_y=abs((self.screen_size["y"])/2)
    
    def verify_hit_wall(self):
        print(f"positionx, wallx: {abs(self.head_position[0])}, {self.wall_limit_x}")
        print(f"positiony, wally: {abs(self.head_position[1])}, {self.wall_limit_y}")
        
        if abs(self.head_position[0]) >= self.wall_limit_x or abs(self.head_position[1]) >= self.wall_limit_y:
            self.update_score_board(message="Game Over, Wall Hit \n Final Score: ")
            self.game_is_on = False
        
    def verify_hit_body(self):
        for segment in self.segments[3:]: # removes the first segment which is the head, always head position in head position duh
            segment_position = self.update_segment_position(segment)
            if self.head_position == segment_position:
                self.update_score_board(message="Game Over, Tail hit :( \n Final Score: ")
                self.game_is_on = False
            
    def generate_snake(self):
        starting_position = [(-position*self.pixel_size, 0) for position in range(0,self.number_segments)]
        for position in starting_position:
            new_segment = Turtle("square")
            if position == (0,0):
                new_segment.color("green")
            else:
                new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def refresh_snake(self):
        snake_lenght=len(self.segments)
        for index in range(1,snake_lenght):
            new_snake_segment_pos = self.segments[-index-1].pos()
            self.segments[-index].setpos(new_snake_segment_pos)
        self.segments[0].forward(self.pixel_size)
        time.sleep(self.refresh_rate)

    def add_snake_segment(self):
        self.segments[0].color(self.body_color)
        self.segments.insert(0,self.food)
        self.segments[0].color(self.head_color)
        self.segments[0].seth(self.segments[1].heading())
    
    def update_segment_position(self, segment):
        return (round(int(segment.xcor()),-1),round(int(segment.ycor()),-1))

    def update_head_position(self):
        self.head_position = self.update_segment_position(self.segments[0])

    def try_eat_food(self):
        if self.head_position == self.food_position:
            self.add_snake_segment()
            self.generate_food()
            self.score+=1
            self.update_score_board()
        self.refresh_snake()

    def move_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)

    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)

    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].seth(180)

    def move_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)
    
    def update_score_board(self, message="Score:"):
        self.scoreboard.setpos(0,260)
        self.scoreboard.pencolor("white")
        self.scoreboard.clear()
        self.scoreboard.down()
        self.scoreboard.write(f"{message} {self.score}", align='center')
        self.scoreboard.up()
        self.scoreboard.hideturtle()
        
    def game_on(self):
        while self.game_is_on:
            self.screen.update()
            self.update_head_position()
            self.try_eat_food()
            self.verify_hit_wall()
            self.verify_hit_body()
