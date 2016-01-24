__author__ = 'nik'

import os
from time import sleep


class Universe:
    """
    a universe of 5*5 cells
    """
    check = []
    check.append([0, 0, 0, 0, 0])
    check.append([0, 0, 1, 0, 0])
    check.append([0, 0, 1, 0, 0])
    check.append([0, 0, 1, 0, 0])
    check.append([0, 0, 0, 0, 0])

    def __init__(self):

        self.universe = []

        for row in range(5):
            rand_x = []
            for col in range(5):
                new_cell = Cell(status=Universe.check[row][col], xpos=col, ypos=row)
                rand_x.append(new_cell)
                pass
            self.universe.append(rand_x)

    def print_universe(self):
        for row in self.universe:
            print ""
            for col in row:
                print col,


class Cell:
    def valid_neighbour(self,row, col):
        neighbours = []
        for (v, j) in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col), (row - 1, col - 1),
                       (row + 1, col + 1), (row - 1, col + 1),
                       (row + 1, col -1)]:
            if not (not (0 <= v <= 4) or not (0 <= j <= 4)):
                neighbours.append((v, j))
                pass
            pass
        return neighbours

    def __init__(self, status, xpos, ypos):
        self.status = status
        self.newstatus = status
        self.x = xpos
        self.y = ypos
        self.n = self.valid_neighbour(self.y, self.x)

    def __repr__(self):
        self.status = self.newstatus
        if self.status == 0:
            return "."
        else:
            return ">"

    def status_check(self, universe):
        score = 0
        for v, j in self.n:
            score += universe[v][j].status
            pass
        if self.status == 0 and score == 3:
            self.newstatus = 1
            pass
        if self.status == 1:
            if score == 2 or score == 3:
                self.newstatus = 1
                pass
            else:
                self.newstatus = 0


def nexit(x):
    x.print_universe()
    sleep(1)
    for row in x.universe:
        for col in row:
            col.status_check(x.universe)
if __name__ == "__main__":
    x = Universe()
    while True:
        nexit(x)
