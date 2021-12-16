from PySide2.QtWidgets import QApplication, QWidget, QGraphicsScene, QPushButton,QGraphicsView, QGraphicsItem
from PySide2.QtGui import QPainter, QPen, QBrush, QPolygon, QFont, QPalette,QColor
from PySide2.QtCore import Qt, QPoint

import sys



class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vehicle stowage")
        self.setGeometry(0,0,1920,1080)

        self.create_ui()


        self.show()








    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        # painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        #painter.setBrush(QBrush(Qt.red))
        self.a=10;self.b=10;self.c=100;self.d=80;
        points = QPolygon([
            QPoint(10, 10),
            QPoint(1010, 10),
            QPoint(1010, 810),
            QPoint(10, 810),
        ])
        self.points1 = QPolygon([
            QPoint(self.a, self.b),
            QPoint(self.c, self.b),
            QPoint(self.c, self.d),
            QPoint(self.a, self.d),
        ])
        painter.drawPolygon(points)
        painter.drawPolygon(self.points1)



    def create_ui(self):
        button = QPushButton("car1",self)
        button.setGeometry(1020, 100, 100,50)  #左上角长宽位置，控件长宽大小
        button.clicked.connect(self.car1)

        button2 = QPushButton("car2", self)
        button2.setGeometry(1020, 200, 100, 50)
        button2.clicked.connect(self.car2)

        scene = QGraphicsScene(self)




        greenBrush = QBrush(Qt.green)
        blueBrush = QBrush(Qt.blue)

        blackPen = QPen(Qt.black)
        blackPen.setWidth(5)

        greenPen = QPen(Qt.green)
        greenPen.setWidth(5)
        a=[0];b=[0];c=[0];d=[0];
        i=0
        j=0
        m=50
        n=100
        #ellipse = scene.addEllipse(10,10, 200,200, blackPen, greenBrush)
        rect = scene.addRect(0,0, 500,500, blackPen)
        rect1 = scene.addRect(0, 0, 50, 100, greenPen)
        rect2 = scene.addRect(50, 0, 50, 100, greenPen)
        while a[-1] <= 400:
            a.append(a[-1] + m)
        while b[-1] <= 300:
            b.append(b[-1] + n)
        for b1 in b:
            for a1 in a:
                recti = scene.addRect(a1, b1, 50, 100)


        #scene.addText("codeloop",QFont("000",15))

        #ellipse.setFlag(QGraphicsItem.ItemIsMovable)  #move
        #rect.setFlag(QGraphicsItem.ItemIsMovable)  # move

        self.view = QGraphicsView(scene, self)
        self.view.setGeometry(1300,10,600,600)

    def car1(self):
        self.a += 10
        self.b += 10
        self.c += 10
        self.d += 10
        self.view(self.points1)


    def car2(self):
        self.view.rotate(+14)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())