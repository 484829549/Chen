# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import os
pythonpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, pythonpath)
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QButtonGroup,
    QComboBox, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLCDNumber,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QStackedWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
from src.myQLabel import MyQLabel
import res.pngConfig_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(929, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(224, 241, 255);\n"
"border-radius:0px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(3)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frameTop_1 = QFrame(self.centralwidget)
        self.frameTop_1.setObjectName(u"frameTop_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frameTop_1.sizePolicy().hasHeightForWidth())
        self.frameTop_1.setSizePolicy(sizePolicy2)
        self.frameTop_1.setMinimumSize(QSize(800, 120))
        self.frameTop_1.setMaximumSize(QSize(1280, 160))
        self.frameTop_1.setFrameShape(QFrame.StyledPanel)
        self.frameTop_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameTop_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 4)
        self.logo = MyQLabel(self.frameTop_1)
        self.logo.setObjectName(u"logo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy3)
        self.logo.setMinimumSize(QSize(100, 0))
        self.logo.setMaximumSize(QSize(180, 80))
        self.logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.logo.setPixmap(QPixmap(u":/images/welld.png"))
        self.logo.setScaledContents(True)
        self.logo.setOpenExternalLinks(True)

        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.title = QLabel(self.frameTop_1)
        self.title.setObjectName(u"title")
        sizePolicy2.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy2)
        self.title.setMaximumSize(QSize(768, 16777215))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.title.setFont(font1)
        self.title.setScaledContents(True)
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.title, 0, 1, 1, 1)

        self.frameStateView_1 = QFrame(self.frameTop_1)
        self.frameStateView_1.setObjectName(u"frameStateView_1")
        sizePolicy2.setHeightForWidth(self.frameStateView_1.sizePolicy().hasHeightForWidth())
        self.frameStateView_1.setSizePolicy(sizePolicy2)
        self.frameStateView_1.setMaximumSize(QSize(256, 120))
        self.frameStateView_1.setStyleSheet(u"border-radius:10px;\n"
"background-color: transparent;")
        self.frameStateView_1.setFrameShape(QFrame.StyledPanel)
        self.frameStateView_1.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frameStateView_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(9, 0, 0, 0)
        self.stateStr = QLabel(self.frameStateView_1)
        self.stateStr.setObjectName(u"stateStr")
        font2 = QFont()
        font2.setFamilies([u"\u6977\u4f53"])
        font2.setPointSize(12)
        self.stateStr.setFont(font2)

        self.gridLayout.addWidget(self.stateStr, 0, 0, 1, 2)

        self.statelight_1 = QLabel(self.frameStateView_1)
        self.statelight_1.setObjectName(u"statelight_1")
        sizePolicy2.setHeightForWidth(self.statelight_1.sizePolicy().hasHeightForWidth())
        self.statelight_1.setSizePolicy(sizePolicy2)
        self.statelight_1.setMinimumSize(QSize(30, 30))
        self.statelight_1.setMaximumSize(QSize(30, 30))
        self.statelight_1.setFrameShape(QFrame.StyledPanel)
        self.statelight_1.setFrameShadow(QFrame.Raised)
        self.statelight_1.setPixmap(QPixmap(u":/images/normallight.png"))
        self.statelight_1.setScaledContents(True)
        self.statelight_1.setWordWrap(False)
        self.statelight_1.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.statelight_1, 1, 0, 1, 1)

        self.state_camera_1 = QLabel(self.frameStateView_1)
        self.state_camera_1.setObjectName(u"state_camera_1")
        sizePolicy2.setHeightForWidth(self.state_camera_1.sizePolicy().hasHeightForWidth())
        self.state_camera_1.setSizePolicy(sizePolicy2)
        self.state_camera_1.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"\u6977\u4f53"])
        font3.setPointSize(11)
        self.state_camera_1.setFont(font3)

        self.gridLayout.addWidget(self.state_camera_1, 1, 1, 1, 1)

        self.state_lcd_1 = QLCDNumber(self.frameStateView_1)
        self.state_lcd_1.setObjectName(u"state_lcd_1")
        sizePolicy2.setHeightForWidth(self.state_lcd_1.sizePolicy().hasHeightForWidth())
        self.state_lcd_1.setSizePolicy(sizePolicy2)
        self.state_lcd_1.setAcceptDrops(False)
        self.state_lcd_1.setFrameShape(QFrame.NoFrame)
        self.state_lcd_1.setSmallDecimalPoint(False)
        self.state_lcd_1.setMode(QLCDNumber.Dec)
        self.state_lcd_1.setSegmentStyle(QLCDNumber.Flat)
        self.state_lcd_1.setProperty("value", 0.000000000000000)
        self.state_lcd_1.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.state_lcd_1, 1, 2, 1, 1)

        self.statelight_2 = QLabel(self.frameStateView_1)
        self.statelight_2.setObjectName(u"statelight_2")
        sizePolicy2.setHeightForWidth(self.statelight_2.sizePolicy().hasHeightForWidth())
        self.statelight_2.setSizePolicy(sizePolicy2)
        self.statelight_2.setMinimumSize(QSize(30, 30))
        self.statelight_2.setMaximumSize(QSize(30, 30))
        self.statelight_2.setFrameShape(QFrame.StyledPanel)
        self.statelight_2.setFrameShadow(QFrame.Raised)
        self.statelight_2.setPixmap(QPixmap(u":/images/normallight.png"))
        self.statelight_2.setScaledContents(True)
        self.statelight_2.setWordWrap(False)
        self.statelight_2.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.statelight_2, 2, 0, 1, 1)

        self.state_camera_2 = QLabel(self.frameStateView_1)
        self.state_camera_2.setObjectName(u"state_camera_2")
        sizePolicy2.setHeightForWidth(self.state_camera_2.sizePolicy().hasHeightForWidth())
        self.state_camera_2.setSizePolicy(sizePolicy2)
        self.state_camera_2.setMaximumSize(QSize(16777215, 16777215))
        self.state_camera_2.setFont(font3)

        self.gridLayout.addWidget(self.state_camera_2, 2, 1, 1, 1)

        self.state_lcd_2 = QLCDNumber(self.frameStateView_1)
        self.state_lcd_2.setObjectName(u"state_lcd_2")
        sizePolicy2.setHeightForWidth(self.state_lcd_2.sizePolicy().hasHeightForWidth())
        self.state_lcd_2.setSizePolicy(sizePolicy2)
        self.state_lcd_2.setAcceptDrops(False)
        self.state_lcd_2.setSmallDecimalPoint(False)
        self.state_lcd_2.setMode(QLCDNumber.Dec)
        self.state_lcd_2.setSegmentStyle(QLCDNumber.Flat)
        self.state_lcd_2.setProperty("value", 0.000000000000000)
        self.state_lcd_2.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.state_lcd_2, 2, 2, 1, 1)

        self.statelight_3 = QLabel(self.frameStateView_1)
        self.statelight_3.setObjectName(u"statelight_3")
        sizePolicy2.setHeightForWidth(self.statelight_3.sizePolicy().hasHeightForWidth())
        self.statelight_3.setSizePolicy(sizePolicy2)
        self.statelight_3.setMinimumSize(QSize(30, 30))
        self.statelight_3.setMaximumSize(QSize(30, 30))
        self.statelight_3.setFrameShape(QFrame.StyledPanel)
        self.statelight_3.setFrameShadow(QFrame.Raised)
        self.statelight_3.setPixmap(QPixmap(u":/images/normallight.png"))
        self.statelight_3.setScaledContents(True)
        self.statelight_3.setWordWrap(False)
        self.statelight_3.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.statelight_3, 3, 0, 1, 1)

        self.state_camera_3 = QLabel(self.frameStateView_1)
        self.state_camera_3.setObjectName(u"state_camera_3")
        sizePolicy2.setHeightForWidth(self.state_camera_3.sizePolicy().hasHeightForWidth())
        self.state_camera_3.setSizePolicy(sizePolicy2)
        self.state_camera_3.setMaximumSize(QSize(16777215, 16777215))
        self.state_camera_3.setFont(font3)

        self.gridLayout.addWidget(self.state_camera_3, 3, 1, 1, 1)

        self.state_lcd_3 = QLCDNumber(self.frameStateView_1)
        self.state_lcd_3.setObjectName(u"state_lcd_3")
        sizePolicy2.setHeightForWidth(self.state_lcd_3.sizePolicy().hasHeightForWidth())
        self.state_lcd_3.setSizePolicy(sizePolicy2)
        self.state_lcd_3.setAcceptDrops(False)
        self.state_lcd_3.setSmallDecimalPoint(False)
        self.state_lcd_3.setMode(QLCDNumber.Dec)
        self.state_lcd_3.setSegmentStyle(QLCDNumber.Flat)
        self.state_lcd_3.setProperty("value", 0.000000000000000)
        self.state_lcd_3.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.state_lcd_3, 3, 2, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)

        self.gridLayout_2.addWidget(self.frameStateView_1, 0, 2, 2, 1)

        self.frameCam = QFrame(self.frameTop_1)
        self.frameCam.setObjectName(u"frameCam")
        self.frameCam.setMaximumSize(QSize(1024, 16777215))
        self.frameCam.setFrameShape(QFrame.StyledPanel)
        self.frameCam.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameCam)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frameCam)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.cam1 = QPushButton(self.frameCam)
        self.cam1.setObjectName(u"cam1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cam1.sizePolicy().hasHeightForWidth())
        self.cam1.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamilies([u"\u6977\u4f53"])
        font4.setPointSize(15)
        self.cam1.setFont(font4)
        self.cam1.setCursor(QCursor(Qt.PointingHandCursor))
        self.cam1.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"border:4px solid rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"padding:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:10px;\n"
"background-color: rgb(180, 235, 255);\n"
"}")
        self.cam1.setCheckable(True)
        self.cam1.setChecked(False)
        self.cam1.setAutoRepeat(True)

        self.horizontalLayout.addWidget(self.cam1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.cam2 = QPushButton(self.frameCam)
        self.cam2.setObjectName(u"cam2")
        self.cam2.setFont(font4)
        self.cam2.setCursor(QCursor(Qt.PointingHandCursor))
        self.cam2.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"border:4px solid rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"padding:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:10px;\n"
"background-color: rgb(180, 235, 255);\n"
"}")
        self.cam2.setCheckable(True)
        self.cam2.setAutoRepeat(True)

        self.horizontalLayout.addWidget(self.cam2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.cam3 = QPushButton(self.frameCam)
        self.cam3.setObjectName(u"cam3")
        self.cam3.setFont(font4)
        self.cam3.setCursor(QCursor(Qt.PointingHandCursor))
        self.cam3.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"border:4px solid rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"padding:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:10px;\n"
"background-color: rgb(180, 235, 255);\n"
"}")
        self.cam3.setCheckable(True)
        self.cam3.setAutoRepeat(True)

        self.horizontalLayout.addWidget(self.cam3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.gridLayout_2.addWidget(self.frameCam, 1, 0, 1, 2, Qt.AlignVCenter)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 5)
        self.gridLayout_2.setColumnStretch(2, 2)

        self.gridLayout_6.addWidget(self.frameTop_1, 0, 0, 1, 1)

        self.contentStackedWidget_1 = QStackedWidget(self.centralwidget)
        self.contentStackedWidget_1.setObjectName(u"contentStackedWidget_1")
        sizePolicy2.setHeightForWidth(self.contentStackedWidget_1.sizePolicy().hasHeightForWidth())
        self.contentStackedWidget_1.setSizePolicy(sizePolicy2)
        self.contentStackedWidget_1.setMaximumSize(QSize(1280, 960))
        self.contentStackedWidget_1.setStyleSheet(u"QStackedWidget#contentStackedWidget_1{\n"
"padding: 0px;\n"
"}")
        self.contentPage_1 = QWidget()
        self.contentPage_1.setObjectName(u"contentPage_1")
        self.gridLayout_3 = QGridLayout(self.contentPage_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.frameBodylist = QFrame(self.contentPage_1)
        self.frameBodylist.setObjectName(u"frameBodylist")
        self.frameBodylist.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.frameBodylist.sizePolicy().hasHeightForWidth())
        self.frameBodylist.setSizePolicy(sizePolicy2)
        self.frameBodylist.setMinimumSize(QSize(180, 0))
        self.frameBodylist.setMaximumSize(QSize(256, 960))
        self.frameBodylist.setFont(font4)
        self.frameBodylist.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(202, 202, 255, 159), stop:1 rgba(198, 240, 255, 255));\n"
