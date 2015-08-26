# -*- coding:utf-8 -*-
#具体的模拟程序
import particle

def __init__():
    pass


class Stimulator():
    def __init__(self, N):
        self.N = N
        # self.Points = [[0 for x in range(N)] for y in range(N)]
        # for i in range(self.N//2):
        #     for j in range(self.N//2):
        #         self.Points[i][j] = 1
        self.particles = particle.Particles(N//2, N//2)

    def step(self):
        # points = self.particles.get_Particles()
        # newpoints = []
        # for i in range(len(points)):
        #     newpoints.append((points[i][0], points[i][1]+1))
        # self.particles.set_Particles(newpoints)
        self.particles.step_Points()
        self.particles.step_V()
        self.particles.step_pressure()
        return self.particles.get_Particles()
