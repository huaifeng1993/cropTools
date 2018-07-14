#author:shenhuixiang
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
import cv2
import sys
import os

class myLabel(QLabel):
    x1 = 0
    y1 = 0
    width=224
    length=224
    flag = False
    switch=False

    croped_save_path='./'

    def mousePressEvent(self, event):
        if self.switch:
            self.flag = True
    def mouseReleaseEvent(self, event):
        if self.switch:
            pqscreen = QGuiApplication.primaryScreen()
            pixmap2 = pqscreen.grabWindow(self.winId(), self.x1 - int(self.width/2),
                                          self.y1 - int(self.length/2),self.width , self.length)
            counts=len(os.listdir(self.croped_save_path))
            pixmap2.save(os.path.join(self.croped_save_path,'{}.png'.format(counts)))
            self.flag = False
    def mouseMoveEvent(self, event):
        if self.switch:
             if self.flag:
                self.x1 = event.x()
                self.y1 = event.y()
                self.update()
    def paintEvent(self, event):
        super().paintEvent(event)  # 重要，更新图片
        if self.switch:
            if self.flag:
                rect = QRect(self.x1-int(self.width/2)-1,
                             self.y1-int(self.length/2)-1,
                             self.width+1,self.length+1)
                painter = QPainter(self)
                painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
                painter.drawRect(rect)

# class Canvas(QtWidgets.QWidget):
#     def __init__(self, *args, **kwargs):
#         super(Canvas, self).__init__(*args, **kwargs)