"border-radius:20px;")
        self.frameBodylist.setFrameShape(QFrame.StyledPanel)
        self.frameBodylist.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameBodylist)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bodyTreeWidget = QTreeWidget(self.frameBodylist)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.bodyTreeWidget.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.bodyTreeWidget)
        __qtreewidgetitem1.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem1.setFont(0, font4);
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setFont(0, font4);
        __qtreewidgetitem3 = QTreeWidgetItem(self.bodyTreeWidget)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4 = QTreeWidgetItem(self.bodyTreeWidget)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5 = QTreeWidgetItem(self.bodyTreeWidget)
        QTreeWidgetItem(__qtreewidgetitem5)
        __qtreewidgetitem6 = QTreeWidgetItem(self.bodyTreeWidget)
        QTreeWidgetItem(__qtreewidgetitem6)
        QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7 = QTreeWidgetItem(self.bodyTreeWidget)
        QTreeWidgetItem(__qtreewidgetitem7)
        __qtreewidgetitem8 = QTreeWidgetItem(self.bodyTreeWidget)
        QTreeWidgetItem(__qtreewidgetitem8)
        __qtreewidgetitem9 = QTreeWidgetItem(self.bodyTreeWidget)
        QTreeWidgetItem(__qtreewidgetitem9)
        self.bodyTreeWidget.setObjectName(u"bodyTreeWidget")
        self.bodyTreeWidget.setEnabled(False)
        font5 = QFont()
        font5.setFamilies([u"\u6977\u4f53"])
        font5.setPointSize(15)
        font5.setKerning(True)
        font5.setHintingPreference(QFont.PreferDefaultHinting)
        self.bodyTreeWidget.setFont(font5)
        self.bodyTreeWidget.setAutoFillBackground(False)
        self.bodyTreeWidget.setStyleSheet(u"QTreeWidget{\n"
"border-radius:14px;\n"
"background-color: transparent;\n"
"}\n"
"QTreeWidget::item {\n"
"margin-top:5px;\n"
"padding:5px 0 5px 5px;\n"
"}\n"
"QTreeWidget::item:hover {\n"
"background-color: rgb(224, 241, 255);\n"
"border-left: 3px solid rgb(0, 85, 255);\n"
"}\n"
"QTreeWidget::item:selected {\n"
"background-color: rgb(207, 251, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-left: 3px solid rgb(162, 240, 119);\n"
"}")
        self.bodyTreeWidget.setFrameShadow(QFrame.Raised)
        self.bodyTreeWidget.setAutoScroll(True)
        self.bodyTreeWidget.setAutoScrollMargin(16)
        self.bodyTreeWidget.setAlternatingRowColors(False)
        self.bodyTreeWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.bodyTreeWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.bodyTreeWidget.setAutoExpandDelay(-1)
        self.bodyTreeWidget.setIndentation(26)
        self.bodyTreeWidget.setUniformRowHeights(False)
        self.bodyTreeWidget.setItemsExpandable(True)
        self.bodyTreeWidget.setSortingEnabled(False)
        self.bodyTreeWidget.setAnimated(True)
        self.bodyTreeWidget.setAllColumnsShowFocus(True)
        self.bodyTreeWidget.setWordWrap(False)
        self.bodyTreeWidget.setColumnCount(1)
        self.bodyTreeWidget.header().setVisible(False)

        self.verticalLayout.addWidget(self.bodyTreeWidget)


        self.gridLayout_3.addWidget(self.frameBodylist, 0, 0, 2, 1)

        self.frameTimer_1 = QFrame(self.contentPage_1)
        self.frameTimer_1.setObjectName(u"frameTimer_1")
        self.frameTimer_1.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frameTimer_1.sizePolicy().hasHeightForWidth())
        self.frameTimer_1.setSizePolicy(sizePolicy5)
        self.frameTimer_1.setMinimumSize(QSize(170, 0))
        self.frameTimer_1.setMaximumSize(QSize(256, 960))
        self.frameTimer_1.setFont(font)
        self.frameTimer_1.setStyleSheet(u"border-radius:20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(242, 255, 236, 255), stop:1 rgba(205, 242, 255, 198));\n"
"padding:0px;\n"
"                                           ")
        self.frameTimer_1.setFrameShape(QFrame.StyledPanel)
        self.frameTimer_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameTimer_1)
        self.verticalLayout_2.setSpacing(35)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.timerLcdNumber_1 = QLCDNumber(self.frameTimer_1)
        self.timerLcdNumber_1.setObjectName(u"timerLcdNumber_1")
        sizePolicy2.setHeightForWidth(self.timerLcdNumber_1.sizePolicy().hasHeightForWidth())
        self.timerLcdNumber_1.setSizePolicy(sizePolicy2)
        self.timerLcdNumber_1.setMinimumSize(QSize(0, 80))
        self.timerLcdNumber_1.setMaximumSize(QSize(16777215, 250))
        self.timerLcdNumber_1.setStyleSheet(u"border: 5px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color:transparent;\n"
"margin-left:5px;\n"
"margin-right:5px;")
        self.timerLcdNumber_1.setFrameShape(QFrame.Box)
        self.timerLcdNumber_1.setMode(QLCDNumber.Dec)
        self.timerLcdNumber_1.setSegmentStyle(QLCDNumber.Flat)
        self.timerLcdNumber_1.setProperty("intValue", 0)

        self.verticalLayout_2.addWidget(self.timerLcdNumber_1)

        self.frameWave_1 = QFrame(self.frameTimer_1)
        self.frameWave_1.setObjectName(u"frameWave_1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frameWave_1.sizePolicy().hasHeightForWidth())
        self.frameWave_1.setSizePolicy(sizePolicy6)
        self.horizontalLayout_2 = QHBoxLayout(self.frameWave_1)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.rayLabel_1 = QLabel(self.frameWave_1)
        self.rayLabel_1.setObjectName(u"rayLabel_1")
        sizePolicy2.setHeightForWidth(self.rayLabel_1.sizePolicy().hasHeightForWidth())
        self.rayLabel_1.setSizePolicy(sizePolicy2)
        self.rayLabel_1.setMinimumSize(QSize(41, 31))
        self.rayLabel_1.setMaximumSize(QSize(61, 61))
        self.rayLabel_1.setStyleSheet(u"background-color: transparent;")
        self.rayLabel_1.setPixmap(QPixmap(u":/images/camera.png"))
        self.rayLabel_1.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.rayLabel_1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.waveLabel_1 = QLabel(self.frameWave_1)
        self.waveLabel_1.setObjectName(u"waveLabel_1")
        sizePolicy2.setHeightForWidth(self.waveLabel_1.sizePolicy().hasHeightForWidth())
        self.waveLabel_1.setSizePolicy(sizePolicy2)
        self.waveLabel_1.setMinimumSize(QSize(0, 60))
        self.waveLabel_1.setMaximumSize(QSize(150, 100))
        self.waveLabel_1.setStyleSheet(u"background-color: transparent;")
        self.waveLabel_1.setPixmap(QPixmap(u":/images/wave.gif"))
        self.waveLabel_1.setScaledContents(True)
        self.waveLabel_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.waveLabel_1, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.frameWave_1)

        self.frameCtrl_1 = QFrame(self.frameTimer_1)
        self.frameCtrl_1.setObjectName(u"frameCtrl_1")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frameCtrl_1.sizePolicy().hasHeightForWidth())
        self.frameCtrl_1.setSizePolicy(sizePolicy7)
        self.frameCtrl_1.setMaximumSize(QSize(256, 120))
        self.frameCtrl_1.setStyleSheet(u"background-color:transparent;")
        self.horizontalLayout_3 = QHBoxLayout(self.frameCtrl_1)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.btnStart_1 = QPushButton(self.frameCtrl_1)
        self.spsButtonGroup_1 = QButtonGroup(MainWindow)
        self.spsButtonGroup_1.setObjectName(u"spsButtonGroup_1")
        self.spsButtonGroup_1.addButton(self.btnStart_1)
        self.btnStart_1.setObjectName(u"btnStart_1")
        sizePolicy2.setHeightForWidth(self.btnStart_1.sizePolicy().hasHeightForWidth())
        self.btnStart_1.setSizePolicy(sizePolicy2)
        self.btnStart_1.setMinimumSize(QSize(50, 50))
        self.btnStart_1.setMaximumSize(QSize(50, 50))
        self.btnStart_1.setStyleSheet(u"QPushButton#btnStart_1{\n"
"background-color: transparent;\n"
"border-image: url(:/images/start.png);\n"
"}\n"
"QPushButton#btnStart_1:checked{\n"
"border-image: url(:/images/starton.png);\n"
"}")
        self.btnStart_1.setCheckable(True)
        self.btnStart_1.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btnStart_1, 0, Qt.AlignHCenter)

        self.btnPause_1 = QPushButton(self.frameCtrl_1)
        self.spsButtonGroup_1.addButton(self.btnPause_1)
        self.btnPause_1.setObjectName(u"btnPause_1")
        sizePolicy2.setHeightForWidth(self.btnPause_1.sizePolicy().hasHeightForWidth())
        self.btnPause_1.setSizePolicy(sizePolicy2)
        self.btnPause_1.setMinimumSize(QSize(50, 50))
        self.btnPause_1.setMaximumSize(QSize(50, 50))
        self.btnPause_1.setStyleSheet(u"QPushButton#btnPause_1{\n"
"background-color: transparent;\n"
"border-image: url(:/images/pause.png);\n"
"}\n"
"QPushButton#btnPause_1:checked{\n"
"border-image: url(:/images/pauseon.png);\n"
"}\n"
"QPushButton#btnPause_1:unchecked{\n"
"background-color: transparent;\n"
"border-image: url(:/images/pause.png);\n"
"}")
        self.btnPause_1.setCheckable(True)
        self.btnPause_1.setAutoRepeat(True)
        self.btnPause_1.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btnPause_1, 0, Qt.AlignHCenter)

        self.btnStop_1 = QPushButton(self.frameCtrl_1)
        self.spsButtonGroup_1.addButton(self.btnStop_1)
        self.btnStop_1.setObjectName(u"btnStop_1")
        sizePolicy2.setHeightForWidth(self.btnStop_1.sizePolicy().hasHeightForWidth())
        self.btnStop_1.setSizePolicy(sizePolicy2)
        self.btnStop_1.setMinimumSize(QSize(50, 50))
        self.btnStop_1.setMaximumSize(QSize(50, 50))
        self.btnStop_1.setStyleSheet(u"QPushButton#btnStop_1{\n"
"background-color: transparent;\n"
"border-image: url(:/images/stop.png);\n"
"}\n"
"QPushButton#btnStop_1:checked{\n"
"border-image: url(:/images/stopon.png);\n"
"}\n"
"QPushButton#btnStop_1:unchecked{\n"
"border-image: url(:/images/stop.png);\n"
"}")
        self.btnStop_1.setCheckable(True)
        self.btnStop_1.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btnStop_1, 0, Qt.AlignHCenter)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.frameCtrl_1)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)

        self.gridLayout_3.addWidget(self.frameTimer_1, 0, 2, 2, 1)

        self.framePointAdjust = QFrame(self.contentPage_1)
        self.framePointAdjust.setObjectName(u"framePointAdjust")
        self.framePointAdjust.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.framePointAdjust.sizePolicy().hasHeightForWidth())
        self.framePointAdjust.setSizePolicy(sizePolicy2)
        self.framePointAdjust.setMinimumSize(QSize(400, 0))
        self.framePointAdjust.setMaximumSize(QSize(768, 16777215))
        self.framePointAdjust.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(205, 242, 255, 198), stop:1 rgba(242, 255, 236, 255));")
        self.framePointAdjust.setFrameShape(QFrame.StyledPanel)
        self.framePointAdjust.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.framePointAdjust)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.savePointPushButton_1 = QPushButton(self.framePointAdjust)
        self.savePointPushButton_1.setObjectName(u"savePointPushButton_1")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.savePointPushButton_1.sizePolicy().hasHeightForWidth())
        self.savePointPushButton_1.setSizePolicy(sizePolicy8)
        self.savePointPushButton_1.setFont(font2)
        self.savePointPushButton_1.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"border:4px solid rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"margin-left:30px;\n"
