# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(683, 699)
        MainWindow.setMinimumSize(QtCore.QSize(683, 699))
        MainWindow.setMaximumSize(QtCore.QSize(683, 699))
        MainWindow.setMouseTracking(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 661, 501))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 0, 231, 31))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 50, 41, 38))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(39, 39))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 70, 51, 21))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(240, 50, 351, 21))
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_10 = QtGui.QPushButton(self.tab)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 70, 61, 21))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(260, 430, 161, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.pushButton.setIconSize(QtCore.QSize(165, 100))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_25 = QtGui.QPushButton(self.tab)
        self.pushButton_25.setGeometry(QtCore.QRect(510, 10, 121, 21))
        self.pushButton_25.setAutoFillBackground(False)
        self.pushButton_25.setShortcut(_fromUtf8(""))
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.pushButton_26 = QtGui.QPushButton(self.tab)
        self.pushButton_26.setGeometry(QtCore.QRect(510, 10, 121, 21))
        self.pushButton_26.setAutoFillBackground(False)
        self.pushButton_26.setShortcut(_fromUtf8(""))
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.checkBox_3 = QtGui.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 340, 111, 21))
        self.checkBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_3.setCheckable(True)
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setAutoExclusive(True)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 340, 51, 21))
        self.lineEdit_2.setStyleSheet(_fromUtf8("font: 75 12pt \"DejaVu Sans Mono\";"))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.checkBox_4 = QtGui.QCheckBox(self.tab)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 370, 71, 21))
        self.checkBox_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_4.setAutoExclusive(True)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.label_62 = QtGui.QLabel(self.tab)
        self.label_62.setGeometry(QtCore.QRect(100, 370, 41, 21))
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 370, 51, 21))
        self.lineEdit_4.setStyleSheet(_fromUtf8("font: 75 12pt \"DejaVu Sans Mono\";"))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.line_4 = QtGui.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(200, 370, 20, 20))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_63 = QtGui.QLabel(self.tab)
        self.label_63.setGeometry(QtCore.QRect(220, 370, 41, 21))
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.pushButton_9 = QtGui.QPushButton(self.tab)
        self.pushButton_9.setGeometry(QtCore.QRect(260, 330, 161, 21))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.pushButton_9.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setAutoExclusive(False)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 370, 51, 21))
        self.lineEdit_5.setStyleSheet(_fromUtf8("font: 75 12pt \"DejaVu Sans Mono\";"))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setDragEnabled(False)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.pushButton_5 = QtGui.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 330, 81, 21))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("img/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setAutoExclusive(False)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_39 = QtGui.QLabel(self.tab)
        self.label_39.setGeometry(QtCore.QRect(490, 350, 151, 20))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(20, 400, 141, 21))
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setAutoExclusive(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_6 = QtGui.QCheckBox(self.tab)
        self.checkBox_6.setGeometry(QtCore.QRect(220, 400, 381, 21))
        self.checkBox_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_6.setAutoExclusive(True)
        self.checkBox_6.setTristate(False)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.line_5 = QtGui.QFrame(self.tab)
        self.line_5.setGeometry(QtCore.QRect(200, 400, 20, 20))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_37 = QtGui.QLabel(self.tab)
        self.label_37.setGeometry(QtCore.QRect(250, 200, 381, 16))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.label_38 = QtGui.QLabel(self.tab)
        self.label_38.setGeometry(QtCore.QRect(250, 220, 381, 16))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_33 = QtGui.QLabel(self.tab)
        self.label_33.setGeometry(QtCore.QRect(250, 240, 381, 16))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_36 = QtGui.QLabel(self.tab)
        self.label_36.setGeometry(QtCore.QRect(250, 260, 381, 16))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.label_34 = QtGui.QLabel(self.tab)
        self.label_34.setGeometry(QtCore.QRect(250, 280, 381, 16))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(self.tab)
        self.label_35.setGeometry(QtCore.QRect(250, 300, 381, 16))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(240, 100, 401, 91))
        self.textBrowser.setStyleSheet(_fromUtf8(""))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_ruta = QtGui.QLabel(self.tab)
        self.label_ruta.setGeometry(QtCore.QRect(360, 370, 281, 20))
        self.label_ruta.setScaledContents(False)
        self.label_ruta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ruta.setObjectName(_fromUtf8("label_ruta"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 221, 281))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("img/posterTMP.jpg")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(260, 0, 191, 41))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("img/animeyt.png")))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_26.raise_()
        self.label.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.lineEdit.raise_()
        self.pushButton_10.raise_()
        self.pushButton.raise_()
        self.pushButton_25.raise_()
        self.checkBox_3.raise_()
        self.lineEdit_2.raise_()
        self.checkBox_4.raise_()
        self.label_62.raise_()
        self.lineEdit_4.raise_()
        self.line_4.raise_()
        self.label_63.raise_()
        self.pushButton_9.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_5.raise_()
        self.label_39.raise_()
        self.checkBox.raise_()
        self.checkBox_6.raise_()
        self.line_5.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.label_33.raise_()
        self.label_36.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.textBrowser.raise_()
        self.label_ruta.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_3)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 80, 641, 381))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 637, 377))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.graphicsView_2 = QtGui.QGraphicsView(self.tab_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 151, 61))
        self.graphicsView_2.setStyleSheet(_fromUtf8("border-image: url(img/animeyt.png);"))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(160, 10, 58, 14))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 20, 341, 31))
        self.lineEdit_3.setStyleSheet(_fromUtf8(""))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEdit_3.setDragEnabled(False)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 50, 61, 21))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(230, 50, 51, 21))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_11 = QtGui.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(360, 50, 131, 31))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_14 = QtGui.QPushButton(self.tab_3)
        self.pushButton_14.setGeometry(QtCore.QRect(500, 50, 151, 31))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(510, 20, 71, 31))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 641, 361))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.gridLayoutWidget)
        self.treeWidget.setMaximumSize(QtCore.QSize(700, 400))
        self.treeWidget.setStyleSheet(_fromUtf8("font: 25 11pt \"URW Gothic L\";"))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.renaudar = QtGui.QPushButton(self.tab_2)
        self.renaudar.setEnabled(False)
        self.renaudar.setGeometry(QtCore.QRect(190, 420, 146, 35))
        self.renaudar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.renaudar.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.renaudar.setIconSize(QtCore.QSize(165, 100))
        self.renaudar.setCheckable(False)
        self.renaudar.setObjectName(_fromUtf8("renaudar"))
        self.pausar = QtGui.QPushButton(self.tab_2)
        self.pausar.setEnabled(False)
        self.pausar.setGeometry(QtCore.QRect(190, 420, 146, 35))
        self.pausar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pausar.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.pausar.setIconSize(QtCore.QSize(165, 100))
        self.pausar.setCheckable(False)
        self.pausar.setObjectName(_fromUtf8("pausar"))
        self.cancelar = QtGui.QPushButton(self.tab_2)
        self.cancelar.setEnabled(False)
        self.cancelar.setGeometry(QtCore.QRect(370, 420, 146, 35))
        self.cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelar.setAutoFillBackground(False)
        self.cancelar.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.cancelar.setCheckable(False)
        self.cancelar.setObjectName(_fromUtf8("cancelar"))
        self.cancelar_todo = QtGui.QPushButton(self.tab_2)
        self.cancelar_todo.setEnabled(False)
        self.cancelar_todo.setGeometry(QtCore.QRect(550, 380, 101, 21))
        self.cancelar_todo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelar_todo.setAutoFillBackground(False)
        self.cancelar_todo.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.cancelar_todo.setCheckable(False)
        self.cancelar_todo.setObjectName(_fromUtf8("cancelar_todo"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 380, 161, 81))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("img/index.jpeg")))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.scrollArea = QtGui.QScrollArea(self.tab_6)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 631, 421))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 627, 417))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.graphicsView_4 = QtGui.QGraphicsView(self.tab_6)
        self.graphicsView_4.setGeometry(QtCore.QRect(220, -10, 161, 61))
        self.graphicsView_4.setStyleSheet(_fromUtf8("border-image: url(img/animeyt.png);"))
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.label_4 = QtGui.QLabel(self.tab_6)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 141, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 10, 61, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.PING = QtGui.QGraphicsView(self.centralwidget)
        self.PING.setGeometry(QtCore.QRect(640, 10, 21, 21))
        self.PING.setStyleSheet(_fromUtf8("border-image: url(img/boton_azul.png);"))
        self.PING.setObjectName(_fromUtf8("PING"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(20, 520, 641, 31))
        self.progressBar.setStyleSheet(_fromUtf8("font: 75 13pt \"Bitstream Charter\";"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_47 = QtGui.QLabel(self.centralwidget)
        self.label_47.setGeometry(QtCore.QRect(20, 560, 201, 21))
        self.label_47.setStyleSheet(_fromUtf8(""))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.label_49 = QtGui.QLabel(self.centralwidget)
        self.label_49.setGeometry(QtCore.QRect(230, 560, 221, 20))
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.label_53 = QtGui.QLabel(self.centralwidget)
        self.label_53.setGeometry(QtCore.QRect(470, 560, 191, 21))
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.label_52 = QtGui.QLabel(self.centralwidget)
        self.label_52.setGeometry(QtCore.QRect(20, 580, 431, 20))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.label_51 = QtGui.QLabel(self.centralwidget)
        self.label_51.setGeometry(QtCore.QRect(20, 600, 191, 20))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.checkBox_5 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 630, 261, 21))
        self.checkBox_5.setStyleSheet(_fromUtf8("font: 63 oblique 9pt \"URW Gothic L\";\n"
"text-decoration: underline;"))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.pushButton_13 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(490, 580, 71, 71))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setToolTip(_fromUtf8(""))
        self.pushButton_13.setStatusTip(_fromUtf8(""))
        self.pushButton_13.setAccessibleName(_fromUtf8(""))
        self.pushButton_13.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/open-file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon2)
        self.pushButton_13.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_13.setShortcut(_fromUtf8(""))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_12 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setGeometry(QtCore.QRect(590, 580, 71, 71))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("img/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("img/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 683, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOpciones = QtGui.QMenu(self.menubar)
        self.menuOpciones.setTearOffEnabled(False)
        self.menuOpciones.setSeparatorsCollapsible(True)
        self.menuOpciones.setObjectName(_fromUtf8("menuOpciones"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOpciones.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_3.clear)
        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_3.paste)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.paste)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AppYT", None))
        self.pushButton_4.setText(_translate("MainWindow", "pegar", None))
        self.lineEdit.setText(_translate("MainWindow", "http://www.animeyt.tv/dragon-ball-super", None))
        self.pushButton_10.setText(_translate("MainWindow", "limpiar", None))
        self.pushButton.setText(_translate("MainWindow", "Añadir a Descargas", None))
        self.pushButton_25.setText(_translate("MainWindow", "agregar a Mi Lista", None))
        self.pushButton_26.setText(_translate("MainWindow", "Quitar de Mi Lista", None))
        self.checkBox_3.setText(_translate("MainWindow", "Capitulo N°:", None))
        self.checkBox_4.setText(_translate("MainWindow", "Rango:", None))
        self.label_62.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Inicio:</span></p></body></html>", None))
        self.label_63.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Final</span><span style=\" font-size:8pt; font-weight:400;\">:</span></p></body></html>", None))
        self.pushButton_9.setText(_translate("MainWindow", "Ver Lista de capitulos", None))
        self.pushButton_5.setText(_translate("MainWindow", "guardar en:", None))
        self.label_39.setText(_translate("MainWindow", "carpeta predeterminada", None))
        self.checkBox.setText(_translate("MainWindow", "Todos los capitulos", None))
        self.checkBox_6.setText(_translate("MainWindow", "Actualizar Carpeta:", None))
        self.label_37.setText(_translate("MainWindow", "Emitido:", None))
        self.label_38.setText(_translate("MainWindow", "Genero:", None))
        self.label_33.setText(_translate("MainWindow", "Estado:", None))
        self.label_36.setText(_translate("MainWindow", "Capitulos actuales:", None))
        self.label_34.setText(_translate("MainWindow", "Siguiente Cap.", None))
        self.label_35.setText(_translate("MainWindow", "Ultimo cap:", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\';\"><br /></span></p></body></html>", None))
        self.label_ruta.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; text-decoration: underline;\">ruta</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "AppYT", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">buscar:</span></p></body></html>", None))
        self.lineEdit_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>anime</p></body></html>", None))
        self.lineEdit_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton_6.setText(_translate("MainWindow", "limpiar", None))
        self.pushButton_8.setText(_translate("MainWindow", "pegar", None))
        self.pushButton_11.setText(_translate("MainWindow", "animes en emision", None))
        self.pushButton_14.setText(_translate("MainWindow", "ultimos cap. agregados", None))
        self.pushButton_7.setText(_translate("MainWindow", "Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Buscar Anime", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Anime", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Tasa", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "%", None))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Descargando", None))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Finaliza", None))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "Transcurrido", None))
        self.renaudar.setText(_translate("MainWindow", "renaudar", None))
        self.pausar.setText(_translate("MainWindow", "pausar", None))
        self.cancelar.setText(_translate("MainWindow", "Cancelar", None))
        self.cancelar_todo.setText(_translate("MainWindow", "Cancelar todo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Proceso de Descarga", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Animes pendientes:</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Mi Lista", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt;\">0 ms</span></p></body></html>", None))
        self.label_47.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Tasa:</span></p></body></html>", None))
        self.label_49.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">MB/Cap:</span></p></body></html>", None))
        self.label_53.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Transcurrido:</span></p></body></html>", None))
        self.label_52.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Cap:</span></p></body></html>", None))
        self.label_51.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Finaliza en:</span></p></body></html>", None))
        self.checkBox_5.setText(_translate("MainWindow", "apagar PC cuando finalizen Descargas", None))
        self.menuOpciones.setTitle(_translate("MainWindow", "preferencias", None))
