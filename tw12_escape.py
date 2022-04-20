


from math import pi, sqrt
from turtle import Turtle
import math
import random

"""
Write a class Escape which will simulate a person randomly walking
from the center until they get to a certain distance, r, from the origin.

"""


class Escape(object):
    
    def __init__(self, radius):
        self.turtle = Turtle()
        self.radius = radius
        
        
        
    def fence(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.setposition(0, (0-self.radius))                               
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.color('black')
        self.turtle.circle(self.radius)
        
    def capture(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.setposition(0,0) 
    
    def escape(self):
        while sqrt(((abs(self.turtle.xcor())**2) + (abs(self.turtle.ycor())**2))) < self.radius: # Pythagorean Theorem
            self.turtle.pendown()
            self.turtle.begin_fill()
            self.turtle.color('blue')
            self.turtle.right((random.randint(0,360))) #turn the walker to the right a random amount
            self.turtle.forward(30)
            


        