"margin-right:20px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:10px;\n"
"background-color: rgb(180, 235, 255);\n"
"padding-top:13px;\n"
"padding-left:15px;\n"
"}")
        self.savePointPushButton_1.setCheckable(True)
        self.savePointPushButton_1.setAutoRepeat(True)

        self.gridLayout_4.addWidget(self.savePointPushButton_1, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pullPushButton_1 = QPushButton(self.framePointAdjust)
        self.pullPushButton_1.setObjectName(u"pullPushButton_1")
        sizePolicy8.setHeightForWidth(self.pullPushButton_1.sizePolicy().hasHeightForWidth())
        self.pullPushButton_1.setSizePolicy(sizePolicy8)
        self.pullPushButton_1.setFont(font2)
        self.pullPushButton_1.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"border:4px solid rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"margin-left:30px;\n"
"margin-right:20px;\n"
"padding:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:10px;\n"
"background-color: rgb(180, 235, 255);\n"
"padding-top:13px;\n"
"padding-left:15px;\n"
"}")
        self.pullPushButton_1.setCheckable(True)
        self.pullPushButton_1.setAutoRepeat(True)

        self.gridLayout_4.addWidget(self.pullPushButton_1, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pointLabel = QLabel(self.framePointAdjust)
        self.pointLabel.setObjectName(u"pointLabel")
        sizePolicy2.setHeightForWidth(self.pointLabel.sizePolicy().hasHeightForWidth())
        self.pointLabel.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setFamilies([u"\u6977\u4f53"])
        font6.setPointSize(14)
        self.pointLabel.setFont(font6)
        self.pointLabel.setStyleSheet(u"background-color:transparent;")
        self.pointLabel.setScaledContents(True)

        self.gridLayout_4.addWidget(self.pointLabel, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.adjustLabel = QLabel(self.framePointAdjust)
        self.adjustLabel.setObjectName(u"adjustLabel")
        self.adjustLabel.setFont(font6)
        self.adjustLabel.setStyleSheet(u"background-color:transparent;\n"
"")

        self.gridLayout_4.addWidget(self.adjustLabel, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.adjustStackedWidget_1 = QStackedWidget(self.framePointAdjust)
        self.adjustStackedWidget_1.setObjectName(u"adjustStackedWidget_1")
        self.adjustStackedWidget_1.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.adjustStackedWidget_1.sizePolicy().hasHeightForWidth())
        self.adjustStackedWidget_1.setSizePolicy(sizePolicy2)
        self.adjustStackedWidget_1.setStyleSheet(u"#adjustStackedWidget_1{\n"
"background-color:transparent;\n"
"}")
        self.adjustStackedWidget_1.setFrameShape(QFrame.StyledPanel)
        self.adjustStackedWidget_1.setFrameShadow(QFrame.Raised)
        self.adjustPage_1 = QWidget()
        self.adjustPage_1.setObjectName(u"adjustPage_1")
        self.adjustPage_1.setStyleSheet(u"background-color:transparent;")
        self.front = QPushButton(self.adjustPage_1)
        self.front.setObjectName(u"front")
        self.front.setGeometry(QRect(70, 0, 61, 51))
        sizePolicy2.setHeightForWidth(self.front.sizePolicy().hasHeightForWidth())
        self.front.setSizePolicy(sizePolicy2)
        self.front.setFont(font6)
        self.front.setStyleSheet(u"QPushButton{\n"
"border-image: url(:images/up.png);\n"
"color: rgb(255, 255, 255);\n"
"padding:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:images/upon.png);\n"
"padding-bottom:5px;\n"
"}")
        self.front.setCheckable(True)
        self.front.setAutoRepeat(True)
        self.front.setAutoRepeatDelay(300)
        self.front.setAutoRepeatInterval(30)
        self.left = QPushButton(self.adjustPage_1)
        self.left.setObjectName(u"left")
        self.left.setGeometry(QRect(20, 40, 61, 51))
        sizePolicy2.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy2)
        self.left.setFont(font6)
        self.left.setStyleSheet(u"QPushButton{\n"
"border-image: url(:images/left.png);\n"
"color: rgb(255, 255, 255);\n"
"padding:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:images/lefton.png);\n"
"padding-top:5px;\n"
"padding-right:5px;\n"
"}")
        self.left.setCheckable(True)
        self.left.setAutoRepeat(True)
        self.left.setAutoRepeatInterval(30)
        self.back = QPushButton(self.adjustPage_1)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(70, 80, 61, 51))
        sizePolicy2.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy2)
        self.back.setFont(font6)
        self.back.setStyleSheet(u"QPushButton{\n"
"border-image: url(:images/down.png);\n"
"padding:0px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:images/downon.png);\n"
"padding-top:5px;\n"
"}")
        self.back.setCheckable(True)
        self.back.setAutoRepeat(True)
        self.back.setAutoRepeatInterval(30)
        self.right = QPushButton(self.adjustPage_1)
        self.right.setObjectName(u"right")
        self.right.setGeometry(QRect(120, 40, 61, 51))
        sizePolicy2.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy2)
        self.right.setFont(font6)
        self.right.setStyleSheet(u"QPushButton{\n"
"border-image: url(:images/right.png);\n"
"color: rgb(255, 255, 255);\n"
"padding:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:images/righton.png);\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"}")
        self.right.setCheckable(True)
        self.right.setAutoRepeat(True)
        self.right.setAutoRepeatInterval(30)
        self.switch_2 = QPushButton(self.adjustPage_1)
        self.switch_2.setObjectName(u"switch_2")
        self.switch_2.setGeometry(QRect(70, 40, 61, 51))
        sizePolicy2.setHeightForWidth(self.switch_2.sizePolicy().hasHeightForWidth())
        self.switch_2.setSizePolicy(sizePolicy2)
        self.switch_2.setStyleSheet(u"QPushButton{\n"
"border-image: url(:images/switch.png);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:images/switchon.png);\n"
"}")
        self.switch_2.setAutoRepeat(True)
        self.adjustStackedWidget_1.addWidget(self.adjustPage_1)
        self.adjustPage_2 = QWidget()
        self.adjustPage_2.setObjectName(u"adjustPage_2")
        self.adjustPage_2.setStyleSheet(u"background-color:transparent;")
        self.switch_1 = QPushButton(self.adjustPage_2)
        self.switch_1.setObjectName(u"switch_1")
        self.switch_1.setGeometry(QRect(70, 40, 61, 51))
        sizePolicy2.setHeightForWidth(self.switch_1.sizePolicy().hasHeightForWidth())
        self.switch_1.setSizePolicy(sizePolicy2)
        self.switch_1.setStyleSheet(u"QPushButton{\n"
"border-image: url(:images/switch.png);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:images/switchon.png);\n"
"}")
        self.switch_1.setAutoRepeat(True)
        self.rightrot = QPushButton(self.adjustPage_2)
        self.rightrot.setObjectName(u"rightrot")
        self.rightrot.setGeometry(QRect(120, 40, 61, 51))
        sizePolicy2.setHeightForWidth(self.rightrot.sizePolicy().hasHeightForWidth())
        self.rightrot.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setFamilies([u"\u6977\u4f53"])
        font7.setPointSize(13)
        self.rightrot.setFont(font7)
        self.rightrot.setStyleSheet(u"QPushButton{\n"
"border-image: url(:images/right.png);\n"
"color: rgb(255, 255, 255);\n"
"padding:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:images/righton.png);\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"}")
        self.rightrot.setCheckable(True)
        self.rightrot.setAutoRepeat(True)
        self.rightrot.setAutoRepeatInterval(30)
        self.up = QPushButton(self.adjustPage_2)
        self.up.setObjectName(u"up")
        self.up.setGeometry(QRect(70, 0, 61, 51))
        sizePolicy2.setHeightForWidth(self.up.sizePolicy().hasHeightForWidth())
        self.up.setSizePolicy(sizePolicy2)
        self.up.setFont(font6)
        self.up.setStyleSheet(u"QPushButton{\n"
"border-image: url(:images/up.png);\n"
"color: rgb(255, 255, 255);\n"
"padding:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:images/upon.png);\n"
"padding-bottom:5px;\n"
"}")
        self.up.setCheckable(True)
        self.up.setAutoRepeat(True)
        self.up.setAutoRepeatInterval(30)
        self.down = QPushButton(self.adjustPage_2)
        self.down.setObjectName(u"down")
        self.down.setGeometry(QRect(70, 80, 61, 51))
        sizePolicy2.setHeightForWidth(self.down.sizePolicy().hasHeightForWidth())
        self.down.setSizePolicy(sizePolicy2)
        self.down.setFont(font6)
        self.down.setStyleSheet(u"QPushButton{\n"
"border-image: url(:images/down.png);\n"
"color: rgb(255, 255, 255);\n"
"padding:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:images/downon.png);\n"
"padding-top:5px;\n"
"}")
        self.down.setCheckable(True)
        self.down.setAutoRepeat(True)
        self.down.setAutoRepeatInterval(30)
        self.leftrot = QPushButton(self.adjustPage_2)
        self.leftrot.setObjectName(u"leftrot")
        self.leftrot.setGeometry(QRect(20, 40, 61, 51))
        sizePolicy2.setHeightForWidth(self.leftrot.sizePolicy().hasHeightForWidth())
        self.leftrot.setSizePolicy(sizePolicy2)
        self.leftrot.setFont(font7)
        self.leftrot.setCursor(QCursor(Qt.ArrowCursor))
        self.leftrot.setStyleSheet(u"QPushButton{\n"
"border-image: url(:images/left.png);\n"
"color: rgb(255, 255, 255);\n"
"padding:0px;\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:images/lefton.png);\n"
"padding-top:5px;\n"
"padding-right:5px;\n"
"}")
        self.leftrot.setCheckable(True)
        self.leftrot.setAutoRepeat(True)
        self.leftrot.setAutoRepeatInterval(30)
        self.adjustStackedWidget_1.addWidget(self.adjustPage_2)

        self.gridLayout_4.addWidget(self.adjustStackedWidget_1, 1, 1, 2, 1)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setRowStretch(2, 2)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)

        self.gridLayout_3.addWidget(self.framePointAdjust, 1, 1, 1, 1)

        self.framePara_1 = QFrame(self.contentPage_1)
        self.framePara_1.setObjectName(u"framePara_1")
        self.framePara_1.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.framePara_1.sizePolicy().hasHeightForWidth())
        self.framePara_1.setSizePolicy(sizePolicy2)
        self.framePara_1.setMinimumSize(QSize(400, 0))
        self.framePara_1.setMaximumSize(QSize(768, 16777215))
        self.framePara_1.setFont(font)
        self.framePara_1.setAutoFillBackground(False)
        self.framePara_1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(242, 255, 236, 255), stop:1 rgba(205, 242, 255, 198));\n"
