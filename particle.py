# -*- coding:utf-8 -*-
#粒子类
import math


def __init__():
    pass

class Particles():
    def __init__(self, Nx, Ny):
        #设置质点数量
        self.N = Nx * Ny
        self.Nx = Nx
        self.Ny = Ny
        #创建质点
        self.Points = []
        for i in range(self.Nx):
            for j in range(self.Ny):
                point = [i*2, j*2]
                self.Points.append(point)
        #创建速度向量
        self.V = []
        for i in range(self.N):
            self.V.append([0, 0])
        #创建质量
        self.M = []
        for i in range(self.N):
            self.M.append(1.0)
        #创建密度
        self.D = []
        for i in range(self.N):
            self.D.append(1.0)
        #创建压强
        self.P = []
        for i in range(self.N):
            self.P.append(1.0)
        #创建外力（只考虑重力)
        self.G = 9.8   #重力加速度
        self.F = []
        for i in range(self.N):
            self.F.append([0.0, self.M[i] * self.G])
        #创建加速度
        self.Acc = []
        for i in range(self.N):
            self.Acc.append([0.0, self.G])

    #对每个粒子的速度进行迭代
    def step_V(self):
        for i in range(self.N):
            self.V[i][0] += self.Acc[i][0]
            self.V[i][1] += self.Acc[i][1]

    #对每个粒子的位移进行迭代，要处理撞墙的问题，先不管粒子间碰撞
    def step_Points(self):
        for i in range(self.N):
            #公式:s = vot + 1/2*a*t**2
            self.Points[i][0] += self.V[i][0] + 0.5 * self.Acc[i][0]
            self.Points[i][1] += self.V[i][1] + 0.5 * self.Acc[i][1]
            if self.Points[i][0] < 0:
                self.Points[i][0] = 0
                self.V[i][0] *= -1
            if self.Points[i][0] >= 600:
                self.Points[i][0] = 599
                self.V[i][0] *= -1
            if self.Points[i][1] < 0:
                self.Points[i][1] = 0
                self.V[i][1] *= -1
            if self.Points[i][1] >= 600:
                self.Points[i][1] = 599
                self.V[i][1] *= -1

    def get_Particles(self):
        return self.Points

    def set_Particles(self, Points):
        self.Points = Points

    #计算粒子的压强
    def step_pressure(self):
        h = 2
        for i in range(self.N):
            self.P[i] = 0.0
            for j in range(self.N):
                if i == j:
                    continue
                d = math.sqrt((self.Points[i][0] - self.Points[j][0])**2 + \
                    (self.Points[i][1] - self.Points[j][1])**2)
                if d < 2*h:
                    print(d)
                    wd = (1.0/(math.pi**(3.0/2.0))*(h**3))*math.exp(d**2/h**2)
                    print(wd)
                    self.P[i] += wd