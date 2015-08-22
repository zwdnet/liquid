# -*- coding:utf-8 -*-
#模拟流体的程序
import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
import stimulator as sm

class LiquidBox(QWidget):
    # 模拟流体力学程序，盛着液体的盒子
    def __init__(self):
        super().__init__()
        self.speed = 100  #重绘速度100ms
        self.WindowSize = 400
        self.timer = QBasicTimer()
        self.sim = sm.Stimulator(self.WindowSize)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 200+self.WindowSize, 200+self.WindowSize)
        self.setFixedSize(self.WindowSize, self.WindowSize)
        self.setWindowTitle("流体力学模拟程序")
        self.timer.start(self.speed, self)
        self.show()

    #处理计时器消息
    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.update()
        else:
            super().timerEvent(event)

    #处理重绘消息
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.Draw(qp)
        qp.end()

    #具体绘图函数
    def Draw(self, qp):
        qp.setPen(Qt.blue)
        #先用一个随机作图函数代替，以后改成模拟程序
        # size = self.size()
        # points = [[1 for x in range(size.width())] for y in range(size.height())]
        # for i in range(5000):
        #     x = random.randint(1, size.width()-1)
        #     y = random.randint(1, size.height()-1)
        #     points[x][y] = 2
        #     qp.drawPoint(x, y)
        # qp.setPen(Qt.black)
        # for i in range(size.width()):
        #     for j in range(size.height()):
        #         if points[i][j] == 1:
        #             qp.drawPoint(i, j)
        points = self.sim.step()
        for i in range(self.WindowSize):
            for j in range(self.WindowSize):
                if points[i][j] == 1:
                    qp.drawPoint(i, j)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    liquidSitumator = LiquidBox()
    sys.exit(app.exec_())
