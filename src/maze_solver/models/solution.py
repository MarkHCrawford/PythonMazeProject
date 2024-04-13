# models/solution.py

from dataclasses import dataclass

from maze_solver.models.role import Role
from maze_solver.models.square import Square

from typing import Iterator
from functools import reduce


@dataclass(frozen=True)
class Solution:
    squares: tuple[Square, ...]


    def __post_init__(self) -> None:
        assert self.squares[0].role is Role.ENTRANCE
        assert self.squares[-1].role is Role.EXIT
        reduce(validate_corridor, self.squares)

    # make iteration possible
    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    def __getitem__(self,index: int) -> Square:
        return self.squares[index]
    
    def __len__(self) -> int:
        return len(self.squares)
    
def validate_corridor (current: Square, following: Square) -> Square:
    '''
    Assert any is great in Python because you can take multiple conditions,
    and it will pass if any of them are true,
    as opposed to assert all
    '''
    assert any ([
        current.row == following.row,
        current.column == following.column
    ]), "ERROR: MUST BE IN SAME ROW OR COLUMN"
    return following