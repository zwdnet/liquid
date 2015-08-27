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
        self.speed = 100  #重绘速度1s
        self.WindowSize = 50
        self.timer = QBasicTimer()
        self.sim = sm.Stimulator(self.WindowSize)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 600, 600)
        self.setFixedSize(400, 400)
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
        points = self.sim.step()
        for i in range(len(points)):
            qp.drawPoint(int(points[i][0]), int(points[i][1]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    liquidSitumator = LiquidBox()
    sys.exit(app.exec_())