"border-radius:20px;")
        self.framePara_1.setFrameShape(QFrame.StyledPanel)
        self.framePara_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.framePara_1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(9)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(9, -1, 9, -1)
        self.planLabel_1 = QLabel(self.framePara_1)
        self.planLabel_1.setObjectName(u"planLabel_1")
        self.planLabel_1.setFont(font6)
        self.planLabel_1.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_5.addWidget(self.planLabel_1, 0, 0, 1, 1, Qt.AlignLeft)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(4)
        self.zkbLabel_1 = QLabel(self.framePara_1)
        self.zkbLabel_1.setObjectName(u"zkbLabel_1")
        self.zkbLabel_1.setEnabled(False)
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.zkbLabel_1.sizePolicy().hasHeightForWidth())
        self.zkbLabel_1.setSizePolicy(sizePolicy9)
        self.zkbLabel_1.setFont(font6)
        self.zkbLabel_1.setStyleSheet(u"background-color:transparent;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.zkbLabel_1)

        self.zkbSpinBox_1 = QSpinBox(self.framePara_1)
        self.zkbSpinBox_1.setObjectName(u"zkbSpinBox_1")
        self.zkbSpinBox_1.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.zkbSpinBox_1.sizePolicy().hasHeightForWidth())
        self.zkbSpinBox_1.setSizePolicy(sizePolicy8)
        self.zkbSpinBox_1.setMinimumSize(QSize(0, 30))
        self.zkbSpinBox_1.setMaximumSize(QSize(16777215, 50))
        font8 = QFont()
        font8.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font8.setPointSize(12)
        self.zkbSpinBox_1.setFont(font8)
        self.zkbSpinBox_1.setStyleSheet(u"background-color:transparent;\n"
"")
        self.zkbSpinBox_1.setMinimum(10)
        self.zkbSpinBox_1.setMaximum(100)
        self.zkbSpinBox_1.setSingleStep(10)
        self.zkbSpinBox_1.setStepType(QAbstractSpinBox.DefaultStepType)
        self.zkbSpinBox_1.setValue(10)
        self.zkbSpinBox_1.setDisplayIntegerBase(10)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.zkbSpinBox_1)

        self.freqLabel_1 = QLabel(self.framePara_1)
        self.freqLabel_1.setObjectName(u"freqLabel_1")
        self.freqLabel_1.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.freqLabel_1.sizePolicy().hasHeightForWidth())
        self.freqLabel_1.setSizePolicy(sizePolicy9)
        self.freqLabel_1.setFont(font6)
        self.freqLabel_1.setStyleSheet(u"background-color:transparent;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.freqLabel_1)

        self.freqSpinBox_1 = QSpinBox(self.framePara_1)
        self.freqSpinBox_1.setObjectName(u"freqSpinBox_1")
        self.freqSpinBox_1.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.freqSpinBox_1.sizePolicy().hasHeightForWidth())
        self.freqSpinBox_1.setSizePolicy(sizePolicy8)
        self.freqSpinBox_1.setMinimumSize(QSize(0, 30))
        self.freqSpinBox_1.setMaximumSize(QSize(16777215, 50))
        self.freqSpinBox_1.setFont(font8)
        self.freqSpinBox_1.setStyleSheet(u"background-color:transparent;\n"
"")
        self.freqSpinBox_1.setMinimum(1)
        self.freqSpinBox_1.setMaximum(3)
        self.freqSpinBox_1.setSingleStep(2)
        self.freqSpinBox_1.setDisplayIntegerBase(10)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.freqSpinBox_1)

        self.speedLabel_1 = QLabel(self.framePara_1)
        self.speedLabel_1.setObjectName(u"speedLabel_1")
        self.speedLabel_1.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.speedLabel_1.sizePolicy().hasHeightForWidth())
        self.speedLabel_1.setSizePolicy(sizePolicy9)
        self.speedLabel_1.setFont(font6)
        self.speedLabel_1.setStyleSheet(u"background-color:transparent;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.speedLabel_1)

        self.speedSpinBox_1 = QSpinBox(self.framePara_1)
        self.speedSpinBox_1.setObjectName(u"speedSpinBox_1")
        self.speedSpinBox_1.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.speedSpinBox_1.sizePolicy().hasHeightForWidth())
        self.speedSpinBox_1.setSizePolicy(sizePolicy8)
        self.speedSpinBox_1.setMinimumSize(QSize(0, 30))
        self.speedSpinBox_1.setMaximumSize(QSize(16777215, 50))
        self.speedSpinBox_1.setFont(font8)
        self.speedSpinBox_1.setStyleSheet(u"background-color:transparent;\n"
"")
        self.speedSpinBox_1.setMinimum(1)
        self.speedSpinBox_1.setMaximum(10)
        self.speedSpinBox_1.setDisplayIntegerBase(10)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.speedSpinBox_1)

        self.soundLabel_1 = QLabel(self.framePara_1)
        self.soundLabel_1.setObjectName(u"soundLabel_1")
        self.soundLabel_1.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.soundLabel_1.sizePolicy().hasHeightForWidth())
        self.soundLabel_1.setSizePolicy(sizePolicy9)
        self.soundLabel_1.setFont(font6)
        self.soundLabel_1.setStyleSheet(u"background-color:transparent;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.soundLabel_1)

        self.soundDoubleSpinBox_1 = QDoubleSpinBox(self.framePara_1)
        self.soundDoubleSpinBox_1.setObjectName(u"soundDoubleSpinBox_1")
        self.soundDoubleSpinBox_1.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.soundDoubleSpinBox_1.sizePolicy().hasHeightForWidth())
        self.soundDoubleSpinBox_1.setSizePolicy(sizePolicy8)
        self.soundDoubleSpinBox_1.setMinimumSize(QSize(0, 30))
        self.soundDoubleSpinBox_1.setMaximumSize(QSize(16777215, 50))
        self.soundDoubleSpinBox_1.setFont(font8)
        self.soundDoubleSpinBox_1.setStyleSheet(u"background-color:transparent;\n"
"")
        self.soundDoubleSpinBox_1.setMinimum(0.100000000000000)
        self.soundDoubleSpinBox_1.setMaximum(3.000000000000000)
        self.soundDoubleSpinBox_1.setSingleStep(0.100000000000000)
        self.soundDoubleSpinBox_1.setValue(0.100000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.soundDoubleSpinBox_1)

        self.timeLabel_1 = QLabel(self.framePara_1)
        self.timeLabel_1.setObjectName(u"timeLabel_1")
        self.timeLabel_1.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.timeLabel_1.sizePolicy().hasHeightForWidth())
        self.timeLabel_1.setSizePolicy(sizePolicy9)
        self.timeLabel_1.setFont(font6)
        self.timeLabel_1.setStyleSheet(u"background-color:transparent;")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.timeLabel_1)

        self.timeSpinBox_1 = QSpinBox(self.framePara_1)
        self.timeSpinBox_1.setObjectName(u"timeSpinBox_1")
        self.timeSpinBox_1.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.timeSpinBox_1.sizePolicy().hasHeightForWidth())
        self.timeSpinBox_1.setSizePolicy(sizePolicy8)
        self.timeSpinBox_1.setMinimumSize(QSize(0, 30))
        self.timeSpinBox_1.setMaximumSize(QSize(16777215, 50))
        self.timeSpinBox_1.setFont(font8)
        self.timeSpinBox_1.setStyleSheet(u"background-color:transparent;\n"
"")
        self.timeSpinBox_1.setMinimum(1)
        self.timeSpinBox_1.setMaximum(20)
        self.timeSpinBox_1.setDisplayIntegerBase(10)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.timeSpinBox_1)

        self.strengthLabel = QLabel(self.framePara_1)
        self.strengthLabel.setObjectName(u"strengthLabel")
        self.strengthLabel.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.strengthLabel.sizePolicy().hasHeightForWidth())
        self.strengthLabel.setSizePolicy(sizePolicy9)
        self.strengthLabel.setFont(font6)
        self.strengthLabel.setStyleSheet(u"background-color:transparent;\n"
"")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.strengthLabel)

        self.strengthSpinBox_1 = QSpinBox(self.framePara_1)
        self.strengthSpinBox_1.setObjectName(u"strengthSpinBox_1")
        self.strengthSpinBox_1.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.strengthSpinBox_1.sizePolicy().hasHeightForWidth())
        self.strengthSpinBox_1.setSizePolicy(sizePolicy8)
        self.strengthSpinBox_1.setMinimumSize(QSize(0, 30))
        self.strengthSpinBox_1.setMaximumSize(QSize(16777215, 50))
        self.strengthSpinBox_1.setFont(font8)
        self.strengthSpinBox_1.setStyleSheet(u"background-color:transparent;\n"
"")
        self.strengthSpinBox_1.setMinimum(1)
        self.strengthSpinBox_1.setMaximum(50)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.strengthSpinBox_1)


        self.gridLayout_5.addLayout(self.formLayout, 0, 1, 3, 1)

        self.planComboBox_1 = QComboBox(self.framePara_1)
        self.planComboBox_1.addItem("")
        self.planComboBox_1.setObjectName(u"planComboBox_1")
        self.planComboBox_1.setFont(font6)

        self.gridLayout_5.addWidget(self.planComboBox_1, 1, 0, 1, 1)

        self.saveCancelStackedWidget_1 = QStackedWidget(self.framePara_1)
        self.saveCancelStackedWidget_1.setObjectName(u"saveCancelStackedWidget_1")
        self.saveCancelStackedWidget_1.setStyleSheet(u"background-color:transparent;")
        self.saveSelfSetPage_1 = QWidget()
        self.saveSelfSetPage_1.setObjectName(u"saveSelfSetPage_1")
        self.horizontalLayout_6 = QHBoxLayout(self.saveSelfSetPage_1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.saveSelfPushButton_1 = QPushButton(self.saveSelfSetPage_1)
        self.saveSelfPushButton_1.setObjectName(u"saveSelfPushButton_1")
        self.saveSelfPushButton_1.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.saveSelfPushButton_1.sizePolicy().hasHeightForWidth())
        self.saveSelfPushButton_1.setSizePolicy(sizePolicy2)
        self.saveSelfPushButton_1.setFont(font2)
        self.saveSelfPushButton_1.setStyleSheet(u"background-color: rgb(49, 192, 253);\n"
"border-radius:10px;\n"
"padding:5px;")
        self.saveSelfPushButton_1.setCheckable(True)
        self.saveSelfPushButton_1.setAutoRepeat(True)
        self.saveSelfPushButton_1.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.saveSelfPushButton_1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.cancelSelfPushButton_1 = QPushButton(self.saveSelfSetPage_1)
        self.cancelSelfPushButton_1.setObjectName(u"cancelSelfPushButton_1")
        sizePolicy2.setHeightForWidth(self.cancelSelfPushButton_1.sizePolicy().hasHeightForWidth())
        self.cancelSelfPushButton_1.setSizePolicy(sizePolicy2)
        self.cancelSelfPushButton_1.setFont(font2)
        self.cancelSelfPushButton_1.setStyleSheet(u"background-color: rgb(49, 192, 253);\n"
"border-radius:10px;\n"
"padding:5px;")
        self.cancelSelfPushButton_1.setCheckable(True)
        self.cancelSelfPushButton_1.setAutoRepeat(True)
        self.cancelSelfPushButton_1.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.cancelSelfPushButton_1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.saveCancelStackedWidget_1.addWidget(self.saveSelfSetPage_1)
        self.saveSelfSetPage_0 = QWidget()
        self.saveSelfSetPage_0.setObjectName(u"saveSelfSetPage_0")
        self.saveCancelStackedWidget_1.addWidget(self.saveSelfSetPage_0)

        self.gridLayout_5.addWidget(self.saveCancelStackedWidget_1, 2, 0, 1, 1)

        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_5.setRowStretch(1, 1)
        self.gridLayout_5.setRowStretch(2, 1)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 2)

        self.gridLayout_3.addWidget(self.framePara_1, 0, 1, 1, 1)

        self.gridLayout_3.setRowStretch(0, 3)
        self.gridLayout_3.setRowStretch(1, 2)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.contentStackedWidget_1.addWidget(self.contentPage_1)
        self.contentPage_2 = QWidget()
        self.contentPage_2.setObjectName(u"contentPage_2")
        self.horizontalLayout_7 = QHBoxLayout(self.contentPage_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.framePara_2 = QFrame(self.contentPage_2)
        self.framePara_2.setObjectName(u"framePara_2")
        sizePolicy2.setHeightForWidth(self.framePara_2.sizePolicy().hasHeightForWidth())
        self.framePara_2.setSizePolicy(sizePolicy2)
        self.framePara_2.setMinimumSize(QSize(400, 0))
        self.framePara_2.setMaximumSize(QSize(1024, 16777215))
        self.framePara_2.setFont(font)
        self.framePara_2.setAutoFillBackground(False)
        self.framePara_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(242, 255, 236, 255), stop:1 rgba(205, 242, 255, 198));\n"
