"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi


__author__ = ""  # TODO


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        return "black"


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float):
        """Initialize the cells with random locations and directions."""
        self.population = []
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1

    def random_location(self) -> Point:
        """Generate a random location."""
        # TODO
        return Point(0.0, 0.0)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        # TODO
        return Point(0.0, 0.0)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        ...

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False