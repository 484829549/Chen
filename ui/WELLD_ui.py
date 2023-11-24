# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WELLD.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)
import res.pngConfig_rc

class Ui_WelldWidget(object):
    def setupUi(self, WelldWidget):
        if not WelldWidget.objectName():
            WelldWidget.setObjectName(u"WelldWidget")
        WelldWidget.resize(800, 600)
        WelldWidget.setMinimumSize(QSize(800, 600))
        WelldWidget.setMaximumSize(QSize(16777215, 16777215))
        WelldWidget.setStyleSheet(u"background-color: rgb(197, 249, 255);")
        self.horizontalLayout_3 = QHBoxLayout(WelldWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frameMenuList = QFrame(WelldWidget)
        self.frameMenuList.setObjectName(u"frameMenuList")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameMenuList.sizePolicy().hasHeightForWidth())
        self.frameMenuList.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(14)
        self.frameMenuList.setFont(font)
        self.frameMenuList.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(85, 255, 255);")
        self.frameMenuList.setFrameShape(QFrame.Box)
        self.frameMenuList.setFrameShadow(QFrame.Sunken)
        self.frameMenuList.setLineWidth(1)
        self.verticalLayout_6 = QVBoxLayout(self.frameMenuList)
        self.verticalLayout_6.setSpacing(9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.menuListWidget = QListWidget(self.frameMenuList)
        QListWidgetItem(self.menuListWidget)
        QListWidgetItem(self.menuListWidget)
        QListWidgetItem(self.menuListWidget)
        QListWidgetItem(self.menuListWidget)
        QListWidgetItem(self.menuListWidget)
        QListWidgetItem(self.menuListWidget)
        self.menuListWidget.setObjectName(u"menuListWidget")
        self.menuListWidget.setMinimumSize(QSize(160, 0))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.menuListWidget.setFont(font1)
        self.menuListWidget.setStyleSheet(u"QListWidget::item{\n"
"padding: 10px;\n"
"}\n"
"QListWidget::item:selected{\n"
"font: bold 15px;\n"
"\n"
"}\n"
"QListWidget::item:hover{\n"
"background-color: #4d80e6;\n"
"color:white;\n"
"\n"
"}")
        self.menuListWidget.setFlow(QListView.TopToBottom)
        self.menuListWidget.setSpacing(8)

        self.verticalLayout_6.addWidget(self.menuListWidget)


        self.horizontalLayout_3.addWidget(self.frameMenuList)

        self.welldStackedWidget = QStackedWidget(WelldWidget)
        self.welldStackedWidget.setObjectName(u"welldStackedWidget")
        self.welldStackedWidget.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(222, 255, 197);")
        self.pageOverView = QWidget()
        self.pageOverView.setObjectName(u"pageOverView")
        self.horizontalLayout = QHBoxLayout(self.pageOverView)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameLeft = QFrame(self.pageOverView)
        self.frameLeft.setObjectName(u"frameLeft")
        self.frameLeft.setMinimumSize(QSize(160, 0))
        self.frameLeft.setStyleSheet(u"background-color: rgb(178, 228, 255);")
        self.frameLeft.setFrameShape(QFrame.StyledPanel)
        self.frameLeft.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameLeft)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_6 = QFrame(self.frameLeft)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(217, 218, 255);\n"
"border-radius:15px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.jjTextBrowser = QTextBrowser(self.frame_6)
        self.jjTextBrowser.setObjectName(u"jjTextBrowser")
        font2 = QFont()
        font2.setFamilies([u"\u5b8b\u4f53"])
        font2.setPointSize(14)
        self.jjTextBrowser.setFont(font2)

        self.verticalLayout_9.addWidget(self.jjTextBrowser, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frameLeft)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(217, 218, 255);\n"
