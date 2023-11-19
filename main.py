import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QTimer, QEventLoop
from ui.window import Ui_MainWindow
from modules.textparser import parser
from time import sleep, time

def delay(msec):
    loop = QEventLoop()
    QTimer().singleShot(msec, lambda: loop.quit())
    loop.exec()
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.OpenFile.clicked.connect(self.OpenFile)
        self.ui.Start.clicked.connect(self.Start)
        self.ui.Stop.clicked.connect(self.Stop)
        self.stoptrigger = 1
        self.ui.Level1.clicked.connect(self.level_1)
        self.ui.Level2.clicked.connect(self.level_2)
        self.ui.Level3.clicked.connect(self.level_3)

    def OpenFile(self):
        filename = QFileDialog().getOpenFileName()
        self.words = parser(filename[0])
        self.stoptrigger = 0

    def Start(self):
        tstr = float(self.ui.spinBox.value())*1000
        twrd = float(self.ui.SpinBox_2.value())*1000
        for line in self.words:
            if self.stoptrigger == 1:
                break
            delay(tstr)
            for word in line:
               delay(twrd)
               self.ui.label.setText(str(word))
               print(word)

    def Stop(self):
        exit()

    def level_1(self):
        self.ui.spinBox.setValue(0.5)
        self.ui.SpinBox_2.setValue(1)

    def level_2(self):
        self.ui.spinBox.setValue(0.4)
        self.ui.SpinBox_2.setValue(0.5)

    def level_3(self):
        self.ui.spinBox.setValue(0.1)
        self.ui.SpinBox_2.setValue(0.2)



if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())