"border-radius:20px;\n"
"padding:20px;")
        self.framePara_2.setFrameShape(QFrame.StyledPanel)
        self.framePara_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.framePara_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.planLabel_2 = QLabel(self.framePara_2)
        self.planLabel_2.setObjectName(u"planLabel_2")
        self.planLabel_2.setFont(font6)
        self.planLabel_2.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_7.addWidget(self.planLabel_2, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.planComboBox_2 = QComboBox(self.framePara_2)
        self.planComboBox_2.addItem("")
        self.planComboBox_2.setObjectName(u"planComboBox_2")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.planComboBox_2.sizePolicy().hasHeightForWidth())
        self.planComboBox_2.setSizePolicy(sizePolicy10)
        self.planComboBox_2.setMinimumSize(QSize(180, 30))
        self.planComboBox_2.setMaximumSize(QSize(180, 16777215))
        self.planComboBox_2.setFont(font6)

        self.gridLayout_7.addWidget(self.planComboBox_2, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.zkbLabel_2 = QLabel(self.framePara_2)
        self.zkbLabel_2.setObjectName(u"zkbLabel_2")
        self.zkbLabel_2.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.zkbLabel_2.sizePolicy().hasHeightForWidth())
        self.zkbLabel_2.setSizePolicy(sizePolicy9)
        self.zkbLabel_2.setFont(font6)
        self.zkbLabel_2.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_7.addWidget(self.zkbLabel_2, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.zkbSpinBox_2 = QSpinBox(self.framePara_2)
        self.zkbSpinBox_2.setObjectName(u"zkbSpinBox_2")
        self.zkbSpinBox_2.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.zkbSpinBox_2.sizePolicy().hasHeightForWidth())
        self.zkbSpinBox_2.setSizePolicy(sizePolicy6)
        self.zkbSpinBox_2.setMinimumSize(QSize(140, 30))
        self.zkbSpinBox_2.setMaximumSize(QSize(140, 50))
        self.zkbSpinBox_2.setSizeIncrement(QSize(0, 0))
        self.zkbSpinBox_2.setBaseSize(QSize(0, 0))
        self.zkbSpinBox_2.setFont(font8)
        self.zkbSpinBox_2.setStyleSheet(u"background-color:transparent;\n"
"padding:0px;\n"
"")
        self.zkbSpinBox_2.setMinimum(10)
        self.zkbSpinBox_2.setMaximum(100)
        self.zkbSpinBox_2.setSingleStep(10)
        self.zkbSpinBox_2.setStepType(QAbstractSpinBox.DefaultStepType)
        self.zkbSpinBox_2.setDisplayIntegerBase(10)

        self.gridLayout_7.addWidget(self.zkbSpinBox_2, 1, 1, 1, 1, Qt.AlignLeft)

        self.soundLabel_2 = QLabel(self.framePara_2)
        self.soundLabel_2.setObjectName(u"soundLabel_2")
        self.soundLabel_2.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.soundLabel_2.sizePolicy().hasHeightForWidth())
        self.soundLabel_2.setSizePolicy(sizePolicy9)
        self.soundLabel_2.setFont(font6)
        self.soundLabel_2.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_7.addWidget(self.soundLabel_2, 1, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.soundDoubleSpinBox_2 = QDoubleSpinBox(self.framePara_2)
        self.soundDoubleSpinBox_2.setObjectName(u"soundDoubleSpinBox_2")
        self.soundDoubleSpinBox_2.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.soundDoubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.soundDoubleSpinBox_2.setSizePolicy(sizePolicy6)
        self.soundDoubleSpinBox_2.setMinimumSize(QSize(140, 30))
        self.soundDoubleSpinBox_2.setMaximumSize(QSize(140, 50))
        self.soundDoubleSpinBox_2.setFont(font8)
        self.soundDoubleSpinBox_2.setStyleSheet(u"background-color:transparent;\n"
"padding:0px;\n"
"")
        self.soundDoubleSpinBox_2.setMinimum(0.100000000000000)
        self.soundDoubleSpinBox_2.setMaximum(3.000000000000000)
        self.soundDoubleSpinBox_2.setSingleStep(0.100000000000000)
        self.soundDoubleSpinBox_2.setStepType(QAbstractSpinBox.DefaultStepType)
        self.soundDoubleSpinBox_2.setValue(0.100000000000000)

        self.gridLayout_7.addWidget(self.soundDoubleSpinBox_2, 1, 3, 1, 1, Qt.AlignLeft)

        self.timeLabel_2 = QLabel(self.framePara_2)
        self.timeLabel_2.setObjectName(u"timeLabel_2")
        self.timeLabel_2.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.timeLabel_2.sizePolicy().hasHeightForWidth())
        self.timeLabel_2.setSizePolicy(sizePolicy9)
        self.timeLabel_2.setFont(font6)
        self.timeLabel_2.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_7.addWidget(self.timeLabel_2, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.timeSpinBox_2 = QSpinBox(self.framePara_2)
        self.timeSpinBox_2.setObjectName(u"timeSpinBox_2")
        self.timeSpinBox_2.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.timeSpinBox_2.sizePolicy().hasHeightForWidth())
        self.timeSpinBox_2.setSizePolicy(sizePolicy6)
        self.timeSpinBox_2.setMinimumSize(QSize(140, 30))
        self.timeSpinBox_2.setMaximumSize(QSize(140, 50))
        self.timeSpinBox_2.setFont(font8)
        self.timeSpinBox_2.setStyleSheet(u"background-color:transparent;\n"
"padding:0px;\n"
"")
        self.timeSpinBox_2.setMinimum(1)
        self.timeSpinBox_2.setMaximum(20)

        self.gridLayout_7.addWidget(self.timeSpinBox_2, 2, 1, 1, 1, Qt.AlignLeft)

        self.freqLabel_2 = QLabel(self.framePara_2)
        self.freqLabel_2.setObjectName(u"freqLabel_2")
        self.freqLabel_2.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.freqLabel_2.sizePolicy().hasHeightForWidth())
        self.freqLabel_2.setSizePolicy(sizePolicy9)
        self.freqLabel_2.setFont(font6)
        self.freqLabel_2.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_7.addWidget(self.freqLabel_2, 2, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.freqSpinBox_2 = QSpinBox(self.framePara_2)
        self.freqSpinBox_2.setObjectName(u"freqSpinBox_2")
        self.freqSpinBox_2.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.freqSpinBox_2.sizePolicy().hasHeightForWidth())
        self.freqSpinBox_2.setSizePolicy(sizePolicy6)
        self.freqSpinBox_2.setMinimumSize(QSize(140, 30))
        self.freqSpinBox_2.setMaximumSize(QSize(140, 50))
        self.freqSpinBox_2.setFont(font8)
        self.freqSpinBox_2.setStyleSheet(u"background-color:transparent;\n"
"padding:0px;\n"
"")
        self.freqSpinBox_2.setMinimum(1)
        self.freqSpinBox_2.setMaximum(3)
        self.freqSpinBox_2.setSingleStep(2)
        self.freqSpinBox_2.setDisplayIntegerBase(10)

        self.gridLayout_7.addWidget(self.freqSpinBox_2, 2, 3, 1, 1, Qt.AlignLeft)

        self.saveStackedWidget_1 = QStackedWidget(self.framePara_2)
        self.saveStackedWidget_1.setObjectName(u"saveStackedWidget_1")
        self.saveStackedWidget_1.setStyleSheet(u"background-color:transparent;")
        self.savePage_1 = QWidget()
        self.savePage_1.setObjectName(u"savePage_1")
        self.verticalLayout_4 = QVBoxLayout(self.savePage_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.saveSelfPushButton_2 = QPushButton(self.savePage_1)
        self.saveSelfPushButton_2.setObjectName(u"saveSelfPushButton_2")
        sizePolicy2.setHeightForWidth(self.saveSelfPushButton_2.sizePolicy().hasHeightForWidth())
        self.saveSelfPushButton_2.setSizePolicy(sizePolicy2)
        self.saveSelfPushButton_2.setFont(font3)
        self.saveSelfPushButton_2.setStyleSheet(u"background-color: rgb(49, 192, 253);\n"
"border-radius:10px;\n"
"padding:5px;")
        self.saveSelfPushButton_2.setCheckable(True)
        self.saveSelfPushButton_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.saveSelfPushButton_2)

        self.saveStackedWidget_1.addWidget(self.savePage_1)
        self.savePage_2 = QWidget()
        self.savePage_2.setObjectName(u"savePage_2")
        self.saveStackedWidget_1.addWidget(self.savePage_2)

        self.gridLayout_7.addWidget(self.saveStackedWidget_1, 3, 0, 1, 2, Qt.AlignRight|Qt.AlignVCenter)

        self.cancelStackedWidget_1 = QStackedWidget(self.framePara_2)
        self.cancelStackedWidget_1.setObjectName(u"cancelStackedWidget_1")
        self.cancelStackedWidget_1.setStyleSheet(u"background-color:transparent;")
        self.cancelPage_2 = QWidget()
        self.cancelPage_2.setObjectName(u"cancelPage_2")
        self.cancelStackedWidget_1.addWidget(self.cancelPage_2)
        self.cancelPage_1 = QWidget()
        self.cancelPage_1.setObjectName(u"cancelPage_1")
        self.verticalLayout_5 = QVBoxLayout(self.cancelPage_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.cancelSelfPushButton_2 = QPushButton(self.cancelPage_1)
        self.cancelSelfPushButton_2.setObjectName(u"cancelSelfPushButton_2")
        sizePolicy2.setHeightForWidth(self.cancelSelfPushButton_2.sizePolicy().hasHeightForWidth())
        self.cancelSelfPushButton_2.setSizePolicy(sizePolicy2)
        self.cancelSelfPushButton_2.setFont(font3)
        self.cancelSelfPushButton_2.setStyleSheet(u"background-color: rgb(49, 192, 253);\n"
"border-radius:10px;\n"
"padding:5px;")
        self.cancelSelfPushButton_2.setCheckable(True)
        self.cancelSelfPushButton_2.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.cancelSelfPushButton_2)

        self.cancelStackedWidget_1.addWidget(self.cancelPage_1)

        self.gridLayout_7.addWidget(self.cancelStackedWidget_1, 3, 2, 1, 2, Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.setRowStretch(0, 1)
        self.gridLayout_7.setRowStretch(1, 1)
        self.gridLayout_7.setRowStretch(2, 1)
        self.gridLayout_7.setRowStretch(3, 1)
        self.gridLayout_7.setColumnStretch(0, 1)
        self.gridLayout_7.setColumnStretch(1, 3)
        self.gridLayout_7.setColumnStretch(2, 1)
        self.gridLayout_7.setColumnStretch(3, 3)

        self.horizontalLayout_7.addWidget(self.framePara_2)

        self.frameTimer_2 = QFrame(self.contentPage_2)
        self.frameTimer_2.setObjectName(u"frameTimer_2")
        self.frameTimer_2.setEnabled(False)
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.frameTimer_2.sizePolicy().hasHeightForWidth())
        self.frameTimer_2.setSizePolicy(sizePolicy11)
        self.frameTimer_2.setMinimumSize(QSize(170, 0))
        self.frameTimer_2.setMaximumSize(QSize(256, 960))
        self.frameTimer_2.setFont(font)
        self.frameTimer_2.setStyleSheet(u"border-radius:20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(242, 255, 236, 255), stop:1 rgba(205, 242, 255, 198));\n"
"padding:0px;\n"
"                                           ")
        self.frameTimer_2.setFrameShape(QFrame.StyledPanel)
        self.frameTimer_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameTimer_2)
        self.verticalLayout_3.setSpacing(35)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.timerLcdNumber_2 = QLCDNumber(self.frameTimer_2)
        self.timerLcdNumber_2.setObjectName(u"timerLcdNumber_2")
        sizePolicy2.setHeightForWidth(self.timerLcdNumber_2.sizePolicy().hasHeightForWidth())
        self.timerLcdNumber_2.setSizePolicy(sizePolicy2)
        self.timerLcdNumber_2.setMinimumSize(QSize(0, 80))
        self.timerLcdNumber_2.setMaximumSize(QSize(16777215, 250))
        self.timerLcdNumber_2.setStyleSheet(u"border: 5px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color:transparent;\n"
"margin-left:5px;\n"
"margin-right:5px;")
        self.timerLcdNumber_2.setFrameShape(QFrame.Box)
        self.timerLcdNumber_2.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_3.addWidget(self.timerLcdNumber_2)

        self.frame_3 = QFrame(self.frameTimer_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy6.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy6)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, -1, -1, -1)
        self.rayLabel_2 = QLabel(self.frame_3)
        self.rayLabel_2.setObjectName(u"rayLabel_2")
        sizePolicy2.setHeightForWidth(self.rayLabel_2.sizePolicy().hasHeightForWidth())
        self.rayLabel_2.setSizePolicy(sizePolicy2)
        self.rayLabel_2.setMinimumSize(QSize(41, 31))
        self.rayLabel_2.setMaximumSize(QSize(61, 61))
        self.rayLabel_2.setStyleSheet(u"background-color: transparent;")
        self.rayLabel_2.setPixmap(QPixmap(u":/images/camera.png"))
        self.rayLabel_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.rayLabel_2, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.waveLabel_2 = QLabel(self.frame_3)
        self.waveLabel_2.setObjectName(u"waveLabel_2")
        sizePolicy2.setHeightForWidth(self.waveLabel_2.sizePolicy().hasHeightForWidth())
        self.waveLabel_2.setSizePolicy(sizePolicy2)
        self.waveLabel_2.setMinimumSize(QSize(0, 60))
        self.waveLabel_2.setMaximumSize(QSize(150, 100))
        self.waveLabel_2.setStyleSheet(u"background-color: transparent;")
        self.waveLabel_2.setPixmap(QPixmap(u":/images/wave.gif"))
        self.waveLabel_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.waveLabel_2, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frameTimer_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy7.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy7)
        self.frame_4.setMaximumSize(QSize(256, 120))
        self.frame_4.setStyleSheet(u"background-color:transparent;")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, -1, 5, -1)
        self.btnStart_2 = QPushButton(self.frame_4)
        self.spsButtonGroup_2 = QButtonGroup(MainWindow)
        self.spsButtonGroup_2.setObjectName(u"spsButtonGroup_2")
        self.spsButtonGroup_2.addButton(self.btnStart_2)
        self.btnStart_2.setObjectName(u"btnStart_2")
        sizePolicy2.setHeightForWidth(self.btnStart_2.sizePolicy().hasHeightForWidth())
        self.btnStart_2.setSizePolicy(sizePolicy2)
        self.btnStart_2.setMinimumSize(QSize(50, 50))
        self.btnStart_2.setMaximumSize(QSize(50, 50))
        self.btnStart_2.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border-image: url(:/images/start.png);\n"
