import sys
import os
pythonpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, pythonpath)
import socket
import src.config as cfg
from PySide6.QtCore import QObject, QThread, Signal, QWaitCondition, QMutex, QMutexLocker
import frrpc
import time
import struct
import copy


class RobotApi(QObject):

    def __init__(self, address) -> None:
        super().__init__()
        self.robot = frrpc.RPC(address)

        self.ep0 = [0.000, 0.000, 0.000, 0.000]
        self.dp0 = [0.000, 0.000, 0.000, 0.000, 0.000, 0.000]
        self.pa2 = [0.0, 1.0, 50.0, 50.0]

        self.status = 1  # 恒力控制开启标志，0-关，1-开

    def ImmStopJOG(self):#jog 点动立即停止
        self.robot.ImmStopJOG()

    def SetWebTPDStop(self):# 停止记录示教轨迹
        self.robot.SetWebTPDStop()

    def LoadTPD(self, nameTPB):# 轨迹预加载
        self.robot.LoadTPD(nameTPB)

    def MoveTPD(self, nameTPB, blend, ovl):# 轨迹复现
        self.robot.MoveTPD(nameTPB, blend, ovl)

    def SetTPDStart(self, type, nameTPB, period, di_choose, do_choose):# 开始记录示教轨迹
        self.robot.SetTPDStart(type, nameTPB, period, di_choose, do_choose)

    def SetTPDParam(self, type, nameTPB, period, di_choose, do_choose):# 配置 TPD 参数
        self.robot.SetTPDParam(type, nameTPB, period, di_choose, do_choose)

    def GetRobotMotionDone(self):# 查询机器人运动完成状态
        ret = self.robot.GetRobotMotionDone()
        return ret

    def GetProgramState(self):#获取机器人作业程序执行状态
        ret = self.robot.GetProgramState()
        return ret

    def GetForwardKin(self, flag):#只有关节位置的情况下，可用正运动学接口求解笛卡尔空间坐标
        ret = self.robot.GetForwardKin(flag)
        return ret

    def GetActualJointPosDegree(self, flag):#获取当前关节位置(角度)
        ret = self.robot.GetActualJointPosDegree(flag)
        return ret

    def GetActualTCPPose(self, flag):# 获取机器人当前工具位姿
        ret = self.robot.GetActualTCPPose(flag)
        return ret

    def SetSpeed(self, speed):# 设置全局速度，手动模式与自动模式独立设置
        self.robot.SetSpeed(speed)

    def drag(self, mode):#控制机器人进入或退出拖动示教模式
        # a=1: go into, a=0: go out
        self.robot.DragTeachSwitch(mode)

    def clearAlarm(self):#错误状态清除
        self.robot.ResetAllError()

    def ProgramStop(self):#终止当前运行的作业程序
        self.robot.ProgramStop()

    def ProgramPause(self):# 暂停正在执行的机器人程序
        self.robot.ProgramPause()

    def ProgramResume(self):# 恢复暂停执行的机器人程序
        self.robot.ProgramResume()

    def changeRobotMode(self, mode):#控制机器人手自动模式切换
        self.robot.Mode(mode)

    def StartJOG(self, ref, nb, dir, max_dis):#jog 点动
        self.robot.StartJOG(ref, nb, dir, 100.0, 100.0, max_dis)

    def MoveCart(self, space):#笛卡尔空间点到点运动
        ret = self.robot.MoveCart(space, 0, 1, 100.0, 180.0, 100.0, 500.0, -1)
        if (ret == 0):
            print("MoveCart is right")
        else:
            print("MoveCart is error")

    def MoveL(self, joint, space, blendR):# 笛卡尔空间直线运动
        ret = self.robot.MoveL(joint, space, 0, 1, 100.0, 180.0, 100.0, blendR, self.ep0, 0, 0, self.dp0)
        if(ret == 0):
            print("MoveL is right")
        else:
            print("MoveL is error")

    def NewSpiral(self, joint, space, pa):# 螺旋线运动
        ret = self.robot.NewSpiral(joint, space, 0, 1, 100.0, 100.0, self.ep0, 100.0, 2, self.dp0, pa)
        if (ret == 0):
            print("NewSpiral is right")
        else:
            print("NewSpiral is error")

    def MoveC(self, joint, space, joint1, space1):#笛卡尔空间圆弧运动
        ret = self.robot.MoveC(joint, space, self.pa2, self.ep0, 0, self.dp0, joint1, space1, self.pa2, self.ep0, 0, self.dp0, 100.0, -1.0)
        if (ret == 0):
            print("MoveC is right")
        else:
            print("MoveC is error")

    def MoveJ(self, joint, space):# 关节空间运动 PTP
        ret = self.robot.MoveJ(joint, space, 0, 1, 100.0, 180.0, 100.0,
                         self.ep0, 500.0, 0, self.dp0)
        if (ret == 0):
            print("MoveJ is right")
        else:
            print("MoveJ is error")

    def FT_Control(self):#恒力控制
        """"
        函数：FT_Control
        功能：恒力控制
        参数：status,sensor_num,is_select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang
        返回值：成功：[0]，失败：[errcode]
        """
        self.robot.FT_Control(self.status, cfg.sensor_num, cfg.selection, cfg.force_torque,
                              cfg.gain, cfg.adj_sign, cfg.ilc_sign, cfg.max_dis, cfg.max_ang)  # 恒力控制

    def FT_FindSurface(self):# 表面定位
        """"
        函数：FT_FindSurface
        功能：表面定位
        参数：rcs,direction,axis,lin_v,lin_a,disMax,force_goal
        返回值：成功：[0]，失败：[errcode]
        """
        self.robot.FT_FindSurface(cfg.rcs, cfg.direction, cfg.axis,
                                  cfg.lin_v, cfg.lin_a, cfg.disMax, cfg.force_goal)

    def FT_Guard(self):# 开启碰撞守护
        self.robot.FT_Guard(cfg.actFlag, cfg.sensor_num, cfg.is_select, cfg.force_guard, cfg.max_threshold,
                       cfg.min_threshold)

