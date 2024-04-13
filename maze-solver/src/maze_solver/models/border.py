# models/border.py

from enum import IntFlag, auto

class Border(IntFlag):
    EMPTY = 0 
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()


    '''
    Defining borders:
       0001 = TOP
       0010 = BOTTOM
       0100 = LEFT
       1000 = RIGHT
       This is an enum with flags.
       With flags means they can be combined.
       0101 = TOP | LEFT = TOP and LEFT
       A cell with all borders closed is 1111 = 15 = TOP | BOTTOM | LEFT | RIGHT
    '''


# This allows it to easily be determined if a cell is a corner
    @property
    def corner(self) -> bool:
        return self in (
            self.TOP | self.LEFT,
            self.TOP | self.RIGHT,
            self.BOTTOM | self.LEFT,
            self.BOTTOM | self.RIGHT
        )
# Likewise for deadends and intersections

    @property
    def dead_end(self) -> bool:
        return self.bit_count() == 3   

    @property
    def intersection(self) -> bool:
        return self.bit_count() < 2