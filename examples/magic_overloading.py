from dataclasses import dataclass, field
from functools import reduce
from typing import Dict, Callable

from functional import seq


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0


def apply_function_on_coordinates(p1, p2, fun):  # todo names
    return Point(fun(p1.x, p2.x), fun(p1.y, p2.y))


def coord_min(p1, p2):  # todo names
    return apply_function_on_coordinates(p1, p2, min)


def coord_max(p1, p2):  # todo names
    return apply_function_on_coordinates(p1, p2, max)


@dataclass
class AsciiPaint:
    position: Point = Point()
    symbol: str = '*'
    filler: str = ' '
    content: Dict[Point, str] = field(default_factory=dict)

    def transform(self, amount, transformation: Callable[[Point, int], Point]):
        for i in range(1, amount + 1):
            self.content[transformation(self.position, i)] = self.symbol

        self.position = transformation(self.position, amount)

    def __lt__(self, other: int):
        for dec in range(1, other + 1):
            self.content[Point(self.position.x - dec, self.position.y)] = self.symbol

        self.position = Point(self.position.x - other, self.position.y)

    def __gt__(self, other):
        return self.transform(other, lambda point, amount: Point(point.x + amount, point.y))

    def __xor__(self, other: int):
        for inc in range(1, other + 1):
            self.content[Point(self.position.x, self.position.y + inc)] = self.symbol

        self.position = Point(self.position.x, self.position.y + other)

    def __floordiv__(self, other):
        pass

    def __repr__(self):
        lower_left, higher_right = self.get_display_rectangle()

        # seq(zip(range(lower_left.x, higher_right.x + 1)), range(higher_right.y, lower_left.y - 1, -1)) \
        #     .map(lambda coord: Point(*coord)) \
        #     .map(lambda point: self.content.get(point, self.filler))

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
        return reduce(coord_min, self.content.keys()), \
               reduce(coord_max, self.content.keys())


p = AsciiPaint()

p < 5
p ^ 7
p > 8
# p // 7
print(p)
