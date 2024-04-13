# persistence/file_format.py

'''
To more easily represent the maze, let's use a byte.
The entire data for each string can be represented by a byte.
We will do some bitwise operations to shift the bits
so that the role and the borders can be represented.
Let's start by creating magic numbers.
Magic numbers are what help identify unique file types.
'''

from dataclasses import dataclass

import struct
from typing import BinaryIO
import array

MAGIC_NUMBER: bytes = b"MAZE"

# [77, 65, 90, 69]


@dataclass(frozen=True)
class FileHeader:
    format_version: int
    width: int
    height: int

# when there is no instance, we can use class methods
# to act on a class instead of an object

    @classmethod
    def read(cls, file:BinaryIO) -> "FileHeader":
        assert (
            file.read(len(MAGIC_NUMBER)) == MAGIC_NUMBER
        ), "FILE TYPE UNKNOWN"
        format_version, = struct.unpack("B", file.read(1))
        width, height = struct.unpack("<2I", file.read(2*4))
        return cls(format_version, width, height)

    def write(self, file:BinaryIO) -> None:
        file.write(MAGIC_NUMBER)
        file.write(struct.pack("B", self.format_version))
        file.write(struct.pack("<2I", self.width, self.height))

@dataclass(frozen=True)
class FileBody:
    square_values: array.array

    @classmethod
    def read(cls, header: FileHeader, file: BinaryIO) -> "FileBody":
        return cls(
            array.array("B", file.read(header.width * header.height))
        )
    
    def write(self, file: BinaryIO) -> None:
        file.write(self.square_values.tobytes())