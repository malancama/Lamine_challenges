"""
Control the movements of a basic robot
"""
import math

# Code

class Robot:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.init_pos = (pos_x, pos_y)
        self.moving = False

    def start(self):
        print("Robot started")
        self.moving = True

    def stop(self):
        print("Robot stopped")
        self.moving = False

    @property
    def position(self):
        return (self.pos_x, self.pos_y)
        
    def up(self, pas):
        self.pos_y += pas
        self.print_position()

    def right(self, pas):
        self.pos_x += pas
        self.print_position()

    def down(self, pas):
        self.pos_y -= pas
        self.print_position()

    def left(self, pas):
        self.pos_x -= pas
        self.print_position()

    def print_position(self):
        print(f"New position : {self.position}\n")

    @property
    def distance(self):
        return ((self.init_pos[0] - self.pos_x)**2 + \
                (self.init_pos[1] - self.pos_y)**2)**.5