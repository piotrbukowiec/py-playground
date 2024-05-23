from dataclasses import dataclass


@dataclass
class ScreenDimensions:
    width: int
    height: int

    def __iter__(self):
        yield self.width
        yield self.height
