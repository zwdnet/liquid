# -*- coding:utf-8 -*-
#粒子类
import math
import numpy as np


def __init__():
    pass

class Particles():
    def __init__(self, Nx, Ny, N, h):
        #设置质点数量
        self.N = Nx * Ny
        self.Nx = Nx
        self.Ny = Ny
        self.Size = N
        self.h = h
        self.G = 9.8
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
        #创建密度
        self.D = []
        for i in range(self.N):
            self.D.append(1.0)
        #创建压强产生的加速度
        self.P = []
        for i in range(self.N):
            self.P.append([0.0, 0.0])
        #创建粘度产生的加速度
        self.Vi = []
        for i in range(self.N):
            self.Vi.append([1.0, 1.0])
        #创建加速度
        self.Acc = []
        for i in range(self.N):
            self.Acc.append([0.0, self.G])

    #寻找point点的邻居,返回neighbor_table中，寻找point周围的24个点（两圈）,N为区域最大值
    def find_neighbor(self, point):
        x = math.floor(point[0])
        y = math.floor(point[1])
        neighbor_table = []
        for i in range(x-2, x+3):
            for j in range(y-2, y+3):
                if i < 0 or i >= self.Size or j < 0 or j >= self.Size:
                    continue
                for k in range(len(self.Points)):
                    if self.Points[k][0] == i and self.Points[k][1] == j:
                        neighbor_table.append(k)
        return neighbor_table

    #计算流体密度
    def compute_D(self):
        w = 315.0/(64.0*np.pi*self.h**9)
        for i in range(self.N):
            sumD = 0.0
            neighbor_table = self.find_neighbor(self.Points[i])
            for j in range(len(neighbor_table)):
                rij = (self.Points[neighbor_table[j]][0] - self.Points[i][0])**2 + (self.Points[neighbor_table[j]][1] - self.Points[i][1])**2
                #rij = 1
                hr = (self.h**2 - rij)**3
                sumD += hr
            self.D[i] = w*sumD

    #计算压力产生的加速度
    def compute_P(self):
        w = 45.0/np.pi*self.h**6
        for i in range(self.N):
            sumPx = 0.0
            sumPy = 0.0
            neighbor_table = self.find_neighbor(self.Points[i])
            for j in range(len(neighbor_table)):
                Dij = (self.D[i]+self.D[j])/2*self.D[i]*self.D[j]
                r = np.sqrt(np.abs((self.Points[i][0] - self.Points[j][0])**2 - (self.Points[i][1] - self.Points[j][1])**2))
                hr = (self.h-r)*(self.h-r)
                rx = self.Points[i][0] - self.Points[j][0]
                ry = self.Points[i][1] - self.Points[j][1]
                # print(j, Dij, r, hr, rx, ry)
                if Dij == 0 or r == 0 or hr == 0 or rx == 0 or ry == 0:
                    continue
                sumPx += Dij*hr*(rx/r)
                sumPy += Dij*hr*(ry/r)
            self.P[i][0] = w*sumPx
            self.P[i][1] = w*sumPy

    def compute_Vi(self):
        w = 45.0/np.pi*self.h**6
        for i in range(self.N):
            sumVx = 0.0
            sumVy = 0.0
            neighbor_table = self.find_neighbor(self.Points[i])
            for j in range(len(neighbor_table)):
                if self.D[i] == 0 or self.D[j] == 0:
                    continue
                vdx = (self.V[j][0] - self.V[i][0])/self.D[i]*self.D[j]
                vdy = (self.V[j][1] - self.V[j][1])/self.D[i]*self.D[j]
                hrx = self.h - np.abs(self.Points[i][0] - self.Points[j][0])
                hry = self.h - np.abs(self.Points[i][1] - self.Points[j][1])
                sumVx += vdx*hrx
                sumVy += vdy*hry
            #     print (i, j, vdx, vdy, hrx, hry, sumVx, sumVy)
            # print(sumVx, sumVy)
            self.Vi[i][0] = w*sumVx
            self.Vi[i][1] = w*sumVy

    #计算加速度
    def compute_Acc(self):
        for i in range(self.N):
            sumAx = self.P[i][0] + self.Vi[i][0]
            sumAy = self.G + self.P[i][1] + self.Vi[i][1]
            #判断边界
            if self.Points[i][0] <= 0 or self.Points[i][0] > self.Size:
                sumAx *= -1
            if self.Points[i][1] <= 0 or self.Points[i][1] > self.Size:
                sumAy *= -1
            self.Acc[i][0] = sumAx
            self.Acc[i][1] = sumAy

    #计算粒子速度
    def compute_V(self):
        for i in range(self.N):
            sumVx = self.V[i][0] + self.Acc[i][0]
            sumVy = self.V[i][1] + self.Acc[i][1]
            #判断边界
            if self.Points[i][0] <= 0 or self.Points[i][0] > self.Size:
                sumVx *= -1
            if self.Points[i][1] <= 0 or self.Points[i][1] > self.Size:
                sumVy *= -1
            self.V[i][0] = sumVx
            self.V[i][1] = sumVy
        print(self.Acc[0][0], self.Acc[0][1], self.V[0][0], self.V[0][1],
              self.Points[0][0], self.Points[0][1], self.D[0], self.P[0][0], self.P[0][1],
              self.Vi[0][0], self.Vi[0][1])

    def compute_position(self):
        for i in range(self.N):
            self.Points[i][0] += self.V[i][0]
            self.Points[i][1] += self.V[i][1]
            '''
            if self.Points[i][0] <= 0 or self.Points[i][0] > self.Size:
                self.V[i][0] *= -1
            if self.Points[i][1] <= 0 or self.Points[i][1] > self.Size:
                self.V[i][1] *= -1
            '''


    #返回所有质点的位置
    def get_Particles(self):
        return self.Points
