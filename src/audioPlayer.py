import os
import sys
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, Slot
from PySide6.QtWidgets import QApplication, QMainWindow


class RobotAudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mediaFile = str()
        self.mediaDir = str()

    def setMediaDir(self, dir_path):
        self.mediaDir = dir_path

    def __state_changed(self, state):
        # print("State is changed to {}".format(state))
        if state == self.player.MediaStatus.LoadedMedia:
            self.player.play()
        elif state == self.player.MediaStatus.EndOfMedia and self.mediaFile != "":
            print("Media ({}) playback finished".format(self.mediaFile))

    def __player_error(self, error, error_string):
        print("Error is occured in the audio player, [", error, "]: ", error_string)

    def setMedia(self, fileName):
        mediaFile = os.path.join(self.mediaDir, fileName)  # refer to the position of the audio file
        self.mediaFile = mediaFile

    def play(self):
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.audioOutput.setVolume(1.0)
        self.player.setSource(QUrl.fromLocalFile(self.mediaFile))
        self.player.errorOccurred.connect(self.__player_error)
        self.player.mediaStatusChanged.connect(self.__state_changed)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    audioPlayer = RobotAudioPlayer()  # test
    audioPlayer.setMediaDir("./res/media")
    audioPlayer.setMedia("welcome.wav")
    audioPlayer.play()
    sys.exit(app.exec())
