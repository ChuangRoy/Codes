from download  import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.download_button.clicked.connect(self.buttonClicked)
    def buttonClicked(self):
        url = self.ui.url.text()
        print("download %s"%url)
        self.ui.url.clear()
        self.download()
    def download(self):
        try:
            yt = YouTube(url)
            title = yt.title
        except:
            print("please check internet 請檢察網路連線" )
        else:
            try:
                print("%s.........Downloading 努力下載中，請稍候" % yt.title)
                video = yt.streams.filter(file_extension='mp4',
                                          res='%s' % cbb.get()).first()
                video.download()
            except:
                print('%s...please check quality 請檢察是否支援此畫質'%yt.title)
            else:
                print("%s.........Done下載完畢" %yt.title)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
