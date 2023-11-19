################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(0, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinBox = QDoubleSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)

        self.SpinBox_2 = QDoubleSpinBox(self.centralwidget)
        self.SpinBox_2.setObjectName(u"SpinBox_2")

        self.horizontalLayout.addWidget(self.SpinBox_2)

        self.OpenFile = QPushButton(self.centralwidget)
        self.OpenFile.setObjectName(u"OpenFile")

        self.horizontalLayout.addWidget(self.OpenFile)

        self.Start = QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")

        self.horizontalLayout.addWidget(self.Start)

        self.Stop = QPushButton(self.centralwidget)
        self.Stop.setObjectName(u"Stop")

        self.horizontalLayout.addWidget(self.Stop)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Level1 = QPushButton(self.centralwidget)
        self.Level1.setObjectName(u"Level1")

        self.horizontalLayout_2.addWidget(self.Level1)

        self.Level2 = QPushButton(self.centralwidget)
        self.Level2.setObjectName(u"Level2")

        self.horizontalLayout_2.addWidget(self.Level2)

        self.Level3 = QPushButton(self.centralwidget)
        self.Level3.setObjectName(u"Level3")

        self.horizontalLayout_2.addWidget(self.Level3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.OpenFile.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.Stop.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u0432\u0430\u0448 \u0442\u0435\u043a\u0441\u0442", None))
        self.Level1.setText(QCoreApplication.translate("MainWindow", u"Level 1", None))
        self.Level2.setText(QCoreApplication.translate("MainWindow", u"Level 2", None))
        self.Level3.setText(QCoreApplication.translate("MainWindow", u"Level 3", None))
    # retranslateUi
