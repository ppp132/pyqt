from PySide2.QtWidgets import QWidget, QApplication
from pyqtgraph.Qt import QtGui, QtCore
from PySide2.QtGui import QPainter, QBrush, QColor
from PySide2.QtCore import Qt, QRect
from PySide2.QtUiTools import QUiLoader
import pyqtgraph as pg




class Stats:
    def __init__(self, parent=None):
        self.ui = QUiLoader().load('stats.ui')
        self.ui.button.clicked.connect(self.paintEvent)

        #super().__init__(parent)
        #self.setFixedSize(1000, 800)

    def gv_test_show(self):
        ## 步骤一：创建一个场景（原点在左上角，x轴向右，y轴向下）
        self.graphicsView.scene = QtWidget.QGraphicsScene(0, 0, 200, 200)

        ## 步骤二：创建一个图元对象
        item = GvTestItem()

        ## 可选：setPos(x,y) 函数来重设Item坐标系原点，这时Item坐标系原点处于设置的x、y处
        item.setPos(0, 250)

        ## 步骤三：通过addItem将图元对象添加到场景中
        self.graphicsView.scene.addItem(item)

        ## 步骤四：通过setScene将场景在视图中呈现
        self.graphicsView.setScene(self.graphicsView.scene)




    def paintEvent(self, event):
        pw = self.ui.graphicsView.scene()



        # 注意设置对象，不然painter不知道在哪画
        painter = QPainter(self)
        # 下面两行等效上面一行
        # painter = QPainter()
        # painter.begin(self)

        # 设置蓝色的画笔
        painter.setPen(Qt.black)
        rectangle = QRect(50, 50, 800, 600)
        rectangle1 = QRect(50, 600, 50, 50)

        # 绘制矩形区域
        painter.drawRect(rectangle)
        painter.drawRect(rectangle1)
        # 填充矩形区域，使用蓝色的刷子
        #painter.fillRect(rectangle, QBrush(QColor(Qt.blue)))
class GvTestItem(QGraphicsItem):
    def __init__(self):
        super(GvTestItem, self).__init__()

    ## 这个纯虚函数将图元的外边界定义为矩形; 所有绘画必须限制在图元的边界矩形内；设置矩形左上角位置(0,0)，右下角位置（200，200）
    def boundingRect(self):
        return QRectF(0, 0, 200, 200)

    def paint(self, painter, option, widget):
        painter.setPen(Qt.blue)
        painter.drawLine(0, 0, 200, -200)

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()