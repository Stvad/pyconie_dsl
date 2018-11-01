from copy import copy
from dataclasses import dataclass, field
from functools import reduce
from typing import Dict, Callable


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0


def apply_function_on_coordinates(p1, p2, fun):
    return Point(fun(p1.x, p2.x), fun(p1.y, p2.y))


def coordinate_min(p1, p2):
    return apply_function_on_coordinates(p1, p2, min)


def coordinate_max(p1, p2):
    return apply_function_on_coordinates(p1, p2, max)


@dataclass
class AsciiCanvas:
    position: Point = Point()
    symbol: str = '*'
    filler: str = ' '
    content: Dict[Point, str] = field(default_factory=dict)

    def transform(self, amount, transformation: Callable[[Point, int], Point]):
        for i in range(1, amount + 1):
            self.content[transformation(self.position, i)] = self.symbol

        self.position = transformation(self.position, amount)

    def __lt__(self, other):
        self.transform(other, lambda point, amount: Point(point.x - amount, point.y))

    def __gt__(self, other):
        self.transform(other, lambda point, amount: Point(point.x + amount, point.y))

    def __xor__(self, other):
        self.transform(other, lambda point, amount: Point(point.x, point.y + amount))

    def __floordiv__(self, other):
        self.transform(other, lambda point, amount: Point(point.x, point.y - amount))

    def __repr__(self):
        lower_left, higher_right = self.get_display_rectangle()

        lines = []
        for y in range(higher_right.y, lower_left.y - 1, -1):
            lines.append(
                ''.join(
                    [self.content.get(Point(x, y), self.filler)
                     for x in range(lower_left.x, higher_right.x + 1)]
                )
            )

        return "\n".join(lines)

    def get_display_rectangle(self):
        return reduce(coordinate_min, self.content.keys()), \
               reduce(coordinate_max, self.content.keys())

    # def __call__(self, contextual_symbol):
    #     return AsciiCanvas(self.position, contextual_symbol, self.filler, self.content)
    #
    #
    # def __enter__(self):
    #     self.symbol = self.contextual_symbol


p = AsciiCanvas()

letter_height = 21
letter_width = letter_height  # makes sense because of the distance diff

p // letter_height
p ^ (letter_height // 2)

p > letter_width

p ^ (letter_height // 2)
p // letter_height

print(p)
