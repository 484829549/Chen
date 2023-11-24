import sys
import os
import winsound
pythonpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, pythonpath)
import src.config as cfg
from src.robot import Robot, RobotThread
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6 import QtWidgets, QtGui, QtCore, QtSql
from ui.WELLD_ui import Ui_WelldWidget


class WelldWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WelldWidget()
        self.ui.setupUi(self)

        self.robotCtrl = Robot(cfg.address)

        self.ui.menuListWidget.itemClicked.connect(self.menu_click_show)

        self.dragClickCount = 0
        self.ui.dragPushButton.clicked.connect(self.drag_click_show)

        self.recordClickCount = 0
        self.ui.recordPushButton.clicked.connect(self.record_click_show)

        # show the main page
        self.ui.welldStackedWidget.setCurrentIndex(0)

    def menu_click_show(self):
        itemIndex = self.ui.menuListWidget.currentIndex().row()
        self.ui.welldStackedWidget.setCurrentIndex(itemIndex)

    def drag_click_show(self):
        self.dragClickCount += 1
        if self.dragClickCount % 2 == 1:
            self.ui.dragPushButton.setText(
                QCoreApplication.translate("MainWindow", u"退出拖拽", None))
            winsound.PlaySound("./res/media/indrag.wav", winsound.SND_FILENAME)
            self.robotCtrl.drag(1)
        else:
            self.ui.dragPushButton.setText(
                QCoreApplication.translate("MainWindow", u"进入拖拽", None))
            winsound.PlaySound("./res/media/outdrag.wav",
                               winsound.SND_FILENAME)
            self.robotCtrl.drag(0)
        winsound.Beep(cfg.beeperfreq, cfg.beeperDuration)

    def record_click_show(self):
        self.recordClickCount += 1
        if self.recordClickCount % 2 == 1:
            self.ui.recordPushButton.setText(
                QCoreApplication.translate("WelldWidget", u"停止记录", None))
        else:
            self.ui.recordPushButton.setText(
                QCoreApplication.translate("WelldWidget", u"开始记录", None))


def main():
    app = QApplication(sys.argv)
    window = WelldWindow()
    window.show()  # for object to show
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
