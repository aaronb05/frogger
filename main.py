
import time
from turtle import Screen
import player as p
import car_manager as c
import scoreboard as s

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = p.Player()
score = s.Scoreboard()
car = c.CarManager()

screen.listen()
screen.onkeypress(player.move_forward, "Up")
screen.onkeypress(player.move_backward, "Down")

playing = True
while playing:
    time.sleep(car.speed)
    screen.update()
    car.create_car()
    car.move_car()
    # determine if car hits player
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            score.game_over()
            playing = False
    # determine if player crosses finish line/add to score and speed up cars
    if player.ycor() > 280:
        player.cross_finish_line()
        score.keep_score()
        car.speed_up()

screen.exitonclick()

