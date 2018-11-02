from dataclasses import dataclass, field
from functools import reduce
from typing import Dict, Callable, List


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
class CharacterCanvas:
    symbol: str = '*'
    filler: str = ' '
    position: Point = Point()
    contextual_symbol: str = '*'

    content: Dict[Point, str] = field(default_factory=dict)
    symbol_stack: List[str] = field(default_factory=list)

    def transform(self, amount, transformation: Callable[[Point], Point]):
        for _ in range(int(amount)):
            self.content[self.position] = self.symbol
            self.position = transformation(self.position)

        self.content[self.position] = self.symbol

    def __lt__(self, other):
        self.transform(other, lambda point: Point(point.x - 1, point.y))

    def __gt__(self, other):
        self.transform(other, lambda point: Point(point.x + 1, point.y))

    def __xor__(self, other):
        self.transform(other, lambda point: Point(point.x, point.y + 1))

    def __floordiv__(self, other):
        self.transform(other, lambda point: Point(point.x, point.y - 1))

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

    def __call__(self, contextual_symbol):
        self.contextual_symbol = contextual_symbol
        return self

    def __enter__(self):
        self.symbol_stack.append(self.symbol)
        self.symbol = self.contextual_symbol

    def __exit__(self, *args):
        self.symbol = self.symbol_stack.pop()


p = CharacterCanvas('🙂', '  ')

letter_height = 21
letter_width = letter_height / 2


def space():
    p > 1
    with p('  '):
        p > letter_width / 2


def reset_height():
    with p(' '):
        p ^ letter_height


def h():
    p // letter_height
    p ^ (letter_height / 2)

    with p('🦄'):
        p > letter_width

    p // (letter_height / 2)
    p ^ letter_height


def i():
    p > letter_width / 2
    p < letter_width / 4

    with p('😛'):
        p // letter_height

    p < letter_width / 4
    p > letter_width / 2 + 1

    reset_height()


h()
space()
i()

print(p)