"border-radius:15px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textBrowser_2 = QTextBrowser(self.frame_7)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout_10.addWidget(self.textBrowser_2, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frameLeft)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(217, 218, 255);\n"
"border-radius:15px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.textBrowser_4 = QTextBrowser(self.frame_8)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.verticalLayout_11.addWidget(self.textBrowser_4)


        self.verticalLayout.addWidget(self.frame_8, 0, Qt.AlignVCenter)

        self.frame_9 = QFrame(self.frameLeft)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(217, 218, 255);\n"
"border-radius:15px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.textBrowser_6 = QTextBrowser(self.frame_9)
        self.textBrowser_6.setObjectName(u"textBrowser_6")

        self.verticalLayout_12.addWidget(self.textBrowser_6, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frameLeft)

        self.frameMid = QFrame(self.pageOverView)
        self.frameMid.setObjectName(u"frameMid")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameMid.sizePolicy().hasHeightForWidth())
        self.frameMid.setSizePolicy(sizePolicy1)
        self.frameMid.setMaximumSize(QSize(16777215, 960))
        self.frameMid.setFrameShape(QFrame.StyledPanel)
        self.frameMid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameMid)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.bodyLabel = QLabel(self.frameMid)
        self.bodyLabel.setObjectName(u"bodyLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bodyLabel.sizePolicy().hasHeightForWidth())
        self.bodyLabel.setSizePolicy(sizePolicy2)
        self.bodyLabel.setMinimumSize(QSize(200, 200))
        self.bodyLabel.setMaximumSize(QSize(16777215, 960))
        self.bodyLabel.setPixmap(QPixmap(u":/images/body.jpg"))
        self.bodyLabel.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.bodyLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frameMid)

        self.frameRight = QFrame(self.pageOverView)
        self.frameRight.setObjectName(u"frameRight")
        self.frameRight.setMinimumSize(QSize(160, 0))
        self.frameRight.setStyleSheet(u"background-color: rgb(178, 228, 255);")
        self.frameRight.setFrameShape(QFrame.StyledPanel)
        self.frameRight.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameRight)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_13 = QFrame(self.frameRight)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(217, 218, 255);\n"
"border-radius:15px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.textBrowser_5 = QTextBrowser(self.frame_13)
        self.textBrowser_5.setObjectName(u"textBrowser_5")

        self.verticalLayout_13.addWidget(self.textBrowser_5, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.frame_11 = QFrame(self.frameRight)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(217, 218, 255);\n"
"border-radius:15px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.textBrowser_3 = QTextBrowser(self.frame_11)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.verticalLayout_14.addWidget(self.textBrowser_3, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frameRight)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgb(217, 218, 255);\n"
"border-radius:15px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.textBrowser_8 = QTextBrowser(self.frame_12)
        self.textBrowser_8.setObjectName(u"textBrowser_8")

        self.verticalLayout_15.addWidget(self.textBrowser_8, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_12)

        self.frame_10 = QFrame(self.frameRight)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(217, 218, 255);\n"
"border-radius:15px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.textBrowser_7 = QTextBrowser(self.frame_10)
        self.textBrowser_7.setObjectName(u"textBrowser_7")

        self.verticalLayout_16.addWidget(self.textBrowser_7, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_10)


        self.horizontalLayout.addWidget(self.frameRight)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.welldStackedWidget.addWidget(self.pageOverView)
        self.pageInfo = QWidget()
        self.pageInfo.setObjectName(u"pageInfo")
        self.horizontalLayout_2 = QHBoxLayout(self.pageInfo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.infoTableWidget = QTableWidget(self.pageInfo)
        if (self.infoTableWidget.columnCount() < 1):
            self.infoTableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.infoTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.infoTableWidget.rowCount() < 5):
            self.infoTableWidget.setRowCount(5)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.infoTableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.infoTableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.infoTableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.infoTableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.infoTableWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        self.infoTableWidget.setObjectName(u"infoTableWidget")

        self.horizontalLayout_2.addWidget(self.infoTableWidget)

        self.welldStackedWidget.addWidget(self.pageInfo)
        self.pageGuiji = QWidget()
        self.pageGuiji.setObjectName(u"pageGuiji")
        self.verticalLayout_8 = QVBoxLayout(self.pageGuiji)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.dragPushButton = QPushButton(self.pageGuiji)
        self.dragPushButton.setObjectName(u"dragPushButton")
        sizePolicy.setHeightForWidth(self.dragPushButton.sizePolicy().hasHeightForWidth())
        self.dragPushButton.setSizePolicy(sizePolicy)
        self.dragPushButton.setMinimumSize(QSize(100, 50))
        self.dragPushButton.setMaximumSize(QSize(16777215, 50))
        self.dragPushButton.setFont(font)
        self.dragPushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 234, 171);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:10px;\n"