"}\n"
"QPushButton:checked{\n"
"border-image: url(:/images/starton.png);\n"
"}")
        self.btnStart_2.setCheckable(True)
        self.btnStart_2.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.btnStart_2, 0, Qt.AlignHCenter)

        self.btnPause_2 = QPushButton(self.frame_4)
        self.spsButtonGroup_2.addButton(self.btnPause_2)
        self.btnPause_2.setObjectName(u"btnPause_2")
        sizePolicy2.setHeightForWidth(self.btnPause_2.sizePolicy().hasHeightForWidth())
        self.btnPause_2.setSizePolicy(sizePolicy2)
        self.btnPause_2.setMinimumSize(QSize(50, 50))
        self.btnPause_2.setMaximumSize(QSize(50, 50))
        self.btnPause_2.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border-image: url(:/images/pause.png);\n"
"}\n"
"QPushButton:checked{\n"
"border-image: url(:/images/pauseon.png);\n"
"}")
        self.btnPause_2.setCheckable(True)
        self.btnPause_2.setAutoRepeat(True)
        self.btnPause_2.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.btnPause_2, 0, Qt.AlignHCenter)

        self.btnStop_2 = QPushButton(self.frame_4)
        self.spsButtonGroup_2.addButton(self.btnStop_2)
        self.btnStop_2.setObjectName(u"btnStop_2")
        sizePolicy2.setHeightForWidth(self.btnStop_2.sizePolicy().hasHeightForWidth())
        self.btnStop_2.setSizePolicy(sizePolicy2)
        self.btnStop_2.setMinimumSize(QSize(50, 50))
        self.btnStop_2.setMaximumSize(QSize(50, 50))
        self.btnStop_2.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border-image: url(:/images/stop.png);\n"
"}\n"
"QPushButton:checked{\n"
"border-image: url(:/images/stopon.png);\n"
"}")
        self.btnStop_2.setCheckable(True)
        self.btnStop_2.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.btnStop_2, 0, Qt.AlignHCenter)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout_3.addWidget(self.frame_4)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_7.addWidget(self.frameTimer_2)

        self.horizontalLayout_7.setStretch(0, 4)
        self.horizontalLayout_7.setStretch(1, 1)
        self.contentStackedWidget_1.addWidget(self.contentPage_2)
        self.contentPage_3 = QWidget()
        self.contentPage_3.setObjectName(u"contentPage_3")
        self.horizontalLayout_10 = QHBoxLayout(self.contentPage_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.framePara_3 = QFrame(self.contentPage_3)
        self.framePara_3.setObjectName(u"framePara_3")
        sizePolicy2.setHeightForWidth(self.framePara_3.sizePolicy().hasHeightForWidth())
        self.framePara_3.setSizePolicy(sizePolicy2)
        self.framePara_3.setMinimumSize(QSize(400, 0))
        self.framePara_3.setMaximumSize(QSize(1024, 16777215))
        self.framePara_3.setFont(font)
        self.framePara_3.setAutoFillBackground(False)
        self.framePara_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(242, 255, 236, 255), stop:1 rgba(205, 242, 255, 198));\n"
