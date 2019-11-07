import sys
from PyQt5 import QtGui

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QImage, QPainter, QPen, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from keras_inference import Inference

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        top = 400
        left = 400
        width = 700
        height = 700
        self.setGeometry(top, left, width, height)

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 30
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

        menuBar = self.menuBar()
        clearAction = QAction("Clear", self)
        clearAction.setShortcut("Ctrl+C")
        menuBar.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        predictAction = QAction("Predict", self)
        menuBar.addAction(predictAction)
        predictAction.triggered.connect(self.predict)

        self.inference = Inference()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def predict(self):
        img_path = 'img/unprocessed_img.png'
        self.image.save(img_path, 'png')
        prediction = self.inference.predict(img_path)

        painter = QPainter(self.image)
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('black'))
        painter.setPen(pen)
        font = QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(200)
        painter.setFont(font)
        self.clear()
        painter.drawText(280, 280, str(prediction))
        painter.end()
        self.update()

    def threePixel(self):
        self.brushSize = 3

    def fivePixel(self):
        self.brushSize = 5

    def sevenPixel(self):
        self.brushSize = 7

    def ninePixel(self):
        self.brushSize = 9

    def blackColor(self):
        self.brushColor = Qt.black

    def whiteColor(self):
        self.brushColor = Qt.white

    def redColor(self):
        self.brushColor = Qt.red

    def greenColor(self):
        self.brushColor = Qt.green

    def yellowColor(self):
        self.brushColor = Qt.yellow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()