"padding-left:5px;\n"
"}")
        self.dragPushButton.setCheckable(True)
        self.dragPushButton.setAutoRepeat(True)
        self.dragPushButton.setFlat(True)

        self.verticalLayout_8.addWidget(self.dragPushButton, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.savePushButton = QPushButton(self.pageGuiji)
        self.savePushButton.setObjectName(u"savePushButton")
        sizePolicy.setHeightForWidth(self.savePushButton.sizePolicy().hasHeightForWidth())
        self.savePushButton.setSizePolicy(sizePolicy)
        self.savePushButton.setMinimumSize(QSize(100, 50))
        self.savePushButton.setMaximumSize(QSize(16777215, 50))
        self.savePushButton.setFont(font)
        self.savePushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 234, 171);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:10px;\n"
"padding-left:5px;\n"
"}")
        self.savePushButton.setCheckable(True)
        self.savePushButton.setAutoRepeat(True)
        self.savePushButton.setFlat(True)

        self.verticalLayout_8.addWidget(self.savePushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.recordPushButton = QPushButton(self.pageGuiji)
        self.recordPushButton.setObjectName(u"recordPushButton")
        sizePolicy.setHeightForWidth(self.recordPushButton.sizePolicy().hasHeightForWidth())
        self.recordPushButton.setSizePolicy(sizePolicy)
        self.recordPushButton.setMinimumSize(QSize(100, 50))
        self.recordPushButton.setMaximumSize(QSize(16777215, 50))
        self.recordPushButton.setFont(font)
        self.recordPushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 234, 171);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:10px;\n"
"padding-left:5px;\n"
"}")
        self.recordPushButton.setCheckable(True)
        self.recordPushButton.setAutoRepeat(True)
        self.recordPushButton.setFlat(True)

        self.verticalLayout_8.addWidget(self.recordPushButton, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 2)
        self.verticalLayout_8.setStretch(2, 2)
        self.welldStackedWidget.addWidget(self.pageGuiji)
        self.pageDemo = QWidget()
        self.pageDemo.setObjectName(u"pageDemo")
        self.verticalLayout_4 = QVBoxLayout(self.pageDemo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.normalPushButton = QPushButton(self.pageDemo)
        self.normalPushButton.setObjectName(u"normalPushButton")
        sizePolicy.setHeightForWidth(self.normalPushButton.sizePolicy().hasHeightForWidth())
        self.normalPushButton.setSizePolicy(sizePolicy)
        self.normalPushButton.setMinimumSize(QSize(100, 50))
        self.normalPushButton.setMaximumSize(QSize(16777215, 50))
        self.normalPushButton.setFont(font)
        self.normalPushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 234, 171);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:10px;\n"
"padding-left:5px;\n"
"}")
        self.normalPushButton.setCheckable(True)
        self.normalPushButton.setAutoRepeat(True)
        self.normalPushButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.normalPushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.painPushButton = QPushButton(self.pageDemo)
        self.painPushButton.setObjectName(u"painPushButton")
        sizePolicy.setHeightForWidth(self.painPushButton.sizePolicy().hasHeightForWidth())
        self.painPushButton.setSizePolicy(sizePolicy)
        self.painPushButton.setMinimumSize(QSize(100, 50))
        self.painPushButton.setMaximumSize(QSize(16777215, 50))
        self.painPushButton.setFont(font)
        self.painPushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 234, 171);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:10px;\n"
