# models/maze.py

from dataclasses import dataclass
from functools import cached_property
from typing import Iterator

from maze_solver.models.role import Role
from maze_solver.models.square import Square

# frozen = true makes the class immutable
@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...]
# the ... in the tuple[square, ...] means that the tuple can have any number of squares
# mazes can now be defined as a tuple of squares

# To cache things later, a tuple is required instead of a list, because of its immutability

# validation after initialization
    def __post_init__(self) -> None:
        validate_indices(self)
        validate_rows_columns(self)
        validate_entrance(self)
        validate_exit(self)

# so we can use a for loop
    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)
    
# so we can use [i] indexing
    def __getitem__(self, index: int) -> Square:
        return self.squares[index]

# iterate over indices to get width    
    @cached_property
    def width(self):
        return max(square.column for square in self) + 1

# iterate over indices to get height    
    @cached_property
    def height(self):
        return max(square.row for square in self) + 1
    
    
# both return next on generator expression, filtering squares by role
# entrace cached
    @cached_property
    def entrance(self) -> Square:
        return next(square for square in self if square.role is Role.ENTRANCE)

# exit cached
    @cached_property
    def exit(self) -> Square:
        return next(square for square in self if square.role is Role.EXIT)

# validation functions
def validate_indices(maze: Maze) -> None:
    assert [square.index for square in maze] == list(
        range(len(maze.squares))
    ), "square.index is incorrect"

def validate_rows_columns(maze: Maze) -> None:
    for y in range(maze.height):
        for x in range(maze.width):
            square = maze[y * maze.width + x]
            assert square.row == y, "square.row incorrect"
            assert square.column == x, "square.column incorrect"

def validate_entrance(maze: Maze) -> None:
    assert 1  == sum(
        1 for square in maze if square.role is Role.ENTRANCE
    ), "Only one entrance allowed"

def validate_exit(maze: Maze) -> None:
    assert 1 == sum(
        1 for square in maze if square.role is Role.EXIT
    ), "Only one exit allowed"