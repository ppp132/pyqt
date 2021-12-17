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

#最低水平线集的最低水平线的高，水平线集的高列表，对应的x位置及l长度
LowLine = 0
LowLine_y = [0]
LowLine_x = [0]
LowLine_l = [500]

#矩形宽高
n1 = 40
n2 = 60


p = [0.5]



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
        #self.ui.btn_sin.clicked.connect(self.plot_sin)

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

        """
        xy2 = np.array([a[0], b[0]])
        rect = mpathes.Rectangle(xy2, n1, n2, color='r')
        self.gv_visual_data_content.axes.add_patch(rect)
        """
        """
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
        """

        #矩形顺时针四个点（a,b）（a,c）（d,c）（d,b）


        self.ui.graphicsView.setScene(self.graphic_scene)
        # 把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()
        # 调用show方法呈现图形






    def showrect1(self):

        LowLine = min(LowLine_y) #最低水平线
        i = LowLine_y.index(LowLine) #i是最低水平线在y中的索引

        if LowLine_l[i] >= n2:
            #LowLine_x.append(LowLine_x[-1] + n2)  # 纵向摆放一个x变化
            a.append(LowLine_x[-1])
            b.append(LowLine)
            # 绘图
            xy = np.array([a[-1], b[-1]])
            rect = mpathes.Rectangle(xy, n2, n1, color='g')
            self.gv_visual_data_content.axes.add_patch(rect)
            LowLine_x.append(LowLine_x[-1] + n2)  # 纵向摆放一个x变化
            """
            if i == 0:  # i=0说明还没放置，进行第一次放置
                LowLine_y[0] = n1
                LowLine_y.append(0)  # insert在索引插入
                LowLine_l[0] = n2  # 第一段为n2
                LowLine_l.append(500 - n2)  # 第二段为n2
            """
            if i >= 0:  # i>=1说明已经有放置了
                LowLine_y.insert(i , LowLine + n1)  # y更新
                LowLine_l.insert(i , n2)  # l更新
                LowLine_l[i + 1] = LowLine_l[i + 1] - LowLine_l[i]



        if n1 <= LowLine_l[i] < n2:
            LowLine_x.append(LowLine_x[-1] + n1)  # 纵向摆放一个x变化
            a.append(LowLine_x[i])
            b.append(LowLine)
            # 绘图
            xy = np.array([a[-1], b[-1]])
            rect = mpathes.Rectangle(xy, n1, n2, color='r')
            self.gv_visual_data_content.axes.add_patch(rect)

            if i == 0:  # i=0说明还没放置，进行第一次放置
                LowLine_y[0] = n2
                LowLine_y.append(0)  # insert在索引的后面插入
                LowLine_l[0] = n1  # 第一段为n1
                LowLine_l.append(500 - n1)  # 第二段为n2
            if i >= 1:  # i>=1说明已经有放置了
                LowLine_y.insert(i , LowLine + n2)  # y更新
                LowLine_l.insert(i , n1)  # l更新
                LowLine_l[i + 1] = LowLine_l[i + 1] - LowLine_l[i]

        if LowLine_y[i] == LowLine_y[i - 1]:  #用于合并最低水平线
            del LowLine_y[i]
            del LowLine_x[i]
            LowLine_l[i - 1] = LowLine_l[i - 1] + LowLine_l[i]
            del LowLine_l[i]


        if LowLine_l[i] < n1:   #最低水平线长度小于矩形宽时则从最低水平线集中删除
            del LowLine_x[i]
            del LowLine_y[i]
            del LowLine_l[i]











    def plot_car1c(self):
        #self.gv_visual_data_content.axes.clear()  # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
        p=0.5


        self.showrect1()



        #self.gv_visual_data_content.axes.plot(h_max_w[-1], h_max_h[-1], 'b*')
        #self.gv_visual_data_content.axes.plot([h_max_w[0], h_max_w[1]],
                                              #[h_max_h[0], h_max_h[1]], color='black')



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