"padding-left:5px;\n"
"}")
        self.painPushButton.setCheckable(True)
        self.painPushButton.setAutoRepeat(True)
        self.painPushButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.painPushButton, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.welldStackedWidget.addWidget(self.pageDemo)
        self.pageExplain = QWidget()
        self.pageExplain.setObjectName(u"pageExplain")
        self.verticalLayout_7 = QVBoxLayout(self.pageExplain)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.explainTextBrowser = QTextBrowser(self.pageExplain)
        self.explainTextBrowser.setObjectName(u"explainTextBrowser")
        self.explainTextBrowser.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.explainTextBrowser, 0, Qt.AlignLeft|Qt.AlignTop)

        self.welldStackedWidget.addWidget(self.pageExplain)
        self.pageAbout = QWidget()
        self.pageAbout.setObjectName(u"pageAbout")
        self.verticalLayout_5 = QVBoxLayout(self.pageAbout)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.aboutTextBrowser = QTextBrowser(self.pageAbout)
        self.aboutTextBrowser.setObjectName(u"aboutTextBrowser")
        self.aboutTextBrowser.setStyleSheet(u"background-color:white;")

        self.verticalLayout_5.addWidget(self.aboutTextBrowser, 0, Qt.AlignLeft|Qt.AlignTop)

        self.welldStackedWidget.addWidget(self.pageAbout)

        self.horizontalLayout_3.addWidget(self.welldStackedWidget)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)

        self.retranslateUi(WelldWidget)

        self.welldStackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(WelldWidget)
    # setupUi

    def retranslateUi(self, WelldWidget):
        WelldWidget.setWindowTitle(QCoreApplication.translate("WelldWidget", u"Form", None))

        __sortingEnabled = self.menuListWidget.isSortingEnabled()
        self.menuListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.menuListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("WelldWidget", u"\u6cbb\u7597\u6f14\u793a\u56fe", None));
        ___qlistwidgetitem1 = self.menuListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("WelldWidget", u"\u75c5\u4eba\u6863\u6848", None));
        ___qlistwidgetitem2 = self.menuListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("WelldWidget", u"\u8f68\u8ff9\u590d\u73b0", None));
        ___qlistwidgetitem3 = self.menuListWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("WelldWidget", u"\u6cbb\u7597\u6f14\u793a", None));
        ___qlistwidgetitem4 = self.menuListWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("WelldWidget", u"\u64cd\u4f5c\u8bf4\u660e", None));
        ___qlistwidgetitem5 = self.menuListWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("WelldWidget", u"\u5173\u4e8e", None));
        self.menuListWidget.setSortingEnabled(__sortingEnabled)

        self.jjTextBrowser.setHtml(QCoreApplication.translate("WelldWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u5b8b\u4f53'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:10pt; font-weight:700;\">\u80a9\u9888\u90e8</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:10pt;\">\u6cbb\u7597\u9888\u690e\u75c5\u3001\u843d\u6795\u3001\u9888\u75db\u3001\u9888"
                        "\u90e8\u808c\u8089\u632b\u4f24\u3001\u626d\u4f24\u53ca\u52b3\u635f\u3001\u80a9\u5468\u708e\u3001\u80a9\u80cc\u7275\u626f\u75db\u3001\u4e0a\u80a2\u6d3b\u52a8\u529f\u80fd\u969c\u788d\u7b49</span></p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("WelldWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u80f8\u80cc\u90e8</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u6cbb\u7597\u80f8\u80cc\u75bc\u75db\u3001\u7275\u62c9\u9178\u80c0\u3001\u80f8\u690e\u4fa7\u5f2f\u3001\u524d\u5c48\u8fc7\u5ea6\u7b49</span>"
                        "</p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("WelldWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u8170\u9ab6\u90e8</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u6cbb\u7597\u8170\u9ab6\u90e8\u75bc\u75db\u3001\u8170\u690e\u95f4\u76d8\u3001\u7a81\u51fa\u75c7\u3001\u8170\u9ab6\u90e8\u808c\u8089\u632b\u4f24"
                        "\u3001\u626d\u4f24\u53ca\u52b3\u635f\u7b49</span></p></body></html>", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("WelldWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u5927\u817f\u5916\u4fa7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u5927\u817f\u5916\u5c55\u56f0\u96be\u3001\u5c40\u90e8\u75bc\u75db\u3001\u4e0b\u80a2\u75c9\u631b\u7b49</span></p></body></html>", None))
        self.bodyLabel.setText("")
        self.textBrowser_5.setHtml(QCoreApplication.translate("WelldWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u81c0\u90e8</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u6cbb\u7597\u5750\u9aa8\u795e\u7ecf\u75db\u3001\u81c0\u90e8\u808c\u8089\u75bc\u75db\u3001\u884c\u8d70\u56f0\u96be\u7b49</span></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("WelldWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u8170\u90e8</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u6cbb\u7597\u8170\u75db\u3001\u8170\u690e\u95f4\u76d8\u7a81\u51fa\u75c7\u3001\u8170\u90e8\u6d3b\u52a8\u53d7\u9650\u7b49</span></p></body></html>", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("WelldWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u8179\u90e8</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u8179\u6cfb\u3001\u4fbf\u79d8\u3001\u524d\u5217\u817a\u708e\u3001\u524d\u5217\u817a\u589e\u751f\u3001\u5c3f\u9053\u708e\u3001\u76c6\u8154\u708e\u7b49"
                        "</span></p></body></html>", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("WelldWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u5c0f\u817f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u6cbb\u7597\u808c\u8089\u62c9\u4f24\u3001\u8fc7\u5ea6\u8fd0\u52a8\u540e\u9178\u75db\u3001\u75c9\u631b\u7b49</span></p></body></html>", None))
        ___qtablewidgetitem = self.infoTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WelldWidget", u"\u4fe1\u606f", None));
        ___qtablewidgetitem1 = self.infoTableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WelldWidget", u"ID", None));
        ___qtablewidgetitem2 = self.infoTableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WelldWidget", u"\u59d3\u540d", None));
        ___qtablewidgetitem3 = self.infoTableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WelldWidget", u"\u6027\u522b", None));
        ___qtablewidgetitem4 = self.infoTableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WelldWidget", u"\u5e74\u9f84", None));
        ___qtablewidgetitem5 = self.infoTableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WelldWidget", u"\u6cbb\u7597\u90e8\u4f4d", None));
        self.dragPushButton.setText(QCoreApplication.translate("WelldWidget", u"\u8fdb\u5165\u62d6\u62fd", None))
        self.savePushButton.setText(QCoreApplication.translate("WelldWidget", u"\u5b58\u8d77\u59cb\u70b9", None))
        self.recordPushButton.setText(QCoreApplication.translate("WelldWidget", u"\u5f00\u59cb\u8bb0\u5f55", None))
        self.normalPushButton.setText(QCoreApplication.translate("WelldWidget", u"\u5e38\u89c4\u6f14\u793a", None))
        self.painPushButton.setText(QCoreApplication.translate("WelldWidget", u"\u75db\u70b9\u6f14\u793a", None))
        self.explainTextBrowser.setHtml(QCoreApplication.translate("WelldWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7535\u5b50\u8bf4\u660e\u4e66</p></body></html>", None))
        self.aboutTextBrowser.setHtml(QCoreApplication.translate("WelldWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u8f6f\u4ef6\u540d\u79f0\uff1a\u5a01\u5c14\u5fb7\u8d85\u58f0\u5eb7\u590d\u673a\u5668\u4eba</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u8f6f\u4ef6\u7248\u672c\uff1a1.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margi"
                        "n-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u5b8c\u6574\u7248\u672c\uff1a1.0.0.0</span></p></body></html>", None))
    # retranslateUi