"border-radius:20px;\n"
"padding:20px;")
        self.framePara_3.setFrameShape(QFrame.StyledPanel)
        self.framePara_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.framePara_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, -1, 9, -1)
        self.planLabel_3 = QLabel(self.framePara_3)
        self.planLabel_3.setObjectName(u"planLabel_3")
        self.planLabel_3.setFont(font6)
        self.planLabel_3.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_8.addWidget(self.planLabel_3, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.planComboBox_3 = QComboBox(self.framePara_3)
        self.planComboBox_3.addItem("")
        self.planComboBox_3.setObjectName(u"planComboBox_3")
        sizePolicy4.setHeightForWidth(self.planComboBox_3.sizePolicy().hasHeightForWidth())
        self.planComboBox_3.setSizePolicy(sizePolicy4)
        self.planComboBox_3.setMinimumSize(QSize(180, 30))
        self.planComboBox_3.setMaximumSize(QSize(180, 16777215))
        self.planComboBox_3.setFont(font6)

        self.gridLayout_8.addWidget(self.planComboBox_3, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.zkbLabel_3 = QLabel(self.framePara_3)
        self.zkbLabel_3.setObjectName(u"zkbLabel_3")
        self.zkbLabel_3.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.zkbLabel_3.sizePolicy().hasHeightForWidth())
        self.zkbLabel_3.setSizePolicy(sizePolicy9)
        self.zkbLabel_3.setFont(font6)
        self.zkbLabel_3.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_8.addWidget(self.zkbLabel_3, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.zkbSpinBox_3 = QSpinBox(self.framePara_3)
        self.zkbSpinBox_3.setObjectName(u"zkbSpinBox_3")
        self.zkbSpinBox_3.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.zkbSpinBox_3.sizePolicy().hasHeightForWidth())
        self.zkbSpinBox_3.setSizePolicy(sizePolicy6)
        self.zkbSpinBox_3.setMinimumSize(QSize(140, 30))
        self.zkbSpinBox_3.setMaximumSize(QSize(140, 50))
        self.zkbSpinBox_3.setSizeIncrement(QSize(0, 0))
        self.zkbSpinBox_3.setBaseSize(QSize(0, 0))
        self.zkbSpinBox_3.setFont(font8)
        self.zkbSpinBox_3.setStyleSheet(u"background-color:transparent;\n"
"padding:0px;\n"
"")
        self.zkbSpinBox_3.setMinimum(10)
        self.zkbSpinBox_3.setMaximum(100)
        self.zkbSpinBox_3.setSingleStep(10)
        self.zkbSpinBox_3.setStepType(QAbstractSpinBox.DefaultStepType)
        self.zkbSpinBox_3.setDisplayIntegerBase(10)

        self.gridLayout_8.addWidget(self.zkbSpinBox_3, 1, 1, 1, 1, Qt.AlignLeft)

        self.soundLabel_3 = QLabel(self.framePara_3)
        self.soundLabel_3.setObjectName(u"soundLabel_3")
        self.soundLabel_3.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.soundLabel_3.sizePolicy().hasHeightForWidth())
        self.soundLabel_3.setSizePolicy(sizePolicy9)
        self.soundLabel_3.setFont(font6)
        self.soundLabel_3.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_8.addWidget(self.soundLabel_3, 1, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.soundDoubleSpinBox_3 = QDoubleSpinBox(self.framePara_3)
        self.soundDoubleSpinBox_3.setObjectName(u"soundDoubleSpinBox_3")
        self.soundDoubleSpinBox_3.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.soundDoubleSpinBox_3.sizePolicy().hasHeightForWidth())
        self.soundDoubleSpinBox_3.setSizePolicy(sizePolicy6)
        self.soundDoubleSpinBox_3.setMinimumSize(QSize(140, 30))
        self.soundDoubleSpinBox_3.setMaximumSize(QSize(140, 50))
        self.soundDoubleSpinBox_3.setFont(font8)
        self.soundDoubleSpinBox_3.setStyleSheet(u"background-color:transparent;\n"
"padding:0px;\n"
"")
        self.soundDoubleSpinBox_3.setMinimum(0.100000000000000)
        self.soundDoubleSpinBox_3.setMaximum(3.000000000000000)
        self.soundDoubleSpinBox_3.setSingleStep(0.100000000000000)
        self.soundDoubleSpinBox_3.setValue(0.100000000000000)

        self.gridLayout_8.addWidget(self.soundDoubleSpinBox_3, 1, 3, 1, 1, Qt.AlignLeft)

        self.timeLabel_3 = QLabel(self.framePara_3)
        self.timeLabel_3.setObjectName(u"timeLabel_3")
        self.timeLabel_3.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.timeLabel_3.sizePolicy().hasHeightForWidth())
        self.timeLabel_3.setSizePolicy(sizePolicy9)
        self.timeLabel_3.setFont(font6)
        self.timeLabel_3.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_8.addWidget(self.timeLabel_3, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.timeSpinBox_3 = QSpinBox(self.framePara_3)
        self.timeSpinBox_3.setObjectName(u"timeSpinBox_3")
        self.timeSpinBox_3.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.timeSpinBox_3.sizePolicy().hasHeightForWidth())
        self.timeSpinBox_3.setSizePolicy(sizePolicy6)
        self.timeSpinBox_3.setMinimumSize(QSize(140, 30))
        self.timeSpinBox_3.setMaximumSize(QSize(140, 50))
        self.timeSpinBox_3.setFont(font8)
        self.timeSpinBox_3.setStyleSheet(u"background-color:transparent;\n"
"padding:0px;\n"
"")
        self.timeSpinBox_3.setMinimum(1)
        self.timeSpinBox_3.setMaximum(20)

        self.gridLayout_8.addWidget(self.timeSpinBox_3, 2, 1, 1, 1, Qt.AlignLeft)

        self.freqLabel_3 = QLabel(self.framePara_3)
        self.freqLabel_3.setObjectName(u"freqLabel_3")
        self.freqLabel_3.setEnabled(False)
        sizePolicy9.setHeightForWidth(self.freqLabel_3.sizePolicy().hasHeightForWidth())
        self.freqLabel_3.setSizePolicy(sizePolicy9)
        self.freqLabel_3.setFont(font6)
        self.freqLabel_3.setStyleSheet(u"background-color:transparent;")

        self.gridLayout_8.addWidget(self.freqLabel_3, 2, 2, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.freqSpinBox_3 = QSpinBox(self.framePara_3)
        self.freqSpinBox_3.setObjectName(u"freqSpinBox_3")
        self.freqSpinBox_3.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.freqSpinBox_3.sizePolicy().hasHeightForWidth())
        self.freqSpinBox_3.setSizePolicy(sizePolicy6)
        self.freqSpinBox_3.setMinimumSize(QSize(140, 30))
        self.freqSpinBox_3.setMaximumSize(QSize(140, 50))
        self.freqSpinBox_3.setFont(font8)
        self.freqSpinBox_3.setStyleSheet(u"background-color:transparent;\n"
"padding:0px;\n"
"")
        self.freqSpinBox_3.setMinimum(1)
        self.freqSpinBox_3.setMaximum(3)
        self.freqSpinBox_3.setSingleStep(2)
        self.freqSpinBox_3.setDisplayIntegerBase(10)

        self.gridLayout_8.addWidget(self.freqSpinBox_3, 2, 3, 1, 1, Qt.AlignLeft)

        self.saveStackedWidget_2 = QStackedWidget(self.framePara_3)
        self.saveStackedWidget_2.setObjectName(u"saveStackedWidget_2")
        self.saveStackedWidget_2.setStyleSheet(u"background-color:transparent;")
        self.savePage_3 = QWidget()
        self.savePage_3.setObjectName(u"savePage_3")
        self.verticalLayout_7 = QVBoxLayout(self.savePage_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.saveSelfPushButton_3 = QPushButton(self.savePage_3)
        self.saveSelfPushButton_3.setObjectName(u"saveSelfPushButton_3")
        sizePolicy2.setHeightForWidth(self.saveSelfPushButton_3.sizePolicy().hasHeightForWidth())
        self.saveSelfPushButton_3.setSizePolicy(sizePolicy2)
        self.saveSelfPushButton_3.setFont(font3)
        self.saveSelfPushButton_3.setStyleSheet(u"background-color: rgb(49, 192, 253);\n"
"border-radius:10px;\n"
"padding:5px;")
        self.saveSelfPushButton_3.setCheckable(True)
        self.saveSelfPushButton_3.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.saveSelfPushButton_3)

        self.saveStackedWidget_2.addWidget(self.savePage_3)
        self.savePage_4 = QWidget()
        self.savePage_4.setObjectName(u"savePage_4")
        self.saveStackedWidget_2.addWidget(self.savePage_4)

        self.gridLayout_8.addWidget(self.saveStackedWidget_2, 3, 0, 1, 2, Qt.AlignRight|Qt.AlignVCenter)

        self.cancelStackedWidget_2 = QStackedWidget(self.framePara_3)
        self.cancelStackedWidget_2.setObjectName(u"cancelStackedWidget_2")
        self.cancelStackedWidget_2.setStyleSheet(u"background-color:transparent;")
        self.cancelPage_3 = QWidget()
        self.cancelPage_3.setObjectName(u"cancelPage_3")
        self.verticalLayout_8 = QVBoxLayout(self.cancelPage_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cancelSelfPushButton_3 = QPushButton(self.cancelPage_3)
        self.cancelSelfPushButton_3.setObjectName(u"cancelSelfPushButton_3")
        sizePolicy2.setHeightForWidth(self.cancelSelfPushButton_3.sizePolicy().hasHeightForWidth())
        self.cancelSelfPushButton_3.setSizePolicy(sizePolicy2)
        self.cancelSelfPushButton_3.setFont(font3)
        self.cancelSelfPushButton_3.setStyleSheet(u"background-color: rgb(49, 192, 253);\n"
"border-radius:10px;\n"
"padding:5px;")
        self.cancelSelfPushButton_3.setCheckable(True)
        self.cancelSelfPushButton_3.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.cancelSelfPushButton_3)

        self.cancelStackedWidget_2.addWidget(self.cancelPage_3)
        self.cancelPage_4 = QWidget()
        self.cancelPage_4.setObjectName(u"cancelPage_4")
        self.cancelStackedWidget_2.addWidget(self.cancelPage_4)

        self.gridLayout_8.addWidget(self.cancelStackedWidget_2, 3, 2, 1, 2, Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_8.setRowStretch(0, 1)
        self.gridLayout_8.setRowStretch(1, 1)
        self.gridLayout_8.setRowStretch(2, 1)
        self.gridLayout_8.setRowStretch(3, 1)
        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setColumnStretch(1, 3)
        self.gridLayout_8.setColumnStretch(2, 1)
        self.gridLayout_8.setColumnStretch(3, 3)

        self.horizontalLayout_10.addWidget(self.framePara_3)

        self.frameTimer_3 = QFrame(self.contentPage_3)
        self.frameTimer_3.setObjectName(u"frameTimer_3")
        self.frameTimer_3.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.frameTimer_3.sizePolicy().hasHeightForWidth())
        self.frameTimer_3.setSizePolicy(sizePolicy5)
        self.frameTimer_3.setMinimumSize(QSize(170, 0))
        self.frameTimer_3.setMaximumSize(QSize(256, 960))
        self.frameTimer_3.setFont(font)
        self.frameTimer_3.setStyleSheet(u"border-radius:20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(242, 255, 236, 255), stop:1 rgba(205, 242, 255, 198));\n"
"padding:0px;\n"
"                                           ")
        self.frameTimer_3.setFrameShape(QFrame.StyledPanel)
        self.frameTimer_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frameTimer_3)
        self.verticalLayout_6.setSpacing(35)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.timerLcdNumber_3 = QLCDNumber(self.frameTimer_3)
        self.timerLcdNumber_3.setObjectName(u"timerLcdNumber_3")
        sizePolicy2.setHeightForWidth(self.timerLcdNumber_3.sizePolicy().hasHeightForWidth())
        self.timerLcdNumber_3.setSizePolicy(sizePolicy2)
        self.timerLcdNumber_3.setMinimumSize(QSize(0, 80))
        self.timerLcdNumber_3.setMaximumSize(QSize(16777215, 250))
        self.timerLcdNumber_3.setStyleSheet(u"border: 5px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color:transparent;\n"
"margin-left:5px;\n"
"margin-right:5px;")
        self.timerLcdNumber_3.setFrameShape(QFrame.Box)
        self.timerLcdNumber_3.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_6.addWidget(self.timerLcdNumber_3)

        self.frame_5 = QFrame(self.frameTimer_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy6.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy6)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, -1, -1, -1)
        self.rayLabel_3 = QLabel(self.frame_5)
        self.rayLabel_3.setObjectName(u"rayLabel_3")
        sizePolicy2.setHeightForWidth(self.rayLabel_3.sizePolicy().hasHeightForWidth())
        self.rayLabel_3.setSizePolicy(sizePolicy2)
        self.rayLabel_3.setMinimumSize(QSize(41, 31))
        self.rayLabel_3.setMaximumSize(QSize(61, 61))
        self.rayLabel_3.setStyleSheet(u"background-color: transparent;")
        self.rayLabel_3.setPixmap(QPixmap(u":/images/camera.png"))
        self.rayLabel_3.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.rayLabel_3, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.waveLabel_3 = QLabel(self.frame_5)
        self.waveLabel_3.setObjectName(u"waveLabel_3")
        sizePolicy2.setHeightForWidth(self.waveLabel_3.sizePolicy().hasHeightForWidth())
        self.waveLabel_3.setSizePolicy(sizePolicy2)
        self.waveLabel_3.setMinimumSize(QSize(0, 60))
        self.waveLabel_3.setMaximumSize(QSize(150, 100))
        self.waveLabel_3.setStyleSheet(u"background-color: transparent;")
        self.waveLabel_3.setPixmap(QPixmap(u":/images/wave.gif"))
        self.waveLabel_3.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.waveLabel_3, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frameTimer_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy7.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy7)
        self.frame_6.setMaximumSize(QSize(256, 120))
        self.frame_6.setStyleSheet(u"background-color:transparent;")
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, -1, 5, -1)
        self.btnStart_3 = QPushButton(self.frame_6)
        self.spsButtonGroup_3 = QButtonGroup(MainWindow)
        self.spsButtonGroup_3.setObjectName(u"spsButtonGroup_3")
        self.spsButtonGroup_3.addButton(self.btnStart_3)
        self.btnStart_3.setObjectName(u"btnStart_3")
        sizePolicy2.setHeightForWidth(self.btnStart_3.sizePolicy().hasHeightForWidth())
        self.btnStart_3.setSizePolicy(sizePolicy2)
        self.btnStart_3.setMinimumSize(QSize(50, 50))
        self.btnStart_3.setMaximumSize(QSize(50, 50))
        self.btnStart_3.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border-image: url(:/images/start.png);\n"
