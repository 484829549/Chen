import os
import socket
import sys
import time
import winsound
import json
import src.config as cfg
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QGuiApplication, QIcon, QPalette, QColor, QFont
from PySide6.QtCore import QFile, QIODevice, QCoreApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from src.audioPlayer import RobotAudioPlayer
from src.treatTimer import TimeThread
from src.welldPage import WelldWindow
from src.robot import Robot, RobotThread, ForceControl, RobotApi
from src.therapy import Therapy
from ui.UI_Form_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_cam_1_runing = False
        self.is_cam_2_runing = False
        self.is_cam_3_runing = False

        self.dragClickCount = 0
        self.isFineTune = False
        self.savePointClickCount = 0
        # for combobox and spinbox event
        self.currentComboIndex_1 = -1
        self.currentComboIndex_2 = -1
        self.currentComboIndex_3 = -1
        # for list item clicked event
        self.parentItemIndex = 0
        self.chooseMode = -1
        # for spinbox, read and save data from json
        self.plan_1_pointNum = int()
        self.plan_1 = dict()
        self.plan_2 = dict()
        self.plan_3 = dict()
        # file path && media path
        self.paraFilePath = self.getDirPath('file')
        self.mediaPath = self.getDirPath('media')
        self.imagePath = self.getDirPath('images')
        # define audio player
        self.audioPlayer_1 = RobotAudioPlayer()
        self.audioPlayer_2 = RobotAudioPlayer()
        self.audioPlayer_3 = RobotAudioPlayer()
        self.audioPlayer_1.setMediaDir(self.mediaPath)
        self.audioPlayer_2.setMediaDir(self.mediaPath)
        self.audioPlayer_3.setMediaDir(self.mediaPath)
        # define the gif
        self.waveGif_1 = QtGui.QMovie(os.path.join(self.imagePath, "wave.gif"))
        self.waveGif_2 = QtGui.QMovie(os.path.join(self.imagePath, "wave.gif"))
        self.waveGif_3 = QtGui.QMovie(os.path.join(self.imagePath, "wave.gif"))

        # 1. load ui file by QtDesigner
        # self.ui = self.readUiFile("./ui/UI_Form.ui")

        # 2. using the ui.py by QtDesigner (* recommend *)
        self.ui = Ui_MainWindow()  # by qt designer
        self.ui.setupUi(self)
        screen = QGuiApplication.primaryScreen().geometry()
        self.resize(screen.width(), screen.height())
        # show the main content page
        self.ui.contentStackedWidget_1.setCurrentIndex(0)
        self.ui.saveCancelStackedWidget_1.setCurrentIndex(1)

        self.ui.waveLabel_1.setMovie(self.waveGif_1)
        self.ui.waveLabel_2.setMovie(self.waveGif_2)
        self.ui.waveLabel_3.setMovie(self.waveGif_3)

        self.audioPlayer_1.setMedia("welcome.wav")
        self.audioPlayer_1.play()

        # init robot
        self.robotCtrl = Robot(cfg.address)
        self.robotCtrl.initRobot()
        self.robotApi = RobotApi(cfg.address)


        # init serial port
        # self.serials = Therapy(cfg.port, cfg.baudrate, cfg.timeout)

        # camera click event
        self.ui.cam1.clicked.connect(lambda: self.camera_click_show(1))
        self.ui.cam2.clicked.connect(lambda: self.camera_click_show(2))
        self.ui.cam3.clicked.connect(lambda: self.camera_click_show(3))

        self.ui.bodyTreeWidget.itemSelectionChanged.connect(
            self.bodyItem_click_show)

        self.ui.planComboBox_1.currentIndexChanged.connect(
            lambda: self.comboSelectChanged(1))
        self.ui.planComboBox_2.currentIndexChanged.connect(
            lambda: self.comboSelectChanged(2))
        self.ui.planComboBox_3.currentIndexChanged.connect(
            lambda: self.comboSelectChanged(3))

        self.ui.timeSpinBox_1.valueChanged.connect(lambda: self.timerSync(1))
        self.ui.timeSpinBox_2.valueChanged.connect(lambda: self.timerSync(2))
        self.ui.timeSpinBox_3.valueChanged.connect(lambda: self.timerSync(3))
        # self.ui.zkbSpinBox_1.valueChanged.connect(lambda: self.zkbHandler(1))
        # self.ui.freqSpinBox_1.valueChanged.connect(lambda: self.freqHandler(1))
        self.ui.speedSpinBox_1.valueChanged.connect(self.speedHandler)

        self.ui.soundDoubleSpinBox_1.valueChanged.connect(
            lambda: self.soundHandler(1))
        self.ui.soundDoubleSpinBox_2.valueChanged.connect(
            lambda: self.soundHandler(2))
        self.ui.soundDoubleSpinBox_3.valueChanged.connect(
            lambda: self.soundHandler(3))

        # self.ui.strengthSpinBox_1.valueChanged.connect()

        # set save&&cancel button event
        self.ui.cancelSelfPushButton_1.clicked.connect(
            self.cancelSelfBtn_click_show)
        self.ui.cancelSelfPushButton_2.clicked.connect(
            self.cancelSelfBtn_click_show)
        self.ui.cancelSelfPushButton_3.clicked.connect(
            self.cancelSelfBtn_click_show)

        self.ui.saveSelfPushButton_1.clicked.connect(
            self.saveSelfBtn_click_show)
        self.ui.saveSelfPushButton_2.clicked.connect(
            self.saveSelfBtn_click_show)
        self.ui.saveSelfPushButton_3.clicked.connect(
            self.saveSelfBtn_click_show)

        # set drag button event
        self.ui.pullPushButton_1.clicked.connect(self.dragBtn_click_show)
        # set save point button event
        self.ui.savePointPushButton_1.clicked.connect(self.pointBtn_click_show)
        # set switch button event
        self.ui.switch_1.clicked.connect(self.switch_button_click_show)
        self.ui.switch_2.clicked.connect(self.switch_button_click_show)
        # do fine tune event
        self.ui.up.clicked.connect(lambda: self.robotCtrl.fineTune('up'))
        self.ui.down.clicked.connect(lambda: self.robotCtrl.fineTune('down'))
        self.ui.leftrot.clicked.connect(
            lambda: self.robotCtrl.fineTune('leftrot'))
        self.ui.rightrot.clicked.connect(
            lambda: self.robotCtrl.fineTune('rightrot'))
        self.ui.front.clicked.connect(lambda: self.robotCtrl.fineTune('front'))
        self.ui.back.clicked.connect(lambda: self.robotCtrl.fineTune('back'))
        self.ui.left.clicked.connect(lambda: self.robotCtrl.fineTune('left'))
        self.ui.right.clicked.connect(lambda: self.robotCtrl.fineTune('right'))
        self.robotCtrl.fineTuneClicked.connect(self.changeIsFineTune)

        # set start button event
        self.ui.btnStart_1.clicked.connect(self.startBtn_click_show)
        self.ui.btnStart_2.clicked.connect(self.startBtn_click_show)
        self.ui.btnStart_3.clicked.connect(self.startBtn_click_show)
        # set pause button event
        self.ui.btnPause_1.clicked.connect(self.pauseBtn_click_show)
        self.ui.btnPause_2.clicked.connect(self.pauseBtn_click_show)
        self.ui.btnPause_3.clicked.connect(self.pauseBtn_click_show)
        # set stop button event
        self.ui.btnStop_1.clicked.connect(self.stopBtn_click_show)
        self.ui.btnStop_2.clicked.connect(self.stopBtn_click_show)
        self.ui.btnStop_3.clicked.connect(self.stopBtn_click_show)

        # set logo link
        self.ui.logo.clicked.connect(self.logo_click_show)
        self.ui.strengthSpinBox_1.valueChanged.connect(self.FT_strength)#--FT

    def FT_strength(self):
        FT_price = -self.ui.strengthSpinBox_1.value()
        cfg.force_torque[2] = float(FT_price)
        print(cfg.force_torque)

    def getDirPath(self, dir_name):
        for root, dirs, _ in os.walk('./'):
            for dir in dirs:
                if dir == dir_name:
                    return os.path.join(root, dir)

    def logo_click_show(self):
        print("Go to logo show page")
        self.welld_ui = WelldWindow()
        self.welld_ui.show()

    # receive signal from time thread

    def lcd_time_show_1(self, timeStr):
        # print("Page 1: LCD receives time string is {}".format(timeStr))
        self.ui.timerLcdNumber_1.display(timeStr)
        self.ui.state_lcd_1.display(timeStr)

    def lcd_time_show_2(self, timeStr):
        print("Page 2: LCD receives time string is {}".format(timeStr))
        self.ui.timerLcdNumber_2.display(timeStr)
        self.ui.state_lcd_2.display(timeStr)

    def lcd_time_show_3(self, timeStr):
        print("Page 3: LCD receives time string is {}".format(timeStr))
        self.ui.timerLcdNumber_3.display(timeStr)
        self.ui.state_lcd_3.display(timeStr)

    def time_speaker_1(self, flag):
        # init the runtime status for these buttons
        if flag == 0:
            self.audioPlayer_1.setMedia("start.wav")
            self.audioPlayer_1.play()
            self.waveGif_1.start()
            self.ui.btnStart_1.setEnabled(False)
            self.ui.btnPause_1.setEnabled(True)
            self.ui.btnStop_1.setEnabled(True)
        elif flag == 6:  # 1/2 time
            if self.parentItemIndex == 5 and self.chooseMode == 1:  # 仅臀部&&痛点
                self.robotCtrl.robot.ProgramStop()  # add new
                self.runtime_robot.setOneHalf(True)
                print("Main::Set is_half finished")
        elif flag == 7:  # 1/3 time
            if not self.parentItemIndex == 5 and self.chooseMode == 1:  # 除了臀部&&痛点
                self.robotCtrl.robot.ProgramStop()  # add new
                self.runtime_robot.setOneThird(True)
                print("Main::Set is_one_third finished")
        elif flag == 2:
            self.audioPlayer_1.setMedia("two_minute_left.wav")
            self.audioPlayer_1.play()
        elif flag == 3:
            self.audioPlayer_1.setMedia("finish.wav")
            self.audioPlayer_1.play()
            self.waveGif_1.stop()
            self.ui.btnStart_1.setEnabled(True)
            self.ui.btnPause_1.setEnabled(False)
            self.ui.btnStop_1.setEnabled(False)
            self.robotCtrl.robot.ProgramStop()  # add new
            self.runtime_robot.stop_thread(True)
            # self.runtime_robot.quit()
            # print("Robot quit SUCCESS, begin to wait...")
            # self.runtime_robot.wait()
            # print("Robot wait DONE")
            self.runtime_robot.deleteLater()
            self.is_cam_1_runing = False
        elif flag == 8:
            self.lcd_time_show_1("%02d:00" % (self.ui.timeSpinBox_1.value()))
            self.audioPlayer_1.setMedia("stop.wav")
            self.audioPlayer_1.play()
            self.waveGif_1.stop()
            self.ui.btnStart_1.setEnabled(True)
            self.ui.btnPause_1.setEnabled(False)
            self.ui.btnStop_1.setEnabled(False)
            # print("quit begin......")
            # self.timer_1.quit()
            # print("quit finished, wait begin......")
            # self.timer_1.wait()
            # print("wait finished")
            # self.timer_1.terminate()
            self.timer_1.deleteLater()
            self.is_cam_1_runing = False
        elif flag == 4:
            self.audioPlayer_1.setMedia("pause.wav")
            self.audioPlayer_1.play()
            self.waveGif_1.stop()
        elif flag == 5:
            self.audioPlayer_1.setMedia("recover.wav")
            self.audioPlayer_1.play()
            self.waveGif_1.start()
        else:
            # running
            pass

    def time_speaker_2(self, flag):
        # init the runtime status for these buttons
        if flag == 3:
            self.audioPlayer_2.setMedia("finish.wav")
            self.audioPlayer_2.play()
            self.waveGif_2.stop()
            self.ui.btnStart_2.setEnabled(True)
            self.ui.btnPause_2.setEnabled(False)
            self.ui.btnStop_2.setEnabled(False)
            self.timer_2.deleteLater()
            self.is_cam_2_runing = False
        elif flag == 2:
            self.audioPlayer_2.setMedia("two_minute_left.wav")
            self.audioPlayer_2.play()
        elif flag == 0:
            self.audioPlayer_2.setMedia("start.wav")
            self.audioPlayer_2.play()
            self.waveGif_2.start()
            self.ui.btnStart_2.setEnabled(False)
            self.ui.btnPause_2.setEnabled(True)
            self.ui.btnStop_2.setEnabled(True)
        elif flag == 4:
            self.audioPlayer_2.setMedia("pause.wav")
            self.audioPlayer_2.play()
            self.waveGif_2.stop()
        elif flag == 5:
            self.audioPlayer_2.setMedia("recover.wav")
            self.audioPlayer_2.play()
            self.waveGif_2.start()
        elif flag == 8:
            self.audioPlayer_2.setMedia("stop.wav")
            self.audioPlayer_2.play()
            self.waveGif_2.stop()
            self.ui.btnStart_2.setEnabled(True)
            self.ui.btnPause_2.setEnabled(False)
            self.ui.btnStop_2.setEnabled(False)
            self.timer_2.deleteLater()
            self.is_cam_2_runing = False
        else:
            # running
            pass

    def time_speaker_3(self, flag):
        # init the runtime status for these buttons
        if flag == 3:
            self.audioPlayer_3.setMedia("finish.wav")
            self.audioPlayer_3.play()
            self.waveGif_3.stop()
            self.ui.btnStart_3.setEnabled(True)
            self.ui.btnPause_3.setEnabled(False)
            self.ui.btnStop_3.setEnabled(False)
            self.timer_3.deleteLater()
            self.is_cam_3_runing = False
        elif flag == 2:
            self.audioPlayer_3.setMedia("two_minute_left.wav")
            self.audioPlayer_3.play()
        elif flag == 0:
            self.audioPlayer_3.setMedia("start.wav")
            self.audioPlayer_3.play()
            self.waveGif_3.start()
            self.ui.btnStart_3.setEnabled(False)
            self.ui.btnPause_3.setEnabled(True)
            self.ui.btnStop_3.setEnabled(True)
        elif flag == 4:
            self.audioPlayer_3.setMedia("pause.wav")
            self.audioPlayer_3.play()
            self.waveGif_3.stop()
        elif flag == 5:
            self.audioPlayer_3.setMedia("recover.wav")
            self.audioPlayer_3.play()
            self.waveGif_3.start()
        elif flag == 8:
            self.audioPlayer_3.setMedia("stop.wav")
            self.audioPlayer_3.play()
            self.waveGif_3.stop()
            self.ui.btnStart_3.setEnabled(True)
            self.ui.btnPause_3.setEnabled(False)
            self.ui.btnStop_3.setEnabled(False)
            self.timer_3.deleteLater()
            self.is_cam_3_runing = False
        else:
            # running
            pass

    def get_socket_info(self):
        """"
        函数：socket_con
        功能：获取机械臂报错
        参数：self
        返回值：无
        """
        # 连接端口获取信息
        Con_SOCKET = socket.socket()
        Con_SOCKET.connect(('192.168.58.2', 8083))
        RV = Con_SOCKET.recv(1024)
        dlg = QtWidgets.QMessageBox()
        text = str()

        if RV[6] == 1:
            text = QCoreApplication.translate(
                "MainWindow", u"驱动器故障,不可复位，断电重启机器人", None)
        elif RV[6] == 2:
            text = QCoreApplication.translate(
                "MainWindow", u"超出软限位故障,进入手动模式，手动拖拽机器人移动至限位内，可复位", None)
        elif RV[6] == 3:
            text = QCoreApplication.translate("MainWindow", u"碰撞故障,可复位", None)
        elif RV[6] == 4:
            text = QCoreApplication.translate(
                "MainWindow", u"奇异位姿,空间点位规划无解，不可复位，断电重启机器人", None)
        elif RV[6] == 5:
            text = QCoreApplication.translate(
                "MainWindow", u"从站错误,从站通讯异常，不可复位，断电重启机器人", None)
        elif RV[6] == 6:
            text = QCoreApplication.translate(
                "MainWindow", u"指令点错误,关节指令点错误，可复位", None)
        elif RV[6] == 7:
            text = QCoreApplication.translate(
                "MainWindow", u"IO 错误,通讯错误，不可复位，重启机器人", None)
        elif RV[6] == 8:
            text = QCoreApplication.translate(
                "MainWindow", u"夹爪错误,通讯错误，不可复位，重启机器人", None)
        elif RV[6] == 9:
            text = QCoreApplication.translate(
                "MainWindow", u"文件错误,通讯错误，不可复位，重启机器人", None)
        elif RV[6] == 10:
            text = QCoreApplication.translate(
                "MainWindow", u"参数错误,参数错误，可复位", None)
        elif RV[6] == 11:
            text = QCoreApplication.translate(
                "MainWindow", u"扩展轴超出软限位错误,进入手动模式，手动点动扩展轴至限位内，可复位", None)
        elif RV[6] == 12:
            text = QCoreApplication.translate(
                "MainWindow", u"关节配置警告,不可复位，断电重启机器人", None)
        else:
            return

        self.robotApi.clearAlarm()
        dlg.critical(self, "ERROR", text,
                     QtWidgets.QMessageBox.StandardButton.Ok)
        if self.is_cam_1_runing:
            self.ui.framePointAdjust.setEnabled(True)
            if not self.ui.btnStart_1.isEnabled():
                self.ui.btnStart_1.setEnabled(True)
            if self.ui.btnPause_1.isEnabled():
                self.ui.btnPause_1.setEnabled(False)
            if self.ui.btnStop_1.isEnabled():
                self.ui.btnStop_1.setEnabled(False)

            # self.timer_1.terminate()
            self.lcd_time_show_1("%02d:00" %
                                 (self.ui.timeSpinBox_1.value()))
            # self.runtime_robot.terminate()
            # self.strength_control.terminate()
            self.robotApi.ProgramStop()
            self.waveGif_1.stop()
            self.is_cam_1_runing = False

    def startBtn_click_show(self):
        match self.ui.contentStackedWidget_1.currentIndex():
            case 0:
                self.robotCtrl.robot.SetSpeed(self.ui.speedSpinBox_1.value())
                self.ui.framePointAdjust.setEnabled(False)
                self.ui.frameBodylist.setEnabled(False)
                self.timer_1 = TimeThread()
                self.pauseCount_1 = 0
                self.timer_1.valueChanged.connect(self.lcd_time_show_1)
                self.timer_1.statusSignal.connect(self.time_speaker_1)
                self.timer_1.socket.connect(self.get_socket_info)
                self.timer_1.setTime(self.ui.timeSpinBox_1.value())

                self.runtime_robot = RobotThread(cfg.address)
                self.robotCtrl.robot.SetSpeed(self.ui.speedSpinBox_1.value())
                self.runtime_robot.setBodyPart(self.robotCtrl.getIsHips())
                self.runtime_robot.setJoint(self.robotCtrl.getJoint())
                self.runtime_robot.setMode(self.robotCtrl.getMode())
                self.runtime_robot.setSpace(self.robotCtrl.getSpace())
                self.runtime_robot.setTPBName(self.robotCtrl.getTPBName())
                self.runtime_robot.setDirection(self.robotCtrl.getDirection())
                self.runtime_robot.start()
                self.timer_1.start()

                self.runtime_robot.stopTimerSignal.connect(
                    self.timer_1.pause_thread)
                self.runtime_robot.startTimerSignal.connect(
                    self.timer_1.resume_thread)
                self.runtime_robot.endSignal.connect(self.timer_1.stop_thread)

                # self.strength_control = ForceControl()
                # self.strength_control.start()

                self.is_cam_1_runing = True
            case 1:
                self.timer_2 = TimeThread()
                self.pauseCount_2 = 0
                self.timer_2.valueChanged.connect(self.lcd_time_show_2)
                self.timer_2.statusSignal.connect(self.time_speaker_2)
                self.timer_2.setTime(self.ui.timeSpinBox_2.value())
                self.timer_2.start()
                self.is_cam_2_runing = True
            case 2:
                self.timer_3 = TimeThread()
                self.pauseCount_3 = 0
                self.timer_3.valueChanged.connect(self.lcd_time_show_3)
                self.timer_3.statusSignal.connect(self.time_speaker_3)
                self.timer_3.setTime(self.ui.timeSpinBox_3.value())
                self.timer_3.start()
                self.is_cam_3_runing = True

    def pauseBtn_click_show(self):
        match self.ui.contentStackedWidget_1.currentIndex():
            case 0:
                self.pauseCount_1 += 1
                self.ui.btnStart_1.setEnabled(False)

                if self.pauseCount_1 % 2 == 1:
                    self.ui.spsButtonGroup_1.setExclusive(False)
                    self.ui.btnPause_1.setChecked(True)
                    self.ui.spsButtonGroup_1.setExclusive(True)
                    # pause thread
                    # self.timer_1.pause_thread()m
                    print("reach UI pauseBtn_click_show")
                    self.robotCtrl.robot.ProgramStop() #  moving
                    self.robotCtrl.robot.SetSpeed(self.ui.speedSpinBox_1.value())
                    self.runtime_robot.pause_thread()
                    # self.strength_control.pause_thread()

                else:
                    self.ui.spsButtonGroup_1.setExclusive(False)
                    self.ui.btnPause_1.setChecked(False)
                    self.ui.spsButtonGroup_1.setExclusive(True)
                    # resume thread
                    # self.timer_1.resume_thread()
                    self.runtime_robot.resume_thread()
                    # self.strength_control.resume_thread()

                print("count: {}, finally pause state is {}".format(
                    self.pauseCount_1, self.ui.btnPause_1.isChecked()))
            case 1:
                self.pauseCount_2 += 1
                self.ui.btnStart_2.setEnabled(False)
                if self.pauseCount_2 % 2 == 1:
                    self.ui.spsButtonGroup_2.setExclusive(False)
                    self.ui.btnPause_2.setChecked(True)
                    self.ui.spsButtonGroup_2.setExclusive(True)
                    # pause thread
                    self.timer_2.pause_thread()
                else:
                    self.ui.spsButtonGroup_2.setExclusive(False)
                    self.ui.btnPause_2.setChecked(False)
                    self.ui.spsButtonGroup_2.setExclusive(True)
                    # resume thread
                    self.timer_2.resume_thread()

                print("count: {}, finally pause state is {}".format(
                    self.pauseCount_2, self.ui.btnPause_2.isChecked()))
            case 2:
                self.pauseCount_3 += 1
                self.ui.btnStart_3.setEnabled(False)
                if self.pauseCount_3 % 2 == 1:
                    self.ui.spsButtonGroup_3.setExclusive(False)
                    self.ui.btnPause_3.setChecked(True)
                    self.ui.spsButtonGroup_3.setExclusive(True)
                    # pause thread
                    self.timer_3.pause_thread()
                else:
                    self.ui.spsButtonGroup_3.setExclusive(False)
                    self.ui.btnPause_3.setChecked(False)
                    self.ui.spsButtonGroup_3.setExclusive(True)
                    # resume thread
                    self.timer_3.resume_thread()

                print("count: {}, finally pause state is {}".format(
                    self.pauseCount_3, self.ui.btnPause_3.isChecked()))

    def stopBtn_click_show(self):
        match self.ui.contentStackedWidget_1.currentIndex():
            case 0:
                self.robotApi.ProgramStop()
                self.ui.frameBodylist.setEnabled(True)
                # runtime not allow point adjustment
                self.ui.framePointAdjust.setEnabled(True)

                # self.runtime_robot.finished.connect(self.runtime_robot.stop_thread)
                self.runtime_robot.stop_thread(False)
                self.runtime_robot.deleteLater()

                if self.robotCtrl.getMode() == 4:
                    self.robotApi.changeRobotMode(1)

                self.is_cam_1_runing = False
            case 1:
                self.timer_2.stop_thread()
                # self.timer_2.quit()
                # self.timer_2.wait()
                self.timer_2.deleteLater()
                self.lcd_time_show_2("%02d:00" %
                                     (self.ui.timeSpinBox_2.value()))
                self.is_cam_2_runing = False
            case 2:
                self.timer_3.stop_thread()
                # self.timer_3.quit()
                # self.timer_3.wait()
                self.timer_3.deleteLater()
                self.lcd_time_show_3("%02d:00" %
                                     (self.ui.timeSpinBox_3.value()))
                self.is_cam_3_runing = False

    def pointBtn_click_show(self):
        print("PointEvent::Into point button click event, need %d point" %
              self.plan_1_pointNum)
        self.savePointClickCount += 1

        if self.savePointClickCount > 1:
            self.ui.savePointPushButton_1.setText(QCoreApplication.translate(
                "MainWindow", u"  存点%d  " % self.savePointClickCount, None))

        print("PointEvent::point={}, drag flag={}, is fine tune={}".format(
            self.savePointClickCount, self.dragClickCount % 2, self.isFineTune))
        if (self.dragClickCount % 2 == 1 and not self.isFineTune) or (self.dragClickCount % 2 == 0 and self.isFineTune):
            self.robotCtrl.savePoint(self.savePointClickCount)
            self.audioPlayer_1.setMedia("record.wav")
            self.audioPlayer_1.play()
            print("PointEvent::point={} saved SUCCESS".format(
                self.savePointClickCount))
            if self.savePointClickCount == self.plan_1_pointNum and self.isFineTune:
                self.savePointReady()
            self.isFineTune = False
        else:
            print(QCoreApplication.translate(
                "MainWindow", u"ERROR: point %d 操作错误, 必须在微调之后或退出拖拽前保存点位" % self.savePointClickCount, None))
            self.savePointClickCount -= 1
            return

    def savePointReady(self):
        reply = QtWidgets.QMessageBox().information(self, 'INFO', QCoreApplication.translate(
            "MainWindow", u"所有点位均已保存, 可开始治疗!", None), QtWidgets.QMessageBox.StandardButton.Ok)
        self.ui.frameTimer_1.setEnabled(True)
        self.ui.btnPause_1.setEnabled(False)
        self.ui.btnStop_1.setEnabled(False)
        self.savePointClickCount = 0
        self.ui.framePointAdjust.setEnabled(False)
        self.ui.savePointPushButton_1.setText(
            QCoreApplication.translate("MainWindow", u"  存点1  ", None))

    def dragBtn_click_show(self):
        if self.isFineTune:
            print(QCoreApplication.translate(
                "MainWindow", u"ERROR: 微调后必须先保存点位, 否则无法拖拽!", None))
            return
        self.dragClickCount += 1
        if self.dragClickCount % 2 == 1:
            self.ui.pullPushButton_1.setText(
                QCoreApplication.translate("MainWindow", u"退出拖拽", None))
            self.audioPlayer_1.setMedia("indrag.wav")
            self.audioPlayer_1.play()
            self.robotApi.drag(1)
        else:
            self.ui.pullPushButton_1.setText(
                QCoreApplication.translate("MainWindow", u"进入拖拽", None))
            self.audioPlayer_1.setMedia("outdrag.wav")
            self.audioPlayer_1.play()
            if self.savePointClickCount == self.plan_1_pointNum:
                self.savePointReady()
            self.robotApi.drag(0)

        self.beep()

    def switch_button_click_show(self):
        if self.ui.adjustStackedWidget_1.currentIndex() == 0:
            self.ui.adjustStackedWidget_1.setCurrentIndex(1)
        else:
            self.ui.adjustStackedWidget_1.setCurrentIndex(0)
        self.beep()

    def changeIsFineTune(self, flag):
        print("Receive fine tune signal")
        self.isFineTune = flag

    def comboSelectChanged(self, index):
        if index == 1:
            self.ui.zkbLabel_1.setEnabled(True)
            self.ui.zkbSpinBox_1.setEnabled(True)
            self.ui.freqLabel_1.setEnabled(True)
            self.ui.freqSpinBox_1.setEnabled(True)
            self.ui.speedLabel_1.setEnabled(True)
            self.ui.speedSpinBox_1.setEnabled(True)
            self.ui.soundLabel_1.setEnabled(True)
            self.ui.soundDoubleSpinBox_1.setEnabled(True)
            self.ui.timeLabel_1.setEnabled(True)
            self.ui.timeSpinBox_1.setEnabled(True)
            self.ui.strengthLabel.setEnabled(True)
            self.ui.strengthSpinBox_1.setEnabled(True)

            if not self.ui.cancelSelfPushButton_1.isEnabled():
                self.ui.cancelSelfPushButton_1.setEnabled(True)

            if not self.ui.saveSelfPushButton_1.isEnabled():
                self.ui.saveSelfPushButton_1.setEnabled(True)

            if self.ui.planComboBox_1.currentIndex() == 0:
                # show the save&&cancel button
                self.ui.saveCancelStackedWidget_1.setCurrentIndex(0)
                self.ui.saveCancelStackedWidget_1.setStyleSheet(
                    "QStackedWidget#stackedWidget{background-color:transparent;}")
            else:
                self.ui.saveCancelStackedWidget_1.setCurrentIndex(1)

            # auto fill the spin boxes
            currentComboText = self.ui.planComboBox_1.currentText()
            if currentComboText != "":
                print("Self Setting cancelled, combo text is {}".format(
                    currentComboText))
                self.ui.zkbSpinBox_1.setValue(
                    self.plan_1[currentComboText]["zkb"])
                self.ui.freqSpinBox_1.setValue(
                    self.plan_1[currentComboText]["frequence"])
                self.ui.speedSpinBox_1.setValue(
                    self.plan_1[currentComboText]["speed"])
                self.ui.soundDoubleSpinBox_1.setValue(
                    self.plan_1[currentComboText]["ultrasoundIntensity"])
                self.ui.timeSpinBox_1.setValue(
                    self.plan_1[currentComboText]["time"])
                self.ui.strengthSpinBox_1.setValue(
                    self.plan_1[currentComboText]["strength"])

            # set lcd time clock
            self.timerSync(1)
            # show the point frame
            if self.ui.planComboBox_1.currentIndex() > 0:
                self.ui.framePointAdjust.setEnabled(True)
                if cfg.istest:
                    self.ui.framePointAdjust.setEnabled(False)
                    self.ui.frameTimer_1.setEnabled(True)
                else:
                    self.ui.adjustStackedWidget_1.setEnabled(True)
                self.dragClickCount = 0
                self.savePointClickCount = 0
            else:
                self.ui.framePointAdjust.setEnabled(False)
                self.ui.frameTimer_1.setEnabled(False)

        elif index == 2:
            self.ui.zkbLabel_2.setEnabled(True)
            self.ui.zkbSpinBox_2.setEnabled(True)
            self.ui.freqLabel_2.setEnabled(True)
            self.ui.freqSpinBox_2.setEnabled(True)
            self.ui.soundLabel_2.setEnabled(True)
            self.ui.soundDoubleSpinBox_2.setEnabled(True)
            self.ui.timeLabel_2.setEnabled(True)
            self.ui.timeSpinBox_2.setEnabled(True)
            if not self.ui.cancelSelfPushButton_2.isEnabled():
                self.ui.cancelSelfPushButton_2.setEnabled(True)

            if not self.ui.saveSelfPushButton_2.isEnabled():
                self.ui.saveSelfPushButton_2.setEnabled(True)

            if self.ui.planComboBox_2.currentIndex() == 0:
                # show the save&&cancel button
                self.ui.saveStackedWidget_1.setCurrentIndex(0)
                self.ui.cancelStackedWidget_1.setCurrentIndex(1)
                if self.ui.frameTimer_2.isEnabled():
                    self.ui.frameTimer_2.setEnabled(False)
            else:
                self.ui.saveStackedWidget_1.setCurrentIndex(1)
                self.ui.cancelStackedWidget_1.setCurrentIndex(0)

            # auto fill the spin boxes
            currentComboText = self.ui.planComboBox_2.currentText()
            self.currentComboIndex_2 = self.ui.planComboBox_2.currentIndex()
            if currentComboText != "":
                print("combo text is {}".format(currentComboText))
                self.ui.zkbSpinBox_2.setValue(
                    self.plan_2[currentComboText]["zkb"])
                self.ui.freqSpinBox_2.setValue(
                    self.plan_2[currentComboText]["frequence"])
                self.ui.soundDoubleSpinBox_2.setValue(
                    self.plan_2[currentComboText]["ultrasoundIntensity"])
                self.ui.timeSpinBox_2.setValue(
                    self.plan_2[currentComboText]["time"])
             # set lcd time clock
            self.timerSync(2)
            if self.ui.planComboBox_2.currentIndex() > 0:
                self.ui.frameTimer_2.setEnabled(True)

        elif index == 3:
            self.ui.zkbLabel_3.setEnabled(True)
            self.ui.zkbSpinBox_3.setEnabled(True)
            self.ui.freqLabel_3.setEnabled(True)
            self.ui.freqSpinBox_3.setEnabled(True)
            self.ui.soundLabel_3.setEnabled(True)
            self.ui.soundDoubleSpinBox_3.setEnabled(True)
            self.ui.timeLabel_3.setEnabled(True)
            self.ui.timeSpinBox_3.setEnabled(True)
            if not self.ui.cancelSelfPushButton_3.isEnabled():
                self.ui.cancelSelfPushButton_3.setEnabled(True)

            if not self.ui.saveSelfPushButton_3.isEnabled():
                self.ui.saveSelfPushButton_3.setEnabled(True)

            if self.ui.planComboBox_3.currentIndex() == 0:
                # show the save&&cancel button
                self.ui.saveStackedWidget_2.setCurrentIndex(0)
                self.ui.cancelStackedWidget_2.setCurrentIndex(0)
                if self.ui.frameTimer_3.isEnabled():
                    self.ui.frameTimer_3.setEnabled(False)
            else:
                self.ui.saveStackedWidget_2.setCurrentIndex(1)
                self.ui.cancelStackedWidget_2.setCurrentIndex(1)

            # auto fill the spin boxes
            currentComboText = self.ui.planComboBox_3.currentText()
            self.currentComboIndex_3 = self.ui.planComboBox_3.currentIndex()
            if currentComboText != "":
                print("combo index is {}".format(self.currentComboIndex_3))
                self.ui.zkbSpinBox_3.setValue(
                    self.plan_3[currentComboText]["zkb"])
                self.ui.freqSpinBox_3.setValue(
                    self.plan_3[currentComboText]["frequence"])
                self.ui.soundDoubleSpinBox_3.setValue(
                    self.plan_3[currentComboText]["ultrasoundIntensity"])
                self.ui.timeSpinBox_3.setValue(
                    self.plan_3[currentComboText]["time"])
             # set lcd time clock
            self.timerSync(3)
            if self.ui.planComboBox_3.currentIndex() > 0:
                self.ui.frameTimer_3.setEnabled(True)

    def zkbHandler(self, index):
        # self.timerSync(index)
        pass

    def freqHandler(self, index):
        # self.timerSync(index)
        pass

    def speedHandler(self):
        # self.timerSync(1)
        self.robotCtrl.robot.SetSpeed(self.ui.speedSpinBox_1.value())

    def soundHandler(self, index):
        if index == 1:
            curValue = self.ui.soundDoubleSpinBox_1.value()
            if curValue <= 1.0:
                self.ui.soundDoubleSpinBox_1.setRange(0.1, 1)
                self.ui.soundDoubleSpinBox_1.setSingleStep(0.1)
                self.ui.soundDoubleSpinBox_1.setRange(0.1, 3)
            else:
                self.ui.soundDoubleSpinBox_1.setRange(1.2, 3)
                self.ui.soundDoubleSpinBox_1.setSingleStep(0.2)
                self.ui.soundDoubleSpinBox_1.setRange(0.1, 3)
        elif index == 2:
            curValue = self.ui.soundDoubleSpinBox_2.value()
            if curValue <= 1.0:
                self.ui.soundDoubleSpinBox_2.setRange(0.1, 1)
                self.ui.soundDoubleSpinBox_2.setSingleStep(0.1)
                self.ui.soundDoubleSpinBox_2.setRange(0.1, 3)
            else:
                self.ui.soundDoubleSpinBox_2.setRange(1.2, 3)
                self.ui.soundDoubleSpinBox_2.setSingleStep(0.2)
                self.ui.soundDoubleSpinBox_2.setRange(0.1, 3)
        else:
            curValue = self.ui.soundDoubleSpinBox_3.value()
            if curValue <= 1.0:
                self.ui.soundDoubleSpinBox_3.setRange(0.1, 1)
                self.ui.soundDoubleSpinBox_3.setSingleStep(0.1)
                self.ui.soundDoubleSpinBox_3.setRange(0.1, 3)
            else:
                self.ui.soundDoubleSpinBox_3.setRange(1.2, 3)
                self.ui.soundDoubleSpinBox_3.setSingleStep(0.2)
                self.ui.soundDoubleSpinBox_3.setRange(0.1, 3)

        # self.timerSync(index)

    def timerSync(self, index):
        if index == 1:
            if not self.is_cam_1_runing:
                self.ui.timerLcdNumber_1.display(
                    "%02d:00" % (self.ui.timeSpinBox_1.value()))
                self.ui.btnStart_1.setEnabled(True)
                self.ui.btnPause_1.setEnabled(False)
                self.ui.btnStop_1.setEnabled(False)
            # else:
            #     self.timer_1.setTime(self.ui.timeSpinBox_1.value())
            #     print("timer 1 is changed in runtime")

        elif index == 2:
            if not self.is_cam_2_runing:
                self.ui.timerLcdNumber_2.display(
                    "%02d:00" % (self.ui.timeSpinBox_2.value()))
                self.ui.btnStart_2.setEnabled(True)
                self.ui.btnPause_2.setEnabled(False)
                self.ui.btnStop_2.setEnabled(False)
            # else:
            #     if self.ui.timeSpinBox_2.value() != self.timer_2.timeSet/60:
            #         self.timer_2.setTime(self.ui.timeSpinBox_2.value())
            #         print("timer 2 is changed in runtime")
        elif index == 3:
            if not self.is_cam_3_runing:
                self.ui.timerLcdNumber_3.display(
                    "%02d:00" % (self.ui.timeSpinBox_3.value()))
                self.ui.btnStart_3.setEnabled(True)
                self.ui.btnPause_3.setEnabled(False)
                self.ui.btnStop_3.setEnabled(False)
            # else:
            #     if self.ui.timeSpinBox_3.value() != self.timer_3.timeSet/60:
            #         self.timer_3.setTime(self.ui.timeSpinBox_3.value())
            #         print("timer 3 is changed in runtime")

    def cancelSelfBtn_click_show(self):
        print("click cancel button")
        if self.ui.contentStackedWidget_1.currentIndex() == 0:
            self.ui.saveCancelStackedWidget_1.setCurrentIndex(1)

            self.ui.planComboBox_1.setCurrentIndex(-1)
            self.ui.zkbLabel_1.setEnabled(False)
            self.ui.zkbSpinBox_1.setEnabled(False)
            self.ui.freqLabel_1.setEnabled(False)
            self.ui.freqSpinBox_1.setEnabled(False)
            self.ui.speedLabel_1.setEnabled(False)
            self.ui.speedSpinBox_1.setEnabled(False)
            self.ui.soundLabel_1.setEnabled(False)
            self.ui.soundDoubleSpinBox_1.setEnabled(False)
            self.ui.timeLabel_1.setEnabled(False)
            self.ui.timeSpinBox_1.setEnabled(False)

            self.ui.framePointAdjust.setEnabled(False)
            self.ui.frameTimer_1.setEnabled(False)

        elif self.ui.contentStackedWidget_1.currentIndex() == 1:
            self.ui.saveStackedWidget_1.setCurrentIndex(1)
            self.ui.cancelStackedWidget_1.setCurrentIndex(0)

            self.ui.planComboBox_2.setCurrentIndex(-1)
            self.ui.zkbLabel_2.setEnabled(False)
            self.ui.zkbSpinBox_2.setEnabled(False)
            self.ui.freqLabel_2.setEnabled(False)
            self.ui.freqSpinBox_2.setEnabled(False)
            self.ui.soundLabel_2.setEnabled(False)
            self.ui.soundDoubleSpinBox_2.setEnabled(False)
            self.ui.timeLabel_2.setEnabled(False)
            self.ui.timeSpinBox_2.setEnabled(False)

            self.ui.frameTimer_2.setEnabled(False)
        else:
            self.ui.saveStackedWidget_1.setCurrentIndex(1)
            self.ui.cancelStackedWidget_1.setCurrentIndex(1)

            self.ui.planComboBox_3.setCurrentIndex(-1)
            self.ui.zkbLabel_3.setEnabled(False)
            self.ui.zkbSpinBox_3.setEnabled(False)
            self.ui.freqLabel_3.setEnabled(False)
            self.ui.freqSpinBox_3.setEnabled(False)
            self.ui.soundLabel_3.setEnabled(False)
            self.ui.soundDoubleSpinBox_3.setEnabled(False)
            self.ui.timeLabel_3.setEnabled(False)
            self.ui.timeSpinBox_3.setEnabled(False)

            self.ui.frameTimer_3.setEnabled(False)

    def saveSelfBtn_click_show(self):
        if self.ui.contentStackedWidget_1.currentIndex() == 0:
            body = self.bodyCurItem.parent().text(0)
            mode = self.bodyCurItem.text(0)
            zkb = self.ui.zkbSpinBox_1.value()
            freq = self.ui.freqSpinBox_1.value()
            speed = self.ui.speedSpinBox_1.value()
            sound = self.ui.soundDoubleSpinBox_1.value()
            time = self.ui.timeSpinBox_1.value()
            dlg = QtWidgets.QInputDialog(self)
            planName, ok = dlg.getText(self, '请输入方案保存名', '方案:')
            if ok:
                print("方案名为：%s" % planName)
                addItem = {"bodyName": body, "mode": mode, "type": "yours", "optionName": planName, "pointsNum": self.plan_1_pointNum,
                           "parameters": {"zkb": zkb, "frequence": freq, "speed": speed, "ultrasoundIntensity": sound, "time": time}
                           }
                with open(os.path.join(self.paraFilePath, "cam1.json"), "r+", encoding="utf-8") as f:
                    data = json.load(f)
                    data["treatDetail"].append(addItem)
                    f.seek(0, 0)
                    f.truncate()
                    json.dump(data, f, ensure_ascii=False)
                    f.close()

                # hide the save&&cancel buttons
                self.ui.saveCancelStackedWidget_1.setCurrentIndex(1)
                # update the combo items
                self.getBodySetFromJson()
                # show the latest items
                self.ui.planComboBox_1.setCurrentIndex(
                    self.ui.planComboBox_1.count()-1)
            else:
                dlg.close()
        elif self.ui.contentStackedWidget_1.currentIndex() == 1:
            zkb = self.ui.zkbSpinBox_2.value()
            freq = self.ui.freqSpinBox_2.value()
            sound = self.ui.soundDoubleSpinBox_2.value()
            time = self.ui.timeSpinBox_2.value()
            # add to ui.py in future
            dlg = QtWidgets.QInputDialog(self)
            planName, ok = dlg.getText(self, '请输入方案保存名', '方案:')
            if ok:
                print("方案名为：%s" % planName)
                addItem = {"type": "yours", "optionName": planName, "parameters":
                           {"zkb": zkb, "frequence": freq,
                               "ultrasoundIntensity": sound, "time": time}
                           }
                with open(os.path.join(self.paraFilePath, "cam2.json"), "r+", encoding="utf-8") as f:
                    data = json.load(f)
                    data["treatDetail"].append(addItem)
                    f.seek(0, 0)
                    f.truncate()
                    json.dump(data, f, ensure_ascii=False)
                    f.close()

                # hide the save&&cancel buttons
                self.ui.saveStackedWidget_1.setCurrentIndex(1)
                self.ui.cancelStackedWidget_1.setCurrentIndex(0)
                # update the combo items
                self.getPlanFromJson(2, self.ui.planComboBox_2.count()-1)

            else:
                dlg.close()
        else:
            zkb = self.ui.zkbSpinBox_3.value()
            freq = self.ui.freqSpinBox_3.value()
            sound = self.ui.soundDoubleSpinBox_3.value()
            time = self.ui.timeSpinBox_3.value()
            # add to ui.py in future
            dlg = QtWidgets.QInputDialog(self)
            planName, ok = dlg.getText(self, '请输入方案保存名', '方案:')
            if ok:
                print("方案名为：%s" % planName)
                addItem = {"type": "yours", "optionName": planName, "parameters":
                           {"zkb": zkb, "frequence": freq,
                               "ultrasoundIntensity": sound, "time": time}
                           }
                with open(os.path.join(self.paraFilePath, "cam3.json"), "r+", encoding="utf-8") as f:
                    data = json.load(f)
                    data["treatDetail"].append(addItem)
                    f.seek(0, 0)
                    f.truncate()
                    json.dump(data, f, ensure_ascii=False)
                    f.close()

                # hide the save&&cancel buttons
                self.ui.saveStackedWidget_2.setCurrentIndex(1)
                self.ui.cancelStackedWidget_2.setCurrentIndex(1)
                # update the combo items
                self.getPlanFromJson(3, self.ui.planComboBox_3.count()-1)

            else:
                dlg.close()

    def camera_click_show(self, index):
        if index == 1:
            print("camera 1 is checked, current combo text is %s" %
                  self.currentComboIndex_1)
            self.ui.contentStackedWidget_1.setCurrentIndex(0)  # body treat
            self.audioPlayer_1.setMedia("cam1.wav")
            self.audioPlayer_1.play()
            self.ui.frameBodylist.setEnabled(True)
            self.ui.bodyTreeWidget.setEnabled(True)

        elif index == 2:
            print("Begin: camera 2 is checked, current combo index is %s" %
                  (self.currentComboIndex_2))
            self.ui.contentStackedWidget_1.setCurrentIndex(1)
            self.audioPlayer_1.setMedia("cam2.wav")
            self.audioPlayer_1.play()
            self.ui.saveStackedWidget_1.setCurrentIndex(1)
            self.getPlanFromJson(index, self.currentComboIndex_2)

        else:
            print("Begin: camera 3 is checked, current combo index is %s" %
                  self.currentComboIndex_3)
            self.ui.contentStackedWidget_1.setCurrentIndex(2)
            self.audioPlayer_1.setMedia("cam3.wav")
            self.audioPlayer_1.play()
            self.getPlanFromJson(index, self.currentComboIndex_3)

    def bodyItem_click_show(self):
        self.ui.framePointAdjust.setEnabled(False)
        self.ui.frameTimer_1.setEnabled(False)
        self.bodyCurItem = self.ui.bodyTreeWidget.currentItem()
        if self.bodyCurItem.parent() is not None:
            print("当前治疗模式为: %s, 选择的治疗部位是--%s--" %
                  (self.bodyCurItem.text(0), self.bodyCurItem.parent().text(0)))

            self.ui.framePara_1.setEnabled(True)
            # import the treatment options, create and update
            self.getBodySetFromJson()

            # robot moves to the position of the point
            self.parentItemIndex = self.ui.bodyTreeWidget.indexOfTopLevelItem(
                self.bodyCurItem.parent())
            print("click item is %d" % self.parentItemIndex)
            match self.parentItemIndex:
                case 0:
                    self.robotCtrl.setBodyPoint(1)
                case 1 | 2 | 3 | 5:
                    self.robotCtrl.setBodyPoint(2)
                case 4:
                    self.robotCtrl.setBodyPoint(2)
                case 6 | 7:
                    self.robotCtrl.setBodyPoint(3)

            # set normal or pain treatment
            if self.bodyCurItem.text(0) == QCoreApplication.translate("MainWindow", u"常规治疗", None):
                self.chooseMode = 0
                self.normalTreat()
            elif self.bodyCurItem.text(0) == QCoreApplication.translate("MainWindow", u"痛点治疗", None):
                self.chooseMode = 1
                self.painTreat()
            elif self.bodyCurItem.text(0) == QCoreApplication.translate("MainWindow", u"顺时针", None):
                self.robotCtrl.setDirection(1)
                self.normalTreat()
            elif self.bodyCurItem.text(0) == QCoreApplication.translate("MainWindow", u"逆时针", None):
                self.robotCtrl.setDirection(0)
                self.normalTreat()
            else:
                # for FUBU in future ???
                pass

        else:
            self.ui.planComboBox_1.setCurrentIndex(-1)
            self.ui.framePara_1.setEnabled(False)

        self.beep()

    def normalTreat(self):
        if self.parentItemIndex == 1 or self.parentItemIndex == 2 or self.parentItemIndex == 6 or self.parentItemIndex == 7:
            self.robotCtrl.setMode(1)
            self.robotCtrl.setIsHips(False)
            if self.parentItemIndex == 1 or self.parentItemIndex == 2:
                self.robotCtrl.setBodyPoint(2)
            elif self.parentItemIndex == 6:
                self.robotCtrl.setBodyPoint(3)
                self.robotCtrl.setIsHips(True)
            elif self.parentItemIndex == 7:
                self.robotCtrl.setBodyPoint(3)
        elif self.parentItemIndex == 3:
            self.robotCtrl.setMode(2)
            self.robotCtrl.setBodyPoint(2)
        elif self.parentItemIndex == 4:
            self.robotCtrl.setMode(3)
            self.robotCtrl.setBodyPoint(2)

        self.beep()

    def painTreat(self):
        if self.parentItemIndex == 5:
            self.robotCtrl.setBodyPoint(2)
            self.robotCtrl.setMode(2)
            self.robotCtrl.setIsHips(True)

        elif self.parentItemIndex == 0 or self.parentItemIndex == 1 or self.parentItemIndex == 2:
            self.robotCtrl.setMode(1)
            self.robotCtrl.setIsHips(False)
            # self.robotCtrl.setIsHips(True)
            if self.parentItemIndex == 0:
                self.robotCtrl.setBodyPoint(1)
            else:
                self.robotCtrl.setBodyPoint(2)

        self.beep()

    # this function will trigger comboBox changed signal

    def getPlanFromJson(self, index, num):
        if index == 1:
            pass
        elif index == 2:
            fileName = os.path.join(self.paraFilePath, "cam2.json")
            with open(fileName, "r", encoding="utf-8") as f:
                jsonStr = json.load(f)
                self.ui.planComboBox_2.clear()
                self.ui.planComboBox_2.addItem("自定义")
                self.plan_2["自定义"] = {
                    'zkb': 10, 'frequence': 1, 'ultrasoundIntensity': 0.1, 'time': 1}
                for treat in jsonStr["treatDetail"]:
                    self.plan_2[treat["optionName"]] = treat["parameters"]
                    self.ui.planComboBox_2.addItem(treat["optionName"])
                f.close()
            self.ui.planComboBox_2.setCurrentIndex(num)
        else:
            fileName = os.path.join(self.paraFilePath, "cam3.json")
            with open(fileName, "r", encoding="utf-8") as f:
                jsonStr = json.load(f)
                self.ui.planComboBox_3.clear()
                self.ui.planComboBox_3.addItem("自定义")
                self.plan_3["自定义"] = {
                    'zkb': 10, 'frequence': 1, 'ultrasoundIntensity': 0.1, 'time': 1}
                for treat in jsonStr["treatDetail"]:
                    self.plan_3[treat["optionName"]] = treat["parameters"]
                    self.ui.planComboBox_3.addItem(treat["optionName"])
                f.close()
            self.ui.planComboBox_3.setCurrentIndex(num)

    def getBodySetFromJson(self):
        curBody = self.bodyCurItem.parent().text(0)
        curMode = self.bodyCurItem.text(0)
        # the page has body list
        fileName = os.path.join(self.paraFilePath, "cam1.json")
        print("open the file %s" % (fileName))
        with open(fileName, "r", encoding="utf-8") as f:
            jsonStr = json.load(f)
            self.ui.planComboBox_1.clear()
            self.ui.planComboBox_1.addItem("自定义")
            self.plan_1["自定义"] = {'zkb': 10, 'frequence': 1,
                                  'speed': 1, 'ultrasoundIntensity': 0.1, 'time': 1, 'strength': 1}
            for treat in jsonStr["treatDetail"]:
                if treat["bodyName"] == curBody and treat["mode"] == curMode:
                    self.plan_1[treat["optionName"]] = treat["parameters"]
                    if treat["pointsNum"] != 0:
                        self.plan_1_pointNum = treat["pointsNum"]
                    self.ui.planComboBox_1.addItem(treat["optionName"])
            f.close()
        self.ui.planComboBox_1.setCurrentIndex(-1)

    def beep(self):
        # beeper
        winsound.Beep(cfg.beeperfreq, cfg.beeperDuration)

    def readUiFile(self, filePath):
        # load the ui file
        ui_file = QFile(filePath)
        if not ui_file.open(QIODevice.ReadOnly):
            print("Open ui file error")
            sys.exit(-1)

        loader = QUiLoader()
        window = loader.load(ui_file)
        ui_file.close()

        return window


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.ui.show()  # for ui loader to show
    window.show()  # for object to show
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