class Robot(QObject):
    fineTuneClicked = Signal(bool)

    def __init__(self, address) -> None:
        super().__init__()
        # robot init
        self.robot = frrpc.RPC(address)
        self.joint = [[] for _ in range(4)]  # 关节坐标
        self.space = [[] for _ in range(4)]  # 空间笛卡尔坐标

        self.robotApi = RobotApi(address)

        self.nameTPB = str()
        self.speed = 4  # default speed
        self.mode = int()  # robot runtime mode
        self.dir = int()

        self.is_hips = False
        self.pausePosition = -1

    def initRobot(self):
        self.robotApi.FT_Guard()
        self.setBodyPoint(0)
        self.robotApi.SetSpeed(10)

    def getJoint(self):
        return self.joint

    def getSpace(self):
        return self.space

    def getTPBName(self):
        return self.nameTPB

    def setIsHips(self, flag):
        self.is_hips = flag

    def getIsHips(self):
        return self.is_hips

    def setSpeed(self, speed):
        self.speed = speed

    def setMode(self, mode):
        self.mode = mode

    def getMode(self):
        return self.mode

    def setDirection(self, direction):
        print("Origin: self.dir = ", self.dir)
        self.dir = direction

    def getDirection(self):
        print("Current: self.dir = ", self.dir)
        return self.dir

    def savePoint(self, pointIndex):
        """"
        函数：save_point
        功能：存点
        参数：无
        返回值：无
        """
        currentJoint = self.robotApi.GetActualJointPosDegree(1)
        self.joint[pointIndex - 1] = [currentJoint[j+1] for j in range(6)]
        change2Space = self.robotApi.GetForwardKin(self.joint[pointIndex - 1])
        self.space[pointIndex - 1] = [change2Space[j+1] for j in range(6)]

    def fineTune(self, direction):
        pstate = self.robotApi.GetProgramState()
        if pstate[1] == 1:  # robot is stopped or without program
            if direction == 'front':  # 向右微调
                self.robotApi.StartJOG(8, 2, 0, 5.0)
            elif direction == 'back':  # 向左微调
                self.robotApi.StartJOG(8, 2, 1, 5.0)
            elif direction == 'right':  # 向后微调
                self.robotApi.StartJOG(8, 1, 0, 5.0)
            elif direction == 'left':  # 向前微调
                self.robotApi.StartJOG(8, 1, 1, 5.0)
            elif direction == 'up':  # 向上微调
                self.robotApi.StartJOG(2, 3, 1, 5.0)
            elif direction == 'down':  # 向下微调
                self.robotApi.StartJOG(2, 3, 0, 5.0)
            elif direction == 'leftrot':  # 末端向左微调
                self.robotApi.StartJOG(2, 6, 1, 5.0)
            elif direction == 'rightrot':  # 末端向右微调
                self.robotApi.StartJOG(2, 6, 0, 5.0)
            else:
                print("ERROR::direction is wrong, direction=%s" % direction)
                return
            self.fineTuneClicked.emit(True)
        else:
            print("ERROR::the robot is running, not allow to adjust it, pstate[1]={}".format(
                pstate[1]))

    # 到达部位点位函数, 0:'origin', 1:'jinbu', 2:'beibu', 3:'tuibu, 4:'others'
    def setBodyPoint(self, body):
        self.robotApi.ProgramStop()
        self.robotApi.SetSpeed(10)
        j0 = list()
        p0 = list()
        if body == 1:  # 颈部点位
            j0 = [-94.5570418858292, -103.457708075495, -80.73711130878714, -86.08930228960396, 91.01639851485149,
                  -32.8038704749381]#改2023/11/15陈：修改点位
            p0 = [-147.1316528320312, -584.511962890625, 375.948028564453, -179.6881561279297, 1.00823664665222,
                  -151.752944946289]#改2023/11/15陈：修改点位

        elif body == 2:  # 背部点位
            j0 = [-94.5570418858292, -103.457708075495, -80.73711130878714, -86.08930228960396, 91.01639851485149,
                  -32.8038704749381]#改2023/11/15陈：修改点位
            p0 = [-147.1316528320312, -584.511962890625, 375.948028564453, -179.6881561279297, 1.00823664665222,
                  -151.752944946289]#改2023/11/15陈：修改点位

        elif body == 3:  # 腿部点位
            j0 = [-94.5570418858292, -103.457708075495, -80.73711130878714, -86.08930228960396, 91.01639851485149, -32.8038704749381]#改2023/11/15陈：修改点位
            p0 = [-147.1316528320312, -584.511962890625, 375.948028564453, -179.6881561279297, 1.00823664665222, -151.752944946289]#改2023/11/15陈：修改点位

        elif body == 0:  # 原点点位
            j0 = [-93.5893748066213, -36.43588528774752, -137.0917533647896, -96.8413279316213, 90.95178585241337, -32.80300027073019]#改2023/11/15陈：修改点位
            p0 = [-109.65274810791, -145.3348236083984, 288.3022155761718, -179.7944946289062, 0.9998968839645386, -150.787643432617]#改2023/11/15陈：修改点位
        else:
            pass

        if j0 and p0:
            self.robotApi.MoveJ(j0, p0)

    def recordTrack(self, isStart):
        if isStart:
            self.nameTPB = time.strftime('%Y-%m-%d %H:%M:%S',
                                         time.localtime(time.time()))
            type = 1  # 数据类型，1-关节位置
            period = 2  # 采样周期，2ms 或 4ms 或 8ms
            di_choose = 0  # di 输入配置
            do_choose = 0  # do 输出配置
            self.robotApi.SetTPDParam(
                type, self.nameTPB, period, di_choose, do_choose)  # 配置 TPD 参数
            self.robotApi.drag(1)
            self.robotApi.SetTPDStart(
                type, self.nameTPB, period, di_choose, do_choose)  # 开始记录示教轨迹
        else:
            self.robotApi.SetWebTPDStop()  # 停止记录示教轨迹
            self.robotApi.drag(0)

    # def pointLift(self, num):
    #     ret = self.robot.GetActualTCPPose(0)  # 获取机器人当前工具位姿
    #     p0 = [ret[1], ret[2], ret[3], ret[4], ret[5], ret[6]]
    #     if (num == 0):  # 暂停点位抬起
    #         p1 = [p0[0], p0[1], p0[2] + 100, p0[3], p0[4], p0[5]]
    #         self.robot.MoveCart(p1, 0, 1, 100.0, 180.0,
    #                             100.0, 500.0, -1)  # 笛卡尔空间点到点运动
    #     if (num == -2):
    #         if self.mode == 1:  # 模式二时两个点位抬起
    #             p1 = [p0[0], p0[1], p0[2] + 50, p0[3], p0[4], p0[5]]
    #             self.robot.MoveCart(p1, 0, 1, 100.0, 180.0,
    #                                 100.0, 500.0, -1)  # 笛卡尔空间点到点运动
    #             p2 = [self.space[2][0], self.space[2][1], self.space[2][2] + 50, self.space[2][3],
    #                   self.space[2][4], self.space[2][5]]
    #             self.robot.MoveCart(p2, 0, 1, 100.0, 180.0,
    #                                 100.0, 500.0, -1)  # 笛卡尔空间点到点运动
    #         elif self.mode == 2:  # 模式四时两个点位抬起
    #             p1 = [p0[0], p0[1], p0[2] + 50, p0[3], p0[4], p0[5]]
    #             self.robot.MoveCart(p1, 0, 1, 100.0, 180.0,
    #                                 100.0, 500.0, -1)  # 笛卡尔空间点到点运动
    #             p2 = [self.space[3][0], self.space[3][1], self.space[3][2] + 50, self.space[3][3],
    #                   self.space[3][4], self.space[3][5]]
    #             self.robot.MoveCart(p2, 0, 1, 100.0, 180.0,
    #                                 100.0, 500.0, -1)  # 笛卡尔空间点到点运动
    #     elif (num == -1):  # 暂停点位落下
    #         p1 = [p0[0], p0[1], p0[2] - 75, p0[3], p0[4], p0[5]]
    #         self.robot.MoveCart(p1, 0, 1, 100.0, 180.0,
    #                             100.0, 500.0, -1)  # 笛卡尔空间点到点运动
    #     elif (num == 2):  # 两个点位直线模式时抬起
    #         p1 = [p0[0], p0[1], p0[2] + 50, p0[3], p0[4], p0[5]]
    #         self.robot.MoveCart(p1, 0, 1, 100.0, 180.0,
    #                             100.0, 500.0, -1)  # 笛卡尔空间点到点运动
    #         ret = [self.space[0][0], self.space[0][1], self.space[0][2] +
    #                50, self.space[0][3], self.space[0][4], self.space[0][5]]
    #         self.robot.MoveCart(ret, 0, 1, 100.0, 180.0,
    #                             100.0, 500.0, -1)  # 笛卡尔空间点到点运动
    #         ret1 = [self.space[0][0], self.space[0][1], self.space[0][2] +
    #                10, self.space[0][3], self.space[0][4], self.space[0][5]]
    #         self.robot.MoveCart(ret1, 0, 1, 100.0, 180.0,
    #                             100.0, 500.0, -1)  # 笛卡尔空间点到点运动
    #         # 改2023/11/15陈：添加ret1已到达皮肤表面1cm处

