from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene, \
    QFileDialog, QMessageBox,QGraphicsView
#from 001 import Ui_MainWindow
from PySide2.QtGui import QPainter, QPen, QBrush, QPolygon, QFont, QPalette,QColor
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Qt, QPoint
import sys
import numpy as np
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpathes
matplotlib.use("Qt5Agg")  # 声明使用QT5



a = [0]
b = [0]
c = [100]
d = [50]
n = [0]
h_max_w = [0]
h_max_h = [100]
n1 = 50
n2 = 100
i = 0




class MyFigureCanvas(FigureCanvas):
    '''
    通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，
    又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
    '''

    def __init__(self, parent=None, width=500, height=800, xlim=(0, 500), ylim=(0, 800),   dpi=100):
        # 创建一个Figure
        fig = plt.Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        # tight_layout: 用于去除画图时两边的空白

        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        """
        #方法1
        blackPen = QPen(Qt.black)
        blackPen.setWidth(5)

        greenPen = QPen(Qt.green)
        greenPen.setWidth(5)
        # ellipse = scene.addEllipse(10,10, 200,200, blackPen, greenBrush)
        rect = fig.addRect(0, 0, 500, 500, blackPen)
        rect1 = fig.addRect(0, 0, 50, 100, greenPen)
        rect2 = fig.addRect(50, 0, 50, 100, greenPen)
        while a[-1] <= 400:
            a.append(a[-1] + m)
        while b[-1] <= 300:
            b.append(b[-1] + n)
        for b1 in b:
            for a1 in a:
                recti = fig.addRect(a1, b1, 50, 100)
        """
        """
        #方法2
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        # painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        # painter.setBrush(QBrush(Qt.red))
        self.a = 10;
        self.b = 10;
        self.c = 100;
        self.d = 80;
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
        """


        self.axes = fig.add_subplot(111)
        # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        #self.axes.spines['top'].set_visible(False)  # 去掉上面的横线
        #self.axes.spines['right'].set_visible(False)
        self.axes.set_xlim(xlim)
        self.axes.set_ylim(ylim)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('001.ui')

        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)

        # 初始化 gv_visual_data 的显示
        self.gv_visual_data_content = MyFigureCanvas(width=self.ui.graphicsView.width() / 101,
                                                     height=self.ui.graphicsView.height() / 101,
                                                     xlim=(0, 500),
                                                     ylim=(0, 800)
                                                     )  # 实例化一个FigureCanvas
        #self.plot_cos()
        self.plot_car1()

        self.ui.car1.clicked.connect(self.plot_car1)
        self.ui.car1c.clicked.connect(self.plot_car1c)
        self.ui.btn_sin.clicked.connect(self.plot_sin)

    def plot_cos(self):
        x = np.arange(0, 2 * np.pi, np.pi / 100)
        y = np.cos(x)
        self.gv_visual_data_content.axes.plot(x, y)
        self.gv_visual_data_content.axes.set_title('cos()')
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，
        # 必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphic_scene.addWidget(self.gv_visual_data_content)
        # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.ui.graphicsView.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()  # 调用show方法呈现图形

    def plot_car1(self):
        self.graphic_scene = QGraphicsScene()
        # 创建一个QGraphicsScene
        self.graphic_scene.addWidget(self.gv_visual_data_content)
        # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        #fig, ax = self.gv_visual_data_content.axes()
        # 矩形顺时针四个点（a,b）（a,c）（d,c）（d,b）



        xy2 = np.array([a[0], b[0]])
        rect = mpathes.Rectangle(xy2, d[0], c[0], color='r')
        self.gv_visual_data_content.axes.add_patch(rect)

        while b[-1] <= 700:
            a.clear()
            a.append(0)
            d.clear()
            d.append(0)
            while a[-1] <= 400:
                if np.random.rand() < 0.5:
                    a.append(d[-1])
                    xy = np.array([a[-1], b[-1]])
                    rect = mpathes.Rectangle(xy, n1, n2, color='r')
                    self.gv_visual_data_content.axes.add_patch(rect)
                    d.append(d[-1] + n1)
                else:
                    a.append(d[-1])
                    xy = np.array([a[-1], b[-1]])
                    rect = mpathes.Rectangle(xy, n2, n1, color='g')
                    self.gv_visual_data_content.axes.add_patch(rect)
                    d.append(d[-1] + n2)
            b.append(b[-1]+n2)

























        #矩形顺时针四个点（a,b）（a,c）（d,c）（d,b）


        self.ui.graphicsView.setScene(self.graphic_scene)
        # 把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()
        # 调用show方法呈现图形

    def plot_car1c(self):
        #self.gv_visual_data_content.axes.clear()  # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
        a.clear()
        a.append(0)
        d.clear()
        d.append(0)
        while a[-1] <= 400:
            if np.random.rand() < 0.5:
                a.append(d[-1])
                xy = np.array([a[-1], 100])
                rect = mpathes.Rectangle(xy, n1, n2, color='r')
                self.gv_visual_data_content.axes.add_patch(rect)
                d.append(d[-1] + n1)
            else:
                a.append(d[-1])
                xy = np.array([a[-1], 100])
                rect = mpathes.Rectangle(xy, n2, n1, color='g')
                self.gv_visual_data_content.axes.add_patch(rect)
                d.append(d[-1] + n2)



        #self.gv_visual_data_content.axes.set_title('sin()')
        self.gv_visual_data_content.draw()  # 刷新画布显示图片，否则不刷新显示

    def plot_sin(self):
        x = np.arange(0, 2 * np.pi, np.pi / 100)
        y = np.sin(x)
        self.gv_visual_data_content.axes.clear()  # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
        self.gv_visual_data_content.axes.plot(x, y)
        self.gv_visual_data_content.axes.set_title('sin()')
        self.gv_visual_data_content.draw()  # 刷新画布显示图片，否则不刷新显示


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.ui.show()
    sys.exit(app.exec_())
