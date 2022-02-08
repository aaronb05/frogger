import random
from turtle import Turtle

COLORS = ["red", "orange", "gold", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
DIFFICULTY = 50


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = 0.1

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(290, random.randint(-220, 225))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.speed *= 0.8