class RobotThread(QThread):
    stopTimerSignal = Signal()
    startTimerSignal = Signal()
    endSignal = Signal()

    def __init__(self, address) -> None:
        super().__init__()
        self.robotCtrlThread = Robot(address)
        self.joint = [[] for _ in range(4)]  # 关节坐标
        self.space = [[] for _ in range(4)]  # 空间笛卡尔坐标
        self.robotApi = RobotApi(address)

        self.nameTPB = str()
        self.mode = 0
        self.dir = 0
        self.is_hips = False
        self.is_paused = False

        self.is_one_third = False
        self.is_half = False

        self.is_running = True
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def setTPBName(self, name):
        self.nameTPB = name

    def setMode(self, mode):
        self.mode = mode

    def setDirection(self, direction):
        self.dir = direction

    def setBodyPart(self, flag):
        self.is_hips = flag

    def setOneThird(self, flag):
        self.is_one_third = flag
        print("Setting::is_one_third: {}".format(self.is_one_third))

    def setOneHalf(self, flag):
        self.is_half = flag
        print("Setting::is_half: {}".format(self.is_half))

    def setJoint(self, jointList):
        if cfg.istest:
            self.joint = copy.copy(cfg.j0)
        else:
            self.joint = copy.copy(jointList)

    def setSpace(self, spaceList):
        if cfg.istest:
            self.space = copy.copy(cfg.p0)
        else:
            self.space = copy.copy(spaceList)

    def pointLift(self, num):
        global variable
        print("Begin lift robot...")
        ret = self.robotApi.GetActualTCPPose(0)
        p0 = ret[1:]
        if num == 0:
            if self.is_paused or not self.is_running:
                print("reach PointLift num==0 variable = 100")
                variable = 100
            else:
                print("reach PointLift num==0 variable = -90")
                variable = -90
            p0[2] += variable
            print(p0[2])
            self.robotApi.MoveCart(p0)

        elif num == 2:  # 两个点位直线模式时抬起
            if self.is_one_third:  # 模式二时两个点位抬起
                variable = 2
            elif self.is_half:
                variable = 3
            else:
                variable = 0
            p0[2] += 50
            self.robotApi.MoveCart(p0)
            self.space[variable][2] += 50
            self.robotApi.MoveCart(self.space[variable])
            self.space[variable][2] -= 40
            self.robotApi.MoveCart(self.space[variable])
            self.space[variable][2] -= 10

    def circle_shifting(self):
        self.robotApi.StartJOG(2, 1, 1, 15.0)
        time.sleep(1)
        j0 = self.robotApi.GetActualJointPosDegree(1)  # 获取当前关节位置(角度)
        j1 = j0[1:]
        p0 = self.robotApi.GetForwardKin(j1)
        p1 = p0[1:]
        self.robotApi.ImmStopJOG()
        return j1, p1

    def stop_thread(self, isTimeOver):
        print("Robot begins to stop...Is time over = {}".format(isTimeOver))

        if self.is_running:
            self.is_running = False
            if not isTimeOver:
                self.endSignal.emit()
                print("time:{}, Send end signal...".format(
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
            print("Set robot flag FALSE")
            self.quit()
            self.wait()

    def pause_thread(self):
        if not self.is_running or self.is_paused:
            print("Robot can not change state to pause. self.is_running={}, self.is_paused={}".format(
                self.is_running, self.is_paused))
            return

        print("time:{}, Robot will be paused".format(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        with QMutexLocker(self.mutex):  # key point
            # locker.mutex().unlock()
            print("reach pause_thread QMutexLocker")
            self.is_paused = True
            self.stopTimerSignal.emit()
            print("time:{}, Send stop timer signal...".format(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
            if self.mode == 1 or self.mode == 2 or self.mode == 3:
                print("reach pause_thread self.pointLift(0)")
                self.pointLift(0)
            else:
                self.robotApi.ProgramPause()  # 暂停正在执行的机器人程序
            print("Robot is paused finished")
        print("reach pause_thread over")

    def resume_thread(self):
        if not self.is_paused or not self.is_running:
            print("pause state is {}".format(self.is_paused))
            return

        print("time:{}, Robot will be resumed".format(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        with QMutexLocker(self.mutex):
            self.is_paused = False

            if self.mode == 1 or self.mode == 2 or self.mode == 3:
                pa = [[500.0, 0.0, 20.0, 20.0, 0.0, 0.0], [500.0, 0.0, 20.0, 20.0, 0.0, 1.0]]
                print("self.mode = ", self.mode)
                if self.mode != 2 or self.is_half:
                    self.pointLift(0)
                    self.robotApi.FT_FindSurface()  # 表面定位
                    self.robotApi.FT_Control()  # 恒力控制
                if self.mode == 1:
                    if self.is_one_third:
                        self.robotApi.MoveCart(self.space[2])
                        target = self.circle_shifting()
                        self.robotApi.NewSpiral(target[0], target[1], pa[0])

                elif self.mode == 2:
                    print("is_one_third: {}, is_half: {}".format(self.is_one_third, self.is_half))
                    if not self.is_one_third and not self.is_half:
                        print("Resume MoveC finished")
                        print("self.pausePosition = ", self.pausePosition)
                        if self.pausePosition == 0:
                            index = 2
                        else:
                            index = 0
                        self.space[index][2] += 100
                        self.robotApi.MoveCart(self.space[index])
                        self.space[index][2] -= 90
                        self.robotApi.MoveCart(self.space[index])
                        self.space[index][2] -= 10
                        self.robotApi.FT_FindSurface()  # 表面定位
                        self.robotApi.FT_Control()  # 恒力控制

                    else:
                        self.robotApi.MoveCart(self.space[3])
                        self.robotApi.SetSpeed(10)
                        target = self.circle_shifting()
                        self.robotApi.NewSpiral(target[0], target[1], pa[0])
                        print("Resume NewSpiral finished")
                elif self.mode == 3:
                    print("reach resume_thread self.mode == 3")
                    self.robotApi.SetSpeed(10)
                    if self.robotCtrlThread.dir == 0:
                        target = self.circle_shifting()
                        self.robotApi.NewSpiral(target[0], target[1], pa[0])
                    else:
                        target = self.circle_shifting()
                        self.robotApi.NewSpiral(target[0], target[1], pa[1])
            else:
                self.robotApi.ProgramResume()  # 恢复暂停执行的机器人程序

            self.startTimerSignal.emit()
            self.cond.wakeOne()
            print("Robot is resumed finished")

    def run(self):
        pa = [[500.0, 0.0, 20.0, 0.0, 0.0, 1.0], [500.0, 0.0, 20.0, 0.0, 0.0, 0.0]]
        print("Mode is {}".format(self.mode))
        if self.mode == 1:  # 直线模式和画圈模式
            self.stopTimerSignal.emit()
            self.pointLift(2)  # 两点直线抬起
            self.robotApi.FT_FindSurface()  # 表面定位
            self.robotApi.FT_Control()  # 恒力控制
            self.robotApi.MoveL(self.joint[1], self.space[1], 500.0)
            self.startTimerSignal.emit()
            while not self.is_one_third and not self.is_half:  # 两点直线---half for tunbu
                if not self.is_running:
                    print("robot is not running......")
                    break

                if not self.is_hips:
                    for pos in range(2):
                        # quit immediately
                        if not self.is_running:
                            print("robot is not running......")
                            break
                        with QMutexLocker(self.mutex):
                            while self.is_paused:
                                self.pausePosition = pos
                                print("1.Current position is {}".format(
                                    self.pausePosition))
                                self.cond.wait(self.mutex)
                                break
                            if not self.is_one_third:
                                self.robotApi.MoveL(self.joint[pos], self.space[pos], -1.0)
                        self.msleep(100)  # 缓减长时间无法获取锁而导致的该线程无法及时暂停的问题
                else:
                    for pos in range(4):
                        if not self.is_running:
                            print("robot is not running......")
                            break
                        with QMutexLocker(self.mutex):
                            while self.is_paused:
                                if pos < 2:
                                    self.pausePosition = pos+1
                                elif pos == 2:
                                    self.pausePosition = 1
                                else:
                                    self.pausePosition = 0
                                print("2.Current pos is {}, position is {}".format(
                                    pos, self.pausePosition))
                                self.cond.wait(self.mutex)
                                break
                            if self.is_running:
                                if pos < 2:
                                    self.robotApi.MoveL(self.joint[pos+1], self.space[pos+1], 500.0)
                                elif pos == 2:
                                    self.robotApi.MoveL(self.joint[1], self.space[1], 500.0)
                                else:
                                    self.robotApi.MoveL(self.joint[0], self.space[0], 500.0)
                        self.msleep(100)  # 解决长时间无法获取锁而导致的线程无法暂停的问题

            if self.is_running:
                self.stopTimerSignal.emit()
                self.pointLift(2)
                self.robotApi.FT_FindSurface()  # 表面定位
                self.startTimerSignal.emit()
                self.robotApi.SetSpeed(10)
                self.robotApi.FT_Control()  # 恒力控制
                target = self.circle_shifting()
                self.robotApi.NewSpiral(target[0], target[1], pa[0])
                while self.is_running:
                    while self.is_paused:
                        self.cond.wait(self.mutex)
                        break

        elif self.mode == 2:  # 圆弧和画圈模式
            self.stopTimerSignal.emit()
            self.pointLift(2)
            self.robotApi.FT_FindSurface()  # 表面定位
            self.robotApi.FT_Control()  # 恒力控制
            self.startTimerSignal.emit()
            while not self.is_one_third and not self.is_half:
                if not self.is_running or self.is_half:
                    print("robot is not running......")
                    break
                for pos in range(2):
                    if not self.is_running or self.is_half:
                        print("robot is not running......")
                        break
                    index = 2
                    if pos != 0:
                        index = 0
                    with QMutexLocker(self.mutex):
                        while self.is_paused:
                            self.pausePosition = pos
                            print("3.Current position is {}".format(index))
                            self.cond.wait(self.mutex)
                            break
                        self.robotApi.MoveC(self.joint[1], self.space[1], self.joint[index], self.space[index])
                    self.msleep(100)  # 缓减长时间无法获取锁而导致的该线程无法及时暂停的问题
            if self.is_running:
                self.stopTimerSignal.emit()
                self.pointLift(2)
                self.robotApi.FT_FindSurface()  # 表面定位
                self.robotApi.SetSpeed(10)
                self.robotApi.FT_Control()  # 恒力控制
                self.startTimerSignal.emit()
                print("In NewSpiral...")
                target = self.circle_shifting()
                self.robotApi.NewSpiral(target[0], target[1], pa[0])
                while self.is_running:
                    with QMutexLocker(self.mutex):
                        while self.is_paused:
                            print("NewSpiral Paused")
                            self.cond.wait(self.mutex)
                            break
                    self.msleep(100)  # 解决长时间无法获取锁而导致的线程无法暂停的问题
                print("Out of running...")

        elif self.mode == 3:
            if self.is_running:
                self.stopTimerSignal.emit()
                self.robotApi.ProgramStop()
                self.pointLift(2)
                self.robotApi.FT_FindSurface()  # 表面定位
                self.robotApi.SetSpeed(10)
                self.robotApi.FT_Control()  # 恒力控制
                self.startTimerSignal.emit()
                print("In NewSpiral...")
                target = self.circle_shifting()
                if self.dir == 0:
                    self.robotApi.NewSpiral(target[0], target[1], pa[0])
                else:
                    self.robotApi.NewSpiral(target[0], target[1], pa[1])
                while self.is_running:
                    with QMutexLocker(self.mutex):
                        while self.is_paused:
                            print("NewSpiral Paused")
                            self.cond.wait(self.mutex)
                            break
                    self.msleep(100)  # 解决长时间无法获取锁而导致的线程无法暂停的问题
            print("Out of running...")

        elif self.mode == 4:
            blend = 1  # 是否平滑，1-平滑，0-不平滑
            ovl = 200.0  # 速度缩放
            self.robotApi.SetSpeed(8)
            while self.is_running:
                ret = self.robotApi.GetRobotMotionDone()  # 查询机器人运动完成状态
                time.sleep(0.5)
                with QMutexLocker(self.mutex):
                    while self.is_paused:
                        self.cond.wait(self.mutex)
                        break
                    if ret[1] == 1:
                        self.robotApi.LoadTPD(
                            self.nameTPB)  # 轨迹预加载
                        self.robotApi.MoveJ(self.joint[0], self.space[0])
                        self.robotApi.MoveTPD(
                            self.nameTPB, blend, ovl)  # 轨迹复现
                        ret = [0, 0]

        # elif self.mode == 5:
        #     a = g.text
        #     self.robotCtrlThread.robot.Mode(0)  # 机器人切入自动运行模式
        #     self.robotCtrlThread.robot.ProgramLoad('/fruser/%s.lua' % a)  # 加载要执行的机器人程序，testPTP.lua程序需要先在 webapp 上编写好
        #     self.robotCtrlThread.robot.ProgramRun()  # 执行机器人程序

        else:
            return

        self.pointLift(0)
        time.sleep(1.2)
        self.robotCtrlThread.setBodyPoint(0)
        print("Robot is end of running")


class ForceControl(QThread):  # 力控实时获取数据线程
    """"
    函数：Force_Control
    功能：力控检测
    参数：无
    返回值：无
    """
    stopped = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.FT_trigger = False

    def setTrigger(self, flag):
        self.FT_trigger = flag

    def getTrigger(self):
        return self.FT_trigger

    def run(self):
        while True:
            # 获取 8083 反馈数据 demo
            Con_SOCKET = socket.socket()
            Con_SOCKET.connect(('192.168.58.2', 8083))
            RV = Con_SOCKET.recv(1024)
            RVV = []
            for i in range(len(RV)):
                RVV.append(hex(RV[i]))
            # 获取力传感器反馈数值
            # FT_name3 = ["FT-X", "FT-Y", "FT-Z", "FT-RX", "FT-RY", "FT-RZ"]#获取6个方向的力
            # print(FT_name3[2] + ": " + str(struct.unpack("d", RV[2 * 8 + 184:3 * 8 + 184])))
            ret = str(struct.unpack("d", RV[2 * 8 + 184:3 * 8 + 184]))
            ret = ret.strip("(),")
            if float(ret) < -15:  # 力超过15牛则停止机器人回到原点
                self.setTrigger(True)
                self.stopped.emit()
            time.sleep(0.5)
