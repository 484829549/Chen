from PySide6.QtCore import (QThread, QWaitCondition,
                            QMutex, Signal, QMutexLocker)


class TimeThread(QThread):
    valueChanged = Signal(str)
    # 0-start, 1-runing, 2-two min left, 3-finished, 4-pause, 5-recover, 6-half time, 7- 1/3 time, 8- stop
    statusSignal = Signal(int)
    socket = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.is_paused = False
        self.is_running = True
        self.timeSet = int()
        self.currentTotalSec = int()
        self.minStr = str()
        self.secStr = str()
        self.timeValueStr = str()
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def setTime(self, minute):
        self.timeSet = minute * 60
        self.currentTotalSec = minute * 60 + 1  # "+ 1" to be used for counting

    def __timeCount(self):
        self.currentTotalSec -= 1
        self.minStr, self.secStr = "%02d" % (
            self.currentTotalSec/60), "%02d" % (self.currentTotalSec % 60)
        self.timeValueStr = "{}:{}".format(self.minStr, self.secStr)

    def pause_thread(self):
        with QMutexLocker(self.mutex):
            self.statusSignal.emit(4)
            self.is_paused = True
            print("Timer need to be paused")

    def resume_thread(self):
        if not self.is_paused:
            return

        with QMutexLocker(self.mutex):
            self.statusSignal.emit(5)
            self.is_paused = False
            self.cond.wakeOne()
            print("Timer is resumed")

    def stop_thread(self):
        print("Timer received stop signal")
        self.statusSignal.emit(8)
        self.is_running = False
        self.quit()
        self.wait()

    def run(self):
        while self.is_running:
            with QMutexLocker(self.mutex):
                while self.is_paused:
                    self.cond.wait(self.mutex)
                    break  # If resume, must break this while loop
                self.__timeCount()
                # print("Thread sends time string is {}".format(self.timeValueStr))
                self.valueChanged.emit(self.timeValueStr)
                self.socket.emit()

                if self.currentTotalSec == 0:
                    self.statusSignal.emit(3)  # send finish signal
                    break
                elif self.currentTotalSec == self.timeSet:
                    self.statusSignal.emit(0)  # send start signal
                # just for camera 1
                elif self.currentTotalSec == (self.timeSet) / 2:
                    self.statusSignal.emit(6)
                    if self.currentTotalSec == 120:
                        self.statusSignal.emit(2)  # send 2 min left signal
                # just for camera 1
                elif self.currentTotalSec == (self.timeSet) / 3:
                    self.statusSignal.emit(7)
                    if self.currentTotalSec == 120:
                        self.statusSignal.emit(2)  # send 2 min left signal
                elif self.currentTotalSec == 120:
                    self.statusSignal.emit(2)  # send 2 min left signal
                else:
                    self.statusSignal.emit(1)  # send running signal

            self.sleep(1)
        print("Timer bye bye...")
