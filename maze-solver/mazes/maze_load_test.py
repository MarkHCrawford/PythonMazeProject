from pathlib import Path
from maze_solver.models.maze import Maze
from maze_solver.view.renderer import SVGRenderer



maze = Maze.load(Path("mazes") "labyrinth.maze")
SVGRenderer().render(maze).preview()