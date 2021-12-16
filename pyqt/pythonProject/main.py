from gv import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


## 重定义Ui_MainWindow，与Qt Designer生成的代码解耦
class GvTest(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GvTest, self).__init__()
        self.setupUi(self)
        self.gv_test_show()

    def gv_test_show(self):
        ## 步骤一：创建一个场景（原点在左上角，x轴向右，y轴向下）
        self.graphicsView.scene = QtWidgets.QGraphicsScene(0, 0, 200, 200)

        ## 步骤二：创建一个图元对象
        item = GvTestItem()

        ## 可选：setPos(x,y) 函数来重设Item坐标系原点，这时Item坐标系原点处于设置的x、y处
        item.setPos(0, 250)

        ## 步骤三：通过addItem将图元对象添加到场景中
        self.graphicsView.scene.addItem(item)

        ## 步骤四：通过setScene将场景在视图中呈现
        self.graphicsView.setScene(self.graphicsView.scene)


## 一般需要自定义一个图元，并实现基本的boundingRect、paint
class GvTestItem(QGraphicsItem):
    def __init__(self):
        super(GvTestItem, self).__init__()

    ## 这个纯虚函数将图元的外边界定义为矩形; 所有绘画必须限制在图元的边界矩形内；设置矩形左上角位置(0,0)，右下角位置（200，200）
    def boundingRect(self):
        return QRectF(0, 0, 200, 200)

    def paint(self, painter, option, widget):
        painter.setPen(Qt.blue)
        painter.drawLine(0, 0, 200, -200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gv = GvTest()
    gv.show()
    sys.exit(app.exec())

