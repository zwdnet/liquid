# -*- coding:utf-8 -*-
#具体的模拟程序
import particle
import numpy as np

def __init__():
    pass


class Stimulator():
    def __init__(self, N):
        self.N = N
        self.h = 2.0
        # self.Points = [[0 for x in range(N)] for y in range(N)]
        # for i in range(self.N//2):
        #     for j in range(self.N//2):
        #         self.Points[i][j] = 1
        self.particles = particle.Particles(N//2, N//2, self.N, self.h)

    def step(self):
        self.particles.compute_D()
        self.particles.compute_P()
        self.particles.compute_Vi()
        self.particles.compute_Acc()
        self.particles.compute_V()
        self.particles.compute_position()
        return self.particles.get_Particles()
