# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\DOCUMENTOS\GitHub\evapotrans\evotui\evotgui.ui'
#
# Created: Sat Dec 09 17:56:31 2017
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(728, 563)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/tux.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setEnabled(True)
        self.mdiArea.setGeometry(QtCore.QRect(-10, 0, 910, 541))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mdiArea.setViewMode(QtGui.QMdiArea.TabbedView)
        self.mdiArea.setDocumentMode(False)
        self.mdiArea.setTabShape(QtGui.QTabWidget.Rounded)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.importtab = QtGui.QWidget()
        self.importtab.setObjectName(_fromUtf8("importtab"))
        self.groupBox_2 = QtGui.QGroupBox(self.importtab)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 681, 221))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.bBd = QtGui.QPushButton(self.groupBox_2)
        self.bBd.setEnabled(True)
        self.bBd.setGeometry(QtCore.QRect(120, 147, 121, 23))
        self.bBd.setObjectName(_fromUtf8("bBd"))
        self.chBbd = QtGui.QCheckBox(self.groupBox_2)
        self.chBbd.setEnabled(False)
        self.chBbd.setGeometry(QtCore.QRect(260, 150, 141, 17))
        self.chBbd.setCheckable(True)
        self.chBbd.setObjectName(_fromUtf8("chBbd"))
        self.bRuta_imp = QtGui.QPushButton(self.groupBox_2)
        self.bRuta_imp.setGeometry(QtCore.QRect(370, 70, 28, 24))
        self.bRuta_imp.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/open_folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bRuta_imp.setIcon(icon1)
        self.bRuta_imp.setAutoDefault(False)
        self.bRuta_imp.setDefault(False)
        self.bRuta_imp.setFlat(False)
        self.bRuta_imp.setObjectName(_fromUtf8("bRuta_imp"))
        self.label_37 = QtGui.QLabel(self.groupBox_2)
        self.label_37.setGeometry(QtCore.QRect(10, 72, 101, 21))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.lRuta_impfile = QtGui.QLineEdit(self.groupBox_2)
        self.lRuta_impfile.setGeometry(QtCore.QRect(119, 72, 245, 20))
        self.lRuta_impfile.setObjectName(_fromUtf8("lRuta_impfile"))
        self.label_38 = QtGui.QLabel(self.groupBox_2)
        self.label_38.setGeometry(QtCore.QRect(50, 40, 61, 16))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.cBdop = QtGui.QComboBox(self.groupBox_2)
        self.cBdop.setGeometry(QtCore.QRect(120, 37, 181, 22))
        self.cBdop.setObjectName(_fromUtf8("cBdop"))
        self.cBdop.addItem(_fromUtf8(""))
        self.cBdop.addItem(_fromUtf8(""))
        self.cBdop.addItem(_fromUtf8(""))
        self.cBdop.addItem(_fromUtf8(""))
        self.cBdop.addItem(_fromUtf8(""))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(420, 20, 251, 181))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.lPass = QtGui.QLineEdit(self.groupBox_4)
        self.lPass.setGeometry(QtCore.QRect(107, 150, 121, 20))
        self.lPass.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lPass.setEchoMode(QtGui.QLineEdit.Password)
        self.lPass.setObjectName(_fromUtf8("lPass"))
        self.lPort = QtGui.QLineEdit(self.groupBox_4)
        self.lPort.setGeometry(QtCore.QRect(107, 90, 121, 20))
        self.lPort.setObjectName(_fromUtf8("lPort"))
        self.label_32 = QtGui.QLabel(self.groupBox_4)
        self.label_32.setGeometry(QtCore.QRect(30, 150, 75, 13))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_33 = QtGui.QLabel(self.groupBox_4)
        self.label_33.setGeometry(QtCore.QRect(17, 60, 75, 13))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_30 = QtGui.QLabel(self.groupBox_4)
        self.label_30.setGeometry(QtCore.QRect(46, 30, 41, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.groupBox_4)
        self.label_31.setGeometry(QtCore.QRect(53, 90, 41, 16))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.lUsr = QtGui.QLineEdit(self.groupBox_4)
        self.lUsr.setGeometry(QtCore.QRect(107, 120, 121, 20))
        self.lUsr.setObjectName(_fromUtf8("lUsr"))
        self.lHost = QtGui.QLineEdit(self.groupBox_4)
        self.lHost.setGeometry(QtCore.QRect(107, 30, 121, 20))
        self.lHost.setObjectName(_fromUtf8("lHost"))
        self.lDb = QtGui.QLineEdit(self.groupBox_4)
        self.lDb.setGeometry(QtCore.QRect(107, 60, 121, 20))
        self.lDb.setObjectName(_fromUtf8("lDb"))
        self.label_34 = QtGui.QLabel(self.groupBox_4)
        self.label_34.setGeometry(QtCore.QRect(50, 120, 75, 13))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.bRuta_exp = QtGui.QPushButton(self.groupBox_2)
        self.bRuta_exp.setGeometry(QtCore.QRect(370, 108, 28, 24))
        self.bRuta_exp.setText(_fromUtf8(""))
        self.bRuta_exp.setIcon(icon1)
        self.bRuta_exp.setAutoDefault(False)
        self.bRuta_exp.setDefault(False)
        self.bRuta_exp.setFlat(False)
        self.bRuta_exp.setObjectName(_fromUtf8("bRuta_exp"))
        self.lRuta_foldsalid = QtGui.QLineEdit(self.groupBox_2)
        self.lRuta_foldsalid.setGeometry(QtCore.QRect(119, 110, 245, 20))
        self.lRuta_foldsalid.setObjectName(_fromUtf8("lRuta_foldsalid"))
        self.label_39 = QtGui.QLabel(self.groupBox_2)
        self.label_39.setGeometry(QtCore.QRect(30, 110, 81, 20))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.groupBox_3 = QtGui.QGroupBox(self.importtab)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 250, 681, 241))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.lRuta_var = QtGui.QLineEdit(self.groupBox_3)
        self.lRuta_var.setGeometry(QtCore.QRect(89, 102, 245, 20))
        self.lRuta_var.setObjectName(_fromUtf8("lRuta_var"))
        self.bRuta_var = QtGui.QPushButton(self.groupBox_3)
        self.bRuta_var.setGeometry(QtCore.QRect(340, 100, 28, 24))
        self.bRuta_var.setText(_fromUtf8(""))
        self.bRuta_var.setIcon(icon1)
        self.bRuta_var.setAutoDefault(False)
        self.bRuta_var.setDefault(False)
        self.bRuta_var.setFlat(False)
        self.bRuta_var.setObjectName(_fromUtf8("bRuta_var"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(30, 102, 46, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.cVariable = QtGui.QComboBox(self.groupBox_3)
        self.cVariable.setGeometry(QtCore.QRect(90, 70, 181, 22))
        self.cVariable.setObjectName(_fromUtf8("cVariable"))
        self.label_35 = QtGui.QLabel(self.groupBox_3)
        self.label_35.setGeometry(QtCore.QRect(30, 70, 46, 20))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.groupBox_3)
        self.label_36.setGeometry(QtCore.QRect(20, 43, 61, 16))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.cBvar = QtGui.QComboBox(self.groupBox_3)
        self.cBvar.setGeometry(QtCore.QRect(90, 40, 181, 22))
        self.cBvar.setObjectName(_fromUtf8("cBvar"))
        self.cBvar.addItem(_fromUtf8(""))
        self.cBvar.addItem(_fromUtf8(""))
        self.cBvar.addItem(_fromUtf8(""))
        self.bCvar = QtGui.QPushButton(self.groupBox_3)
        self.bCvar.setEnabled(True)
        self.bCvar.setGeometry(QtCore.QRect(90, 150, 121, 23))
        self.bCvar.setObjectName(_fromUtf8("bCvar"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_5.setGeometry(QtCore.QRect(380, 20, 291, 121))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.cB_hr = QtGui.QCheckBox(self.groupBox_5)
        self.cB_hr.setEnabled(False)
        self.cB_hr.setGeometry(QtCore.QRect(20, 70, 110, 17))
        self.cB_hr.setCheckable(True)
        self.cB_hr.setObjectName(_fromUtf8("cB_hr"))
        self.cB_ve = QtGui.QCheckBox(self.groupBox_5)
        self.cB_ve.setEnabled(False)
        self.cB_ve.setGeometry(QtCore.QRect(140, 70, 117, 17))
        self.cB_ve.setCheckable(True)
        self.cB_ve.setObjectName(_fromUtf8("cB_ve"))
        self.cB_bs = QtGui.QCheckBox(self.groupBox_5)
        self.cB_bs.setEnabled(False)
        self.cB_bs.setGeometry(QtCore.QRect(20, 24, 72, 17))
        self.cB_bs.setCheckable(True)
        self.cB_bs.setObjectName(_fromUtf8("cB_bs"))
        self.cB_tx = QtGui.QCheckBox(self.groupBox_5)
        self.cB_tx.setEnabled(False)
        self.cB_tx.setGeometry(QtCore.QRect(20, 93, 123, 17))
        self.cB_tx.setCheckable(True)
        self.cB_tx.setObjectName(_fromUtf8("cB_tx"))
        self.cB_tm = QtGui.QCheckBox(self.groupBox_5)
        self.cB_tm.setEnabled(False)
        self.cB_tm.setGeometry(QtCore.QRect(140, 47, 115, 17))
        self.cB_tm.setCheckable(True)
        self.cB_tm.setObjectName(_fromUtf8("cB_tm"))
        self.cB_ev = QtGui.QCheckBox(self.groupBox_5)
        self.cB_ev.setEnabled(False)
        self.cB_ev.setGeometry(QtCore.QRect(20, 47, 82, 17))
        self.cB_ev.setCheckable(True)
        self.cB_ev.setObjectName(_fromUtf8("cB_ev"))
        self.cB_tn = QtGui.QCheckBox(self.groupBox_5)
        self.cB_tn.setEnabled(False)
        self.cB_tn.setGeometry(QtCore.QRect(140, 24, 119, 17))
        self.cB_tn.setCheckable(True)
        self.cB_tn.setObjectName(_fromUtf8("cB_tn"))
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_6.setGeometry(QtCore.QRect(380, 150, 291, 71))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.cB_est = QtGui.QCheckBox(self.groupBox_6)
        self.cB_est.setEnabled(False)
        self.cB_est.setGeometry(QtCore.QRect(20, 19, 70, 17))
        self.cB_est.setObjectName(_fromUtf8("cB_est"))
        self.cB_pr = QtGui.QCheckBox(self.groupBox_6)
        self.cB_pr.setEnabled(False)
        self.cB_pr.setGeometry(QtCore.QRect(140, 20, 121, 17))
        self.cB_pr.setObjectName(_fromUtf8("cB_pr"))
        self.cB_rad = QtGui.QCheckBox(self.groupBox_6)
        self.cB_rad.setEnabled(False)
        self.cB_rad.setGeometry(QtCore.QRect(140, 40, 151, 17))
        self.cB_rad.setObjectName(_fromUtf8("cB_rad"))
        self.cB_datos = QtGui.QCheckBox(self.groupBox_3)
        self.cB_datos.setEnabled(False)
        self.cB_datos.setGeometry(QtCore.QRect(230, 150, 101, 17))
        self.cB_datos.setObjectName(_fromUtf8("cB_datos"))
        self.eporttab = QtGui.QWidget()
        self.eporttab.setObjectName(_fromUtf8("eporttab"))
        self.label_9 = QtGui.QLabel(self.eporttab)
        self.label_9.setGeometry(QtCore.QRect(475, 250, 51, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.eporttab)
        self.label_10.setGeometry(QtCore.QRect(475, 290, 51, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.anio1 = QtGui.QLineEdit(self.eporttab)
        self.anio1.setEnabled(False)
        self.anio1.setGeometry(QtCore.QRect(540, 250, 113, 20))
        self.anio1.setObjectName(_fromUtf8("anio1"))
        self.groupBox = QtGui.QGroupBox(self.eporttab)
        self.groupBox.setGeometry(QtCore.QRect(480, 60, 121, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 101, 111))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.rAnio = QtGui.QRadioButton(self.layoutWidget)
        self.rAnio.setObjectName(_fromUtf8("rAnio"))
        self.verticalLayout_5.addWidget(self.rAnio)
        self.rPer = QtGui.QRadioButton(self.layoutWidget)
        self.rPer.setObjectName(_fromUtf8("rPer"))
        self.verticalLayout_5.addWidget(self.rPer)
        self.rHis = QtGui.QRadioButton(self.layoutWidget)
        self.rHis.setChecked(True)
        self.rHis.setObjectName(_fromUtf8("rHis"))
        self.verticalLayout_5.addWidget(self.rHis)
        self.anio2 = QtGui.QLineEdit(self.eporttab)
        self.anio2.setEnabled(False)
        self.anio2.setGeometry(QtCore.QRect(540, 290, 113, 20))
        self.anio2.setObjectName(_fromUtf8("anio2"))
        self.cExcl_2 = QtGui.QCheckBox(self.eporttab)
        self.cExcl_2.setGeometry(QtCore.QRect(144, 330, 288, 17))
        self.cExcl_2.setObjectName(_fromUtf8("cExcl_2"))
        self.label_13 = QtGui.QLabel(self.eporttab)
        self.label_13.setGeometry(QtCore.QRect(75, 163, 61, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.cPeriodicidad = QtGui.QComboBox(self.eporttab)
        self.cPeriodicidad.setGeometry(QtCore.QRect(144, 160, 191, 20))
        self.cPeriodicidad.setObjectName(_fromUtf8("cPeriodicidad"))
        self.cPeriodicidad.addItem(_fromUtf8(""))
        self.cPeriodicidad.addItem(_fromUtf8(""))
        self.cAgrup = QtGui.QComboBox(self.eporttab)
        self.cAgrup.setGeometry(QtCore.QRect(143, 125, 191, 20))
        self.cAgrup.setObjectName(_fromUtf8("cAgrup"))
        self.cAgrup.addItem(_fromUtf8(""))
        self.cAgrup.addItem(_fromUtf8(""))
        self.cMetho = QtGui.QComboBox(self.eporttab)
        self.cMetho.setGeometry(QtCore.QRect(143, 230, 191, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cMetho.sizePolicy().hasHeightForWidth())
        self.cMetho.setSizePolicy(sizePolicy)
        self.cMetho.setObjectName(_fromUtf8("cMetho"))
        self.cTipo = QtGui.QComboBox(self.eporttab)
        self.cTipo.setGeometry(QtCore.QRect(143, 196, 191, 20))
        self.cTipo.setObjectName(_fromUtf8("cTipo"))
        self.cTipo.addItem(_fromUtf8(""))
        self.cTipo.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.eporttab)
        self.label_2.setGeometry(QtCore.QRect(75, 54, 23, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_7 = QtGui.QLabel(self.eporttab)
        self.label_7.setGeometry(QtCore.QRect(75, 85, 37, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.eporttab)
        self.label_8.setGeometry(QtCore.QRect(75, 232, 36, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_11 = QtGui.QLabel(self.eporttab)
        self.label_11.setGeometry(QtCore.QRect(75, 198, 60, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.eporttab)
        self.label_12.setGeometry(QtCore.QRect(74, 128, 61, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.bExport = QtGui.QPushButton(self.eporttab)
        self.bExport.setGeometry(QtCore.QRect(240, 270, 101, 31))
        self.bExport.setObjectName(_fromUtf8("bExport"))
        self.cExcl = QtGui.QCheckBox(self.eporttab)
        self.cExcl.setGeometry(QtCore.QRect(144, 300, 67, 17))
        self.cExcl.setObjectName(_fromUtf8("cExcl"))
        self.cShp = QtGui.QCheckBox(self.eporttab)
        self.cShp.setGeometry(QtCore.QRect(144, 270, 67, 17))
        self.cShp.setObjectName(_fromUtf8("cShp"))
        self.layoutWidget1 = QtGui.QWidget(self.eporttab)
        self.layoutWidget1.setGeometry(QtCore.QRect(143, 44, 301, 71))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lRuta = QtGui.QLineEdit(self.layoutWidget1)
        self.lRuta.setObjectName(_fromUtf8("lRuta"))
        self.horizontalLayout_5.addWidget(self.lRuta)
        self.bRuta = QtGui.QPushButton(self.layoutWidget1)
        self.bRuta.setText(_fromUtf8(""))
        self.bRuta.setIcon(icon1)
        self.bRuta.setAutoDefault(False)
        self.bRuta.setDefault(False)
        self.bRuta.setFlat(False)
        self.bRuta.setObjectName(_fromUtf8("bRuta"))
        self.horizontalLayout_5.addWidget(self.bRuta)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.lShpName = QtGui.QLineEdit(self.layoutWidget1)
        self.lShpName.setObjectName(_fromUtf8("lShpName"))
        self.verticalLayout.addWidget(self.lShpName)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setObjectName(_fromUtf8("menuWindows"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuWindows.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.rAnio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.anio2.setEnabled)
        QtCore.QObject.connect(self.rAnio, QtCore.SIGNAL(_fromUtf8("clicked()")), self.anio2.clear)
        QtCore.QObject.connect(self.rPer, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.anio2.setDisabled)
        QtCore.QObject.connect(self.rAnio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.anio1.setEnabled)
        QtCore.QObject.connect(self.rPer, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.anio1.setDisabled)
        QtCore.QObject.connect(self.rPer, QtCore.SIGNAL(_fromUtf8("clicked()")), self.anio1.clear)
        QtCore.QObject.connect(self.rPer, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.anio1.setEnabled)
        QtCore.QObject.connect(self.rAnio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.anio2.setDisabled)
        QtCore.QObject.connect(self.cExcl_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cShp.setChecked)
        QtCore.QObject.connect(self.rHis, QtCore.SIGNAL(_fromUtf8("clicked()")), self.anio1.clear)
        QtCore.QObject.connect(self.rPer, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.anio2.setEnabled)
        QtCore.QObject.connect(self.groupBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.anio2.clear)
        QtCore.QObject.connect(self.rHis, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.anio1.setDisabled)
        QtCore.QObject.connect(self.rHis, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.anio2.setDisabled)
        QtCore.QObject.connect(self.rAnio, QtCore.SIGNAL(_fromUtf8("clicked()")), self.anio1.clear)
        QtCore.QObject.connect(self.rHis, QtCore.SIGNAL(_fromUtf8("clicked()")), self.anio2.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Evapot Master", None))
        self.importtab.setWindowTitle(_translate("MainWindow", "Cargue de Datos", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Base de Datos", None))
        self.bBd.setText(_translate("MainWindow", "Ejecutar Operación", None))
        self.chBbd.setText(_translate("MainWindow", "La base de Datos Existe", None))
        self.label_37.setText(_translate("MainWindow", "Archivo a Importar", None))
        self.label_38.setText(_translate("MainWindow", "Operación", None))
        self.cBdop.setItemText(0, _translate("MainWindow", "Crear Base de Datos", None))
        self.cBdop.setItemText(1, _translate("MainWindow", "Borrar Base de Datos", None))
        self.cBdop.setItemText(2, _translate("MainWindow", "Exportar Base de Datos", None))
        self.cBdop.setItemText(3, _translate("MainWindow", "Importar Base de Datos", None))
        self.cBdop.setItemText(4, _translate("MainWindow", "Verificar Base de Datos", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Parámetros de Conexión", None))
        self.label_32.setText(_translate("MainWindow", "Contraseña", None))
        self.label_33.setText(_translate("MainWindow", "Base de Datos", None))
        self.label_30.setText(_translate("MainWindow", "Servidor", None))
        self.label_31.setText(_translate("MainWindow", "Puerto", None))
        self.label_34.setText(_translate("MainWindow", "Usuario", None))
        self.label_39.setText(_translate("MainWindow", "Ruta de Salida", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Cargue de Variables", None))
        self.label_14.setText(_translate("MainWindow", "Archivo", None))
        self.label_35.setText(_translate("MainWindow", "Datos", None))
        self.label_36.setText(_translate("MainWindow", "Operación", None))
        self.cBvar.setItemText(0, _translate("MainWindow", "Cargar Datos", None))
        self.cBvar.setItemText(1, _translate("MainWindow", "Eliminar Datos", None))
        self.cBvar.setItemText(2, _translate("MainWindow", "Verificar Datos", None))
        self.bCvar.setText(_translate("MainWindow", "Ejecutar Operación", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Variables Disponibles", None))
        self.cB_hr.setText(_translate("MainWindow", "Humedad Relativa", None))
        self.cB_ve.setText(_translate("MainWindow", "Velocidad del Viento", None))
        self.cB_bs.setText(_translate("MainWindow", "Brillo Solar", None))
        self.cB_tx.setText(_translate("MainWindow", "Temperatura Máxima", None))
        self.cB_tm.setText(_translate("MainWindow", "Temperatura Media", None))
        self.cB_ev.setText(_translate("MainWindow", "Evaporación", None))
        self.cB_tn.setText(_translate("MainWindow", "Temperatura Mínima", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Otros Datos", None))
        self.cB_est.setText(_translate("MainWindow", "Estaciones", None))
        self.cB_pr.setText(_translate("MainWindow", "Tabla Punto de Rocio", None))
        self.cB_rad.setText(_translate("MainWindow", "Tabla Rad. Estraterrestre", None))
        self.cB_datos.setText(_translate("MainWindow", "Datos Cargados", None))
        self.eporttab.setWindowTitle(_translate("MainWindow", "Consulta de Datos", None))
        self.label_9.setText(_translate("MainWindow", "Año Inicial:", None))
        self.label_10.setText(_translate("MainWindow", "Año Final:", None))
        self.groupBox.setTitle(_translate("MainWindow", "Temporalidad", None))
        self.rAnio.setText(_translate("MainWindow", "Año Específico", None))
        self.rPer.setText(_translate("MainWindow", "Período", None))
        self.rHis.setText(_translate("MainWindow", "Toda la Serie", None))
        self.cExcl_2.setText(_translate("MainWindow", "Raster", None))
        self.label_13.setText(_translate("MainWindow", "Periodicidad", None))
        self.cPeriodicidad.setItemText(0, _translate("MainWindow", "Mensual", None))
        self.cPeriodicidad.setItemText(1, _translate("MainWindow", "Decadal", None))
        self.cAgrup.setItemText(0, _translate("MainWindow", "Normal", None))
        self.cAgrup.setItemText(1, _translate("MainWindow", "Promedio", None))
        self.cTipo.setItemText(0, _translate("MainWindow", "Resultado", None))
        self.cTipo.setItemText(1, _translate("MainWindow", "Variable", None))
        self.label_2.setText(_translate("MainWindow", "Ruta", None))
        self.label_7.setText(_translate("MainWindow", "Nombre", None))
        self.label_8.setText(_translate("MainWindow", "Metodo", None))
        self.label_11.setText(_translate("MainWindow", "Tipo de dato", None))
        self.label_12.setText(_translate("MainWindow", "Agrupación", None))
        self.bExport.setText(_translate("MainWindow", "Ejecutar Consulta", None))
        self.cExcl.setText(_translate("MainWindow", "Excel", None))
        self.cShp.setText(_translate("MainWindow", "Shapefile", None))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows", None))

import ofolder_rc
