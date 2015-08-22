# -*- coding:utf-8 -*-
#具体的模拟程序
def __init__():
    pass


class Stimulator():
    def __init__(self, N):
        self.N = N
        self.Points = [[0 for x in range(N)] for y in range(N)]
        for i in range(self.N//2):
            for j in range(self.N//2):
                self.Points[i][j] = 1

    def step(self):
        return self.Points
