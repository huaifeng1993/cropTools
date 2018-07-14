#!usr/bin/python3
# -*- coding: utf-8 -*-
#
# author:shenhuixiang
#
import sys
from mainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox,QInputDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QStringListModel

import os
class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self,*args, **kwargs):
        super(MainWindow,self).__init__()
        self.setupUi(self)

        self.label_info = {}
        self.label_name=[]
        self.image_crop_save_path=None

        # Method Connected
        self.startBtn.clicked.connect(self.startBtnMethod)
        self.imageOpenToolBtn.clicked.connect(self.imagetoolBtnMethod)

        self.rightBtn.clicked.connect(self.rightBtnMethod)
        self.leftBtn.clicked.connect(self.leftBtnMethod)
        self.deletBtn.clicked.connect(self.deletBtnMethod)
        self.cropToolBtn.clicked.connect(self.cropBtnMethod)
        self.cropStopToolBtn.clicked.connect(self.cropStopBtnMethod)
        self.addClassBtn.clicked.connect(self.addClassBtnMethod)
        self.classDeletBtn.clicked.connect(self.classDeletBtnMethod)
        self.classListView.clicked.connect(self.classListViewMethod)


        self.viewCount=0
        self.statusBar().showMessage('Ready')
        self.show()
    def addClassBtnMethod(self):
        text, ok = QInputDialog.getText(self, '输入类别',
                                       '输入类别:')


        if ok:
            label_directory = QFileDialog.getExistingDirectory(self, "选取保存类别文件夹", '/home')
            if label_directory:
                self.label_name.append(str(text))
                self.label_info.update({str(text):label_directory})
                slm = QStringListModel()
                self.classListView.setModel(slm)
                slm.setStringList(self.label_name)

    def classDeletBtnMethod(self):
        print('classDeleteBtnMethod')


    def startBtnMethod(self):
        image_directory=self.imageLineEdit.text()
        if image_directory:
            self.images=os.listdir(image_directory)
            self.images.sort()

            image_path=os.path.join(image_directory,self.images[self.viewCount])
            # load image and label.
            self.loadGraph(image_path)
            # if start button is not pushed then the other buttons will be disabled.
            self.rightBtn.setEnabled(True)
            self.leftBtn.setEnabled(True)
            self.deletBtn.setEnabled(True)
        else:
            QMessageBox.information(self, '注意！', "没有载入任何文件夹！")




    def imagetoolBtnMethod(self):
        image_directory=QFileDialog.getExistingDirectory(self,"选取文件夹",'/home')
        self.imageLineEdit.setText(image_directory)


    def rightBtnMethod(self):
        """right button method
        :return: 
        """
        if self.viewCount==len(self.images)-1:
            QMessageBox.warning(self, '注意！', "这已经是最后一张图片！")
        else:
            self.viewCount=self.viewCount+1
            image_directory = self.imageLineEdit.text()

            image_path = os.path.join(image_directory, self.images[self.viewCount])

            #load image and label.
            self.loadGraph(image_path)

    def leftBtnMethod(self):
        """left button method """
        if(self.viewCount==0):
            QMessageBox.warning(self,'注意！',"这已经是第一张图片！")
        else:
            self.viewCount=self.viewCount-1
            image_directory = self.imageLineEdit.text()

            image_path = os.path.join(image_directory, self.images[self.viewCount])

            # load image and label.
            self.loadGraph(image_path)

    def deletBtnMethod(self):
        reply = QMessageBox.question(self, 'Message',
                                     "确定删除此图片?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            image_directory = self.imageLineEdit.text()

            image_path = os.path.join(image_directory, self.images[self.viewCount])

            if(os.path.exists(image_path)):

                os.remove(image_path)

                QMessageBox.information(self, '通知！', "图片已成功删除！")
                if(self.viewCount==len(self.images)-1):
                    self.viewCount=self.viewCount-1
                self.images = os.listdir(image_directory)
                self.images.sort()

                self.labels.sort()
                image_path = os.path.join(image_directory, self.images[self.viewCount])

                # load image and label.
                self.loadGraph(image_path)
            else:
                QMessageBox.warning(self, '注意！', "图片不存在！")

    def cropBtnMethod(self):
        """
        :return: 
        """
        self.imageCandvas.setMouseTracking(True)
        self.imageQLb.width=int(self.widthSpinBox.text())
        self.imageQLb.length=int(self.lengthSpinBox.text())
        self.imageQLb.croped_save_path=self.image_crop_save_path
        self.imageQLb.switch = True

        #if corpBtn is clicked then the method,setMouseTracking,was seted.



    def cropStopBtnMethod(self):
        """
        :return: 
        """
        self.imageQLb.switch = False
    def classListViewMethod(self,qModelindex):
        self.listViewselectedRow=self.label_name[qModelindex.row()]
        self.image_crop_save_path=self.label_info[self.listViewselectedRow]

        print(self.image_crop_save_path)
    def loadGraph(self,image_path):
        # load image and label.
        imagePng = QPixmap(image_path)
        self.imageQLb.setPixmap(imagePng)
        #set statusbar
        self.statusBar().showMessage(
            '当前图片:({0})'.format(self.images[self.viewCount]))






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex=MainWindow()
    sys.exit(app.exec_())