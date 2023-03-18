from dataclasses import dataclass, astuple
from itertools import product
from copy import deepcopy


@dataclass
class Square:
    x: int
    y: int
    size: int


class Table:
    def __init__(self, n: int):
        self.n = n
        self.matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        self.squares = []
        self.solution = []

    def __str__(self) -> str:
        return '\n'.join([str(x) for x in self.matrix])

    def place_square(self, square: Square) -> None:
        x, y, size = astuple(square)
        for i, j in product(range(size), range(size)):
            self.matrix[y + j][x + i] = 1
        self.squares.append(square)

    def del_top_square(self) -> None:
        square = self.squares.pop()
        for i, j in product(range(square.size), range(square.size)):
            self.matrix[square.y + j][square.x + i] = 0

    def free_cell(self) -> None | tuple[int, int]:
        for y, x in product(range(self.n // 2 + 1, self.n + 1), range(self.n // 2 + 1, self.n + 1)):
            if self.matrix[y][x] == 0:
                return y, x

    def check_square(self, square: Square) -> bool:
        x, y, size = astuple(square)
        if y + size - 1 > self.n or x + size - 1 > self.n:
            return False
        for i, j in product(range(size), range(size)):
            if self.matrix[y + j][x + i] == 1:
                return False
        return True

    def solve_prime(self) -> list[Square]:
        z = self.n // 2 + 1
        self.place_square(Square(1, 1, z))
        self.place_square(Square(1, z + 1, z - 1))
        self.place_square(Square(z + 1, 1, z - 1))
        stack = []
        y, x = self.free_cell()
        stack.append(Square(x, y, 1))
        while stack:
            if self.solution and len(self.squares) >= len(self.solution) - 1 or \
                    not self.solution and len(self.squares) > self.n:
                self.del_top_square()
                stack.pop()
                continue
            square = stack[len(stack) - 1]
            x, y, size = astuple(square)
            if self.check_square(square):
                self.place_square(square)
                try:
                    new_y, new_x = self.free_cell()
                except TypeError:
                    self.solution = deepcopy(self.squares)
                    self.del_top_square()
                    self.del_top_square()
                    stack.pop()
                    continue
                stack.pop()
                stack.append(Square(x, y, size + 1))
                stack.append(Square(new_x, new_y, 1))
                continue
            self.del_top_square()
            stack.pop()
        return self.solution

    def solve_other(self) -> list[Square]:
        if self.n % 2 == 0:
            self.place_square(Square(1, 1, n // 2))
            self.place_square(Square(1, n // 2 + 1, n // 2))
            self.place_square(Square(n // 2 + 1, 1, n // 2))
            self.place_square(Square(n // 2 + 1, n // 2 + 1, n // 2))
            return self.squares

        if self.n % 3 == 0:
            self.place_square(Square(1, 1, (n * 2) // 3))
            self.place_square(Square(1, (n * 2) // 3 + 1, n // 3))
            self.place_square(Square(n // 3 + 1, (n * 2) // 3 + 1, n // 3))
            self.place_square(Square((n * 2) // 3 + 1, (n * 2) // 3 + 1, n // 3))
            self.place_square(Square((n * 2) // 3 + 1, 1, n // 3))
            self.place_square(Square((n * 2) // 3 + 1, n // 3 + 1, n // 3))
            return self.squares

        if self.n % 5 == 0:
            self.place_square(Square(1, 1, (n * 3) // 5))
            self.place_square(Square(1, (n * 3) // 5 + 1, (n * 2) // 5))
            self.place_square(Square((n * 3) // 5 + 1, 1, (n * 2) // 5))
            self.place_square(Square((n * 3) // 5 + 1, (n * 3) // 5 + 1, (n * 2) // 5))
            self.place_square(Square((n * 2) // 5 + 1, (n * 3) // 5 + 1, n // 5))
            self.place_square(Square((n * 2) // 5 + 1, (n * 4) // 5 + 1, n // 5))
            self.place_square(Square((n * 3) // 5 + 1, (n * 2) // 5 + 1, n // 5))
            self.place_square(Square((n * 4) // 5 + 1, (n * 2) // 5 + 1, n // 5))
            return self.squares


if __name__ == "__main__":
    n = int(input())
    table = Table(n)
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        solution = table.solve_other()
    else:
        solution = table.solve_prime()
    print(len(solution))
    for x in solution:
        print(x.y, x.x, x.size)
