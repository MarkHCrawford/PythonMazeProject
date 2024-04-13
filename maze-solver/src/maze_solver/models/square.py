# models/square.py


# Import from border and role classes
from dataclasses import dataclass

from maze_solver.models.border import Border
from maze_solver.models.role import Role

# Defining a square


# Note that dataclass is just a simple way of doing a class definition.

@dataclass(frozen = True)
class Square:
    index: int
    row: int
    column: int
    border: Border
    role: Role = Role.NONE

'''
Now a square class can be created like:
Square(1, 0, 0, Border.TOP | Border.LEFT, Role.START)
'''