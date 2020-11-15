from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time
import random
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 716)
        MainWindow.setMaximumSize(QtCore.QSize(453, 716))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 160, 431, 311))
        self.groupBox.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(320, 40, 101, 31))
        self.label_2.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(240, 40, 81, 31))
        self.label.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 71, 31))
        self.label_3.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(80, 80, 81, 31))
        self.label_4.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(80, 40, 151, 31))
        self.label_5.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 71, 31))
        self.label_6.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(220, 80, 61, 31))
        self.label_7.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(170, 80, 51, 31))
        self.label_8.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(350, 80, 71, 31))
        self.label_9.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(290, 80, 61, 31))
        self.label_10.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 120, 411, 181))
        self.plainTextEdit.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.plainTextEdit.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 480, 431, 161))
        self.groupBox_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.label_16.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_16.setObjectName("label_16")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 40, 121, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 40, 81, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(240, 40, 101, 31))
        self.label_17.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 80, 121, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.label_18.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(280, 80, 41, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(240, 80, 41, 31))
        self.label_19.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_19.setObjectName("label_19")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(380, 80, 41, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(340, 80, 41, 31))
        self.label_20.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_20.setObjectName("label_20")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 431, 131))
        self.groupBox_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 255);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(240, 40, 51, 31))
        self.label_22.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_22.setObjectName("label_22")
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(10, 40, 51, 31))
        self.label_26.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_26.setObjectName("label_26")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(60, 40, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 40, 131, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(290, 80, 131, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(170, 80, 111, 31))
        self.comboBox.setStyleSheet("color: rgb(0, 255, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_26.raise_()
        self.lineEdit.raise_()
        self.label_22.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.comboBox.raise_()
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 650, 131, 31))
        self.pushButton_2.setStyleSheet("\n"
"background-color: rgb(0, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 650, 131, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.login_iq)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mack UP V1 By ThongD"))
        self.groupBox.setTitle(_translate("MainWindow", "Show"))
        self.label.setText(_translate("MainWindow", "Balance :"))
        self.label_3.setText(_translate("MainWindow", "Profit  :"))
        self.label_6.setText(_translate("MainWindow", "Status :"))
        self.label_8.setText(_translate("MainWindow", "Win  :"))
        self.label_10.setText(_translate("MainWindow", "Loss  :"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "สนับสนุน   :สหวัชระ \n"

""))
        self.groupBox_2.setTitle(_translate("MainWindow", "Input"))
        self.label_16.setText(_translate("MainWindow", "* MG       :"))
        self.label_17.setText(_translate("MainWindow", "Amount  :"))
        self.label_18.setText(_translate("MainWindow", "๋Max MG   :"))
        self.label_19.setText(_translate("MainWindow", "TP :"))
        self.label_20.setText(_translate("MainWindow", "SL :"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Login IQ OPTION"))
        self.label_22.setText(_translate("MainWindow", "Pass :"))
        self.label_26.setText(_translate("MainWindow", "User :"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.comboBox.setItemText(0, _translate("MainWindow", "PRACTICE"))
        self.comboBox.setItemText(1, _translate("MainWindow", "REAL"))
        self.pushButton_2.setText(_translate("MainWindow", "START"))
        self.pushButton_3.setText(_translate("MainWindow", "STOP"))


 
    def login_iq(self):
        def stop_run():
            self.plainTextEdit.appendPlainText("หยุดทำงาน!")
            while True:
                QtCore.QCoreApplication.processEvents()
                
        def mack_up():
            self.plainTextEdit.appendPlainText("เริ่มทำงาน!")
            profit = 0.0
            wins = 0
            loss = 0
            RMG  = 0
            ATM  = self.lineEdit_4.text()
            MAXMG = self.lineEdit_5.text()
            XMG   = self.lineEdit_3.text()
            TP    = self.lineEdit_6.text()
            SL    = self.lineEdit_7.text()
            while True:
                QtCore.QCoreApplication.processEvents()
                if ATM == "":
                    while ATM == "":
                        QtCore.QCoreApplication.processEvents()
                        self.plainTextEdit.appendPlainText("กรุณาเช็คการตั้งค่าจำนวนเงิน!")
                        if ATM != "":
                            ATM  = self.lineEdit_4.text()
                            break
                if TP != "":                
                    if float(profit) >= float(TP):
                        self.plainTextEdit.appendPlainText("ยินดีด้วยถึง TP ที่กำหนด!")
                        stop_run()
                if SL != "":
                    if float(profit) <= (float(SL)* -1.00):
                        print(SL)
                        self.plainTextEdit.appendPlainText("รอบหน้าเอาใหม่ถึง SL ที่กำหนด!")
                        stop_run()
    
                TMIQ   = API.get_server_timestamp()
                FMTMIQ = datetime.fromtimestamp(TMIQ)
                DOTC   = (FMTMIQ.strftime("%w"))
                RDOD = random.choices(["call","put"])
                OD   = (RDOD[0])  
                while True:
                    QtCore.QCoreApplication.processEvents()
                    chop1 = API.get_all_open_time()
                    if DOTC == 5 or DOTC == 0 or (chop1["digital"]["USDJPY-OTC"]["open"]) == True:
                        RDCA = random.choices(["USDJPY-OTC","EURJPY-OTC","USDCHF-OTC","EURUSD-OTC","AUDCAD-OTC","GBPUSD-OTC","GBPJPY-OTC","EURGBP-OTC"])
                        CA = (RDCA[0])
                        chop2 = (chop1["digital"][CA]["open"])
                        if chop2 == True:
                                break
                    elif (chop1["digital"]["USDJPY"]["open"]) == True:
                        RDCA = random.choices(["USDJPY","EURJPY","USDCHF","EURUSD","AUDCAD","GBPUSD","GBPJPY","EURGBP"])
                        CA = (RDCA[0])
                        chop2 = (chop1["digital"][CA]["open"])
                        if chop2 == True:
                                break
                    else:
                        RDCA = random.choices(["USDJPY","EURJPY","USDCHF","EURUSD","AUDCAD","GBPUSD","GBPJPY","EURGBP"])
                        CA = (RDCA[0])
                        chop2 = (chop1["digital"][CA]["open"])
                        if chop2 == True:
                                break
                while True:
                    QtCore.QCoreApplication.processEvents()
                    TMIQ   = API.get_server_timestamp()
                    FMTMIQ = datetime.fromtimestamp(TMIQ)
                    if FMTMIQ.second <= 5:
                        if ATM == "":
                            while ATM == "":
                                QtCore.QCoreApplication.processEvents()
                                self.plainTextEdit.appendPlainText("กรุณาเช็คการตั้งค่าจำนวนเงิน!")
                                ATM  = self.lineEdit_4.text()
                        if int(ATM) < 1:
                            ATM = 1
                        order_iq,id = (API.buy_digital_spot(CA,float(ATM),OD,1))
                        if order_iq == True:
                            show_opod = ("ออก Order"+(" ")+str(CA))
                            self.plainTextEdit.appendPlainText(show_opod)
                            while True:
                                QtCore.QCoreApplication.processEvents()
                                check,win = API.check_win_digital_v2(id)
                                if check == True:
                                    break
                            if win > 0:
                                wins = wins + 1
                                RMG  = 0
                                ATM  = self.lineEdit_4.text()
                                profit = profit + win
                                show_rs = ("ชนะ"+str(" ")+str("%.2f"%win))
                                self.plainTextEdit.appendPlainText(show_rs)
                                self.label_4.setNum(float("%.2f" %profit))
                                self.label_7.setNum(wins)
                                break
                
                
                            else:
                                loss = loss + 1
                                RMG  = RMG + 1
                                if MAXMG != "":
                                    ATM = float(ATM) * float(XMG)
                                    if RMG > int(MAXMG):
                                        ATM  = self.lineEdit_4.text()

                                profit = profit + win
                                show_rs = ("แพ้"+str(" ")+str("%.2f"%win))
                                self.plainTextEdit.appendPlainText(show_rs)
                                self.label_4.setNum(float("%.2f" %profit))
                                self.label_9.setNum(loss)
                                break
                        else:
                            show_opod = ("ออก Order ไม่สำเร็จ!"+(" ")+str(CA))
                            self.plainTextEdit.appendPlainText(show_opod)
                            break
                    else:
                        show_st = ("รอเวลา...:"+str(FMTMIQ.second)+str(":")+str(CA)+str(":")+str(OD))
                        self.plainTextEdit.appendPlainText(show_st)
                  

        user     = self.lineEdit.text()
        password = self.lineEdit_2.text()
        API=IQ_Option(user,password)
        iqch1,iqch2 = API.connect()
        if iqch1 == True:
            self.label_5.setText("ล็อคอินสำเร็จ!")
            mode = self.comboBox.currentText()
            API.change_balance(mode)
            BA = API.get_balance()
            self.label_2.setNum(BA)
            self.pushButton_2.clicked.connect(mack_up)
            self.pushButton_3.clicked.connect(stop_run)
        else:
            self.label_5.setText("ล็อคอินไม่ผ่าน!")
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