"}\n"
"QPushButton:checked{\n"
"border-image: url(:/images/starton.png);\n"
"}")
        self.btnStart_3.setCheckable(True)
        self.btnStart_3.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.btnStart_3, 0, Qt.AlignHCenter)

        self.btnPause_3 = QPushButton(self.frame_6)
        self.spsButtonGroup_3.addButton(self.btnPause_3)
        self.btnPause_3.setObjectName(u"btnPause_3")
        sizePolicy2.setHeightForWidth(self.btnPause_3.sizePolicy().hasHeightForWidth())
        self.btnPause_3.setSizePolicy(sizePolicy2)
        self.btnPause_3.setMinimumSize(QSize(50, 50))
        self.btnPause_3.setMaximumSize(QSize(50, 50))
        self.btnPause_3.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border-image: url(:/images/pause.png);\n"
"}\n"
"QPushButton:checked{\n"
"border-image: url(:/images/pauseon.png);\n"
"}")
        self.btnPause_3.setCheckable(True)
        self.btnPause_3.setAutoRepeat(True)
        self.btnPause_3.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.btnPause_3, 0, Qt.AlignHCenter)

        self.btnStop_3 = QPushButton(self.frame_6)
        self.spsButtonGroup_3.addButton(self.btnStop_3)
        self.btnStop_3.setObjectName(u"btnStop_3")
        sizePolicy2.setHeightForWidth(self.btnStop_3.sizePolicy().hasHeightForWidth())
        self.btnStop_3.setSizePolicy(sizePolicy2)
        self.btnStop_3.setMinimumSize(QSize(50, 50))
        self.btnStop_3.setMaximumSize(QSize(50, 50))
        self.btnStop_3.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border-image: url(:/images/stop.png);\n"
"}\n"
"QPushButton:checked{\n"
"border-image: url(:/images/stopon.png);\n"
"}")
        self.btnStop_3.setCheckable(True)
        self.btnStop_3.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.btnStop_3, 0, Qt.AlignHCenter)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 1)

        self.verticalLayout_6.addWidget(self.frame_6)

        self.verticalLayout_6.setStretch(0, 2)
        self.verticalLayout_6.setStretch(1, 2)
        self.verticalLayout_6.setStretch(2, 1)

        self.horizontalLayout_10.addWidget(self.frameTimer_3)

        self.horizontalLayout_10.setStretch(0, 4)
        self.horizontalLayout_10.setStretch(1, 1)
        self.contentStackedWidget_1.addWidget(self.contentPage_3)

        self.gridLayout_6.addWidget(self.contentStackedWidget_1, 1, 0, 1, 1)

        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.contentStackedWidget_1.setCurrentIndex(0)
        self.adjustStackedWidget_1.setCurrentIndex(0)
        self.planComboBox_1.setCurrentIndex(-1)
        self.saveCancelStackedWidget_1.setCurrentIndex(1)
        self.planComboBox_2.setCurrentIndex(-1)
        self.saveStackedWidget_1.setCurrentIndex(0)
        self.planComboBox_3.setCurrentIndex(-1)
        self.saveStackedWidget_2.setCurrentIndex(1)
        self.cancelStackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u58f0\u6cbb\u7597\u673a\u5668\u4eba", None))
        self.stateStr.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u4f5c\u72b6\u6001\uff1a", None))
        self.statelight_1.setText("")
        self.state_camera_1.setText(QCoreApplication.translate("MainWindow", u"\u63a2\u59341", None))
        self.statelight_2.setText("")
        self.state_camera_2.setText(QCoreApplication.translate("MainWindow", u"\u63a2\u59342", None))
        self.statelight_3.setText("")
        self.state_camera_3.setText(QCoreApplication.translate("MainWindow", u"\u63a2\u59343", None))
        self.label.setText("")
        self.cam1.setText(QCoreApplication.translate("MainWindow", u"\u63a2\u59341", None))
        self.cam2.setText(QCoreApplication.translate("MainWindow", u"\u63a2\u59342", None))
        self.cam3.setText(QCoreApplication.translate("MainWindow", u"\u63a2\u59343", None))

        __sortingEnabled = self.bodyTreeWidget.isSortingEnabled()
        self.bodyTreeWidget.setSortingEnabled(False)
        ___qtreewidgetitem = self.bodyTreeWidget.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u80a9\u9888\u90e8", None));
        ___qtreewidgetitem1 = ___qtreewidgetitem.child(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u75db\u70b9\u6cbb\u7597", None));
        ___qtreewidgetitem2 = self.bodyTreeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u80f8\u80cc\u90e8", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u5e38\u89c4\u6cbb\u7597", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u75db\u70b9\u6cbb\u7597", None));
        ___qtreewidgetitem5 = self.bodyTreeWidget.topLevelItem(2)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u8170\u90e8", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u5e38\u89c4\u6cbb\u7597", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem5.child(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u75db\u70b9\u6cbb\u7597", None));
        ___qtreewidgetitem8 = self.bodyTreeWidget.topLevelItem(3)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u8170\u9ab6\u90e8", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem8.child(0)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u5e38\u89c4\u6cbb\u7597", None));
        ___qtreewidgetitem10 = self.bodyTreeWidget.topLevelItem(4)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u8179\u90e8", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u987a\u65f6\u9488", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem10.child(1)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u9006\u65f6\u9488", None));
        ___qtreewidgetitem13 = self.bodyTreeWidget.topLevelItem(5)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"\u81c0\u90e8", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem13.child(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"\u75db\u70b9\u6cbb\u7597", None));
        ___qtreewidgetitem15 = self.bodyTreeWidget.topLevelItem(6)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"\u5927\u817f\u5916\u4fa7", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem15.child(0)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"\u5e38\u89c4\u6cbb\u7597", None));
        ___qtreewidgetitem17 = self.bodyTreeWidget.topLevelItem(7)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"\u5c0f\u817f", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem17.child(0)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"\u5e38\u89c4\u6cbb\u7597", None));
        self.bodyTreeWidget.setSortingEnabled(__sortingEnabled)

        self.rayLabel_1.setText("")
        self.waveLabel_1.setText("")
        self.btnStart_1.setText("")
        self.btnPause_1.setText("")
        self.btnStop_1.setText("")
        self.savePointPushButton_1.setText(QCoreApplication.translate("MainWindow", u"  \u5b58\u70b91  ", None))
        self.pullPushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5165\u62d6\u62fd", None))
        self.pointLabel.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a\u70b9\u4f4d: ", None))
        self.adjustLabel.setText(QCoreApplication.translate("MainWindow", u"\u5fae\u8c03: ", None))
        self.front.setText(QCoreApplication.translate("MainWindow", u"\u524d", None))
        self.left.setText(QCoreApplication.translate("MainWindow", u"\u5de6", None))
        self.back.setText(QCoreApplication.translate("MainWindow", u"\u540e", None))
        self.right.setText(QCoreApplication.translate("MainWindow", u"\u53f3", None))
        self.switch_2.setText("")
        self.switch_1.setText("")
        self.rightrot.setText(QCoreApplication.translate("MainWindow", u"\u53f3\u65cb", None))
        self.up.setText(QCoreApplication.translate("MainWindow", u"\u4e0a", None))
        self.down.setText(QCoreApplication.translate("MainWindow", u"\u4e0b", None))
        self.leftrot.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u65cb", None))
        self.planLabel_1.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u6848: ", None))
        self.zkbLabel_1.setText(QCoreApplication.translate("MainWindow", u"\u5360\u7a7a\u6bd4: ", None))
        self.zkbSpinBox_1.setSuffix(QCoreApplication.translate("MainWindow", u" %", None))
        self.freqLabel_1.setText(QCoreApplication.translate("MainWindow", u"\u9891 \u7387: ", None))
        self.freqSpinBox_1.setSuffix(QCoreApplication.translate("MainWindow", u" MHz", None))
        self.speedLabel_1.setText(QCoreApplication.translate("MainWindow", u"\u901f \u5ea6: ", None))
        self.speedSpinBox_1.setSuffix(QCoreApplication.translate("MainWindow", u" cm/s", None))
        self.soundLabel_1.setText(QCoreApplication.translate("MainWindow", u"\u58f0 \u5f3a: ", None))
        self.soundDoubleSpinBox_1.setPrefix("")
        self.soundDoubleSpinBox_1.setSuffix(QCoreApplication.translate("MainWindow", u" W/cm2", None))
        self.timeLabel_1.setText(QCoreApplication.translate("MainWindow", u"\u65f6 \u95f4: ", None))
        self.timeSpinBox_1.setSuffix(QCoreApplication.translate("MainWindow", u" minutes", None))
        self.strengthLabel.setText(QCoreApplication.translate("MainWindow", u"\u529b \u5ea6: ", None))
        self.strengthSpinBox_1.setSuffix(QCoreApplication.translate("MainWindow", u" N", None))
        self.planComboBox_1.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u81ea\u5b9a\u4e49...", None))

        self.planComboBox_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5148\u9009\u62e9\u65b9\u6848", None))
        self.saveSelfPushButton_1.setText(QCoreApplication.translate("MainWindow", u"  \u4fdd\u5b58  ", None))
        self.cancelSelfPushButton_1.setText(QCoreApplication.translate("MainWindow", u"  \u53d6\u6d88  ", None))
        self.planLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u6848: ", None))
        self.planComboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u81ea\u5b9a\u4e49+++", None))

        self.planComboBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5148\u9009\u62e9\u65b9\u6848", None))
        self.zkbLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u5360\u7a7a\u6bd4: ", None))
        self.zkbSpinBox_2.setSuffix(QCoreApplication.translate("MainWindow", u" %", None))
        self.soundLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u58f0\u5f3a: ", None))
        self.soundDoubleSpinBox_2.setSuffix(QCoreApplication.translate("MainWindow", u" W/cm2", None))
        self.timeLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4: ", None))
        self.timeSpinBox_2.setSuffix(QCoreApplication.translate("MainWindow", u" minutes", None))
        self.freqLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u9891\u7387: ", None))
        self.freqSpinBox_2.setSuffix(QCoreApplication.translate("MainWindow", u" MHz", None))
        self.saveSelfPushButton_2.setText(QCoreApplication.translate("MainWindow", u"  \u4fdd\u5b58  ", None))
        self.cancelSelfPushButton_2.setText(QCoreApplication.translate("MainWindow", u"  \u53d6\u6d88  ", None))
        self.rayLabel_2.setText("")
        self.waveLabel_2.setText("")
        self.btnStart_2.setText("")
        self.btnPause_2.setText("")
        self.btnStop_2.setText("")
        self.planLabel_3.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u6848: ", None))
        self.planComboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49+++", None))

        self.planComboBox_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5148\u9009\u62e9\u65b9\u6848", None))
        self.zkbLabel_3.setText(QCoreApplication.translate("MainWindow", u"\u5360\u7a7a\u6bd4: ", None))
        self.zkbSpinBox_3.setSuffix(QCoreApplication.translate("MainWindow", u" %", None))
        self.soundLabel_3.setText(QCoreApplication.translate("MainWindow", u"\u58f0\u5f3a: ", None))
        self.soundDoubleSpinBox_3.setSuffix(QCoreApplication.translate("MainWindow", u" W/cm2", None))
        self.timeLabel_3.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4: ", None))
        self.timeSpinBox_3.setSuffix(QCoreApplication.translate("MainWindow", u" minutes", None))
        self.freqLabel_3.setText(QCoreApplication.translate("MainWindow", u"\u9891\u7387: ", None))
        self.freqSpinBox_3.setSuffix(QCoreApplication.translate("MainWindow", u" MHz", None))
        self.saveSelfPushButton_3.setText(QCoreApplication.translate("MainWindow", u"  \u4fdd\u5b58  ", None))
        self.cancelSelfPushButton_3.setText(QCoreApplication.translate("MainWindow", u"  \u53d6\u6d88  ", None))
        self.rayLabel_3.setText("")
        self.waveLabel_3.setText("")
        self.btnStart_3.setText("")
        self.btnPause_3.setText("")
        self.btnStop_3.setText("")
    # retranslateUi

