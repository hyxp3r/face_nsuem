# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import logo_rc

class Ui_info_Window(object):
    def setupUi(self, info_Window):
        info_Window.setObjectName("info_Window")
        #info_Window.resize(1165, 370)
        info_Window.setGeometry(QtCore.QRect(70, 170, 1165, 390))
        self.surnameName_label = QtWidgets.QLabel(info_Window)
        self.surnameName_label.setGeometry(QtCore.QRect(140, 230, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.surnameName_label.setFont(font)
        self.surnameName_label.setObjectName("surnameName_label")
        self.telephone_label = QtWidgets.QLabel(info_Window)
        self.telephone_label.setGeometry(QtCore.QRect(137, 270, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.telephone_label.setFont(font)
        self.telephone_label.setObjectName("telephone_label")
        self.personalNumber_label = QtWidgets.QLabel(info_Window)
        self.personalNumber_label.setGeometry(QtCore.QRect(210, 110, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.personalNumber_label.setFont(font)
        self.personalNumber_label.setObjectName("personalNumber_label")
        self.program_label = QtWidgets.QLabel(info_Window)
        self.program_label.setGeometry(QtCore.QRect(500, 110, 681, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.program_label.setFont(font)
        self.program_label.setObjectName("program_label")
        self.programTitle_label_2 = QtWidgets.QLabel(info_Window)
        self.programTitle_label_2.setGeometry(QtCore.QRect(340, 150, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.programTitle_label_2.setFont(font)
        self.programTitle_label_2.setObjectName("programTitle_label_2")
        self.form_label_2 = QtWidgets.QLabel(info_Window)
        self.form_label_2.setGeometry(QtCore.QRect(340, 190, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.form_label_2.setFont(font)
        self.form_label_2.setObjectName("form_label_2")
        self.course_label = QtWidgets.QLabel(info_Window)
        self.course_label.setGeometry(QtCore.QRect(400, 230, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.course_label.setFont(font)
        self.course_label.setObjectName("course_label")
        self.middleName_label = QtWidgets.QLabel(info_Window)
        self.middleName_label.setGeometry(QtCore.QRect(90, 190, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.middleName_label.setFont(font)
        self.middleName_label.setObjectName("middleName_label")
        self.surName_label_2 = QtWidgets.QLabel(info_Window)
        self.surName_label_2.setGeometry(QtCore.QRect(30, 230, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.surName_label_2.setFont(font)
        self.surName_label_2.setObjectName("surName_label_2")
        self.telephone_label_2 = QtWidgets.QLabel(info_Window)
        self.telephone_label_2.setGeometry(QtCore.QRect(30, 270, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.telephone_label_2.setFont(font)
        self.telephone_label_2.setObjectName("surName_label_2")
        self.logo_2 = QtWidgets.QLabel(info_Window)
        self.logo_2.setGeometry(QtCore.QRect(10, 20, 161, 61))
        self.logo_2.setText("")
        self.logo_2.setPixmap(QtGui.QPixmap(":/NewPrefix/ЛОГО НГУЭУ_без текста.png"))
        self.logo_2.setScaledContents(True)
        self.logo_2.setObjectName("logo_2")
        self.logoText_Reg = QtWidgets.QLabel(info_Window)
        self.logoText_Reg.setGeometry(QtCore.QRect(190, 10, 741, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.logoText_Reg.setFont(font)
        self.logoText_Reg.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.logoText_Reg.setObjectName("logoText_Reg")
        self.middleName_label_2 = QtWidgets.QLabel(info_Window)
        self.middleName_label_2.setGeometry(QtCore.QRect(30, 190, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.middleName_label_2.setFont(font)
        self.middleName_label_2.setObjectName("middleName_label_2")
        self.programTitle_label_3 = QtWidgets.QLabel(info_Window)
        self.programTitle_label_3.setGeometry(QtCore.QRect(340, 230, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.programTitle_label_3.setFont(font)
        self.programTitle_label_3.setObjectName("programTitle_label_3")
        self.programTitle_label_4 = QtWidgets.QLabel(info_Window)
        self.programTitle_label_4.setGeometry(QtCore.QRect(340, 270, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.programTitle_label_4.setFont(font)
        self.programTitle_label_4.setObjectName("programTitle_label_4")
        self.programTitle_label = QtWidgets.QLabel(info_Window)
        self.programTitle_label.setGeometry(QtCore.QRect(340, 110, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.programTitle_label.setFont(font)
        self.programTitle_label.setObjectName("programTitle_label")
        self.printButton = QtWidgets.QPushButton(info_Window)
        self.printButton.setGeometry(QtCore.QRect(380, 340, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.printButton.setFont(font)
        self.printButton.setObjectName("printButton")
        self.personalNumber_label_2 = QtWidgets.QLabel(info_Window)
        self.personalNumber_label_2.setGeometry(QtCore.QRect(30, 110, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.personalNumber_label_2.setFont(font)
        self.personalNumber_label_2.setObjectName("personalNumber_label_2")
        self.gtoup_label = QtWidgets.QLabel(info_Window)
        self.gtoup_label.setGeometry(QtCore.QRect(430, 150, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.gtoup_label.setFont(font)
        self.gtoup_label.setObjectName("gtoup_label")
        self.form_label = QtWidgets.QLabel(info_Window)
        self.form_label.setGeometry(QtCore.QRect(430, 190, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.form_label.setFont(font)
        self.form_label.setObjectName("form_label")
        self.personalNumber_label_3 = QtWidgets.QLabel(info_Window)
        self.personalNumber_label_3.setGeometry(QtCore.QRect(30, 150, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.personalNumber_label_3.setFont(font)
        self.personalNumber_label_3.setObjectName("personalNumber_label_3")
        self.payment_label = QtWidgets.QLabel(info_Window)
        self.payment_label.setGeometry(QtCore.QRect(590, 270, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.payment_label.setFont(font)
        self.payment_label.setObjectName("payment_label")
        self.infBackButton = QtWidgets.QPushButton(info_Window)
        self.infBackButton.setGeometry(QtCore.QRect(560, 340, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.infBackButton.setFont(font)
        self.infBackButton.setObjectName("infBackButton")
        self.firstName_label = QtWidgets.QLabel(info_Window)
        self.firstName_label.setGeometry(QtCore.QRect(140, 150, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.firstName_label.setFont(font)
        self.firstName_label.setObjectName("firstName_label")

        self.retranslateUi(info_Window)
        QtCore.QMetaObject.connectSlotsByName(info_Window)

    def retranslateUi(self, info_Window):
        _translate = QtCore.QCoreApplication.translate
        info_Window.setWindowTitle(_translate("info_Window", "Form"))
        self.surnameName_label.setText(_translate("info_Window", "Николаевич"))
        self.telephone_label.setText(_translate("info_Window", "89139543204"))
        self.personalNumber_label.setText(_translate("info_Window", "190722"))
        self.program_label.setText(_translate("info_Window", "09.03.02 Правовое обеспечение национальной безопасности"))
        self.programTitle_label_2.setText(_translate("info_Window", "Группа:"))
        self.form_label_2.setText(_translate("info_Window", "Форма:"))
        self.course_label.setText(_translate("info_Window", "4"))
        self.middleName_label.setText(_translate("info_Window", "Евгений"))
        self.surName_label_2.setText(_translate("info_Window", "Отчество:"))
        self.telephone_label_2.setText(_translate("info_Window", "Телефон:"))
        self.logoText_Reg.setText(_translate("info_Window", "Информационные сведения об обучающимся"))
        self.middleName_label_2.setText(_translate("info_Window", "Имя:"))
        self.programTitle_label_3.setText(_translate("info_Window", "Курс:"))
        self.programTitle_label_4.setText(_translate("info_Window", "Тип финансирования:"))
        self.programTitle_label.setText(_translate("info_Window", "Направление:"))
        self.printButton.setText(_translate("info_Window", "Печатать справку"))
        self.personalNumber_label_2.setText(_translate("info_Window", "Личный номер:"))
        self.gtoup_label.setText(_translate("info_Window", "ПИ9011"))
        self.form_label.setText(_translate("info_Window", "очно-заочная"))
        self.personalNumber_label_3.setText(_translate("info_Window", "Фамилия:"))
        self.payment_label.setText(_translate("info_Window", "договор"))
        self.infBackButton.setText(_translate("info_Window", "Назад"))
        self.firstName_label.setText(_translate("info_Window", "Ермаков"))
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    info_Window = QtWidgets.QWidget()
    ui = Ui_info_Window()
    ui.setupUi(info_Window)
    info_Window.show()
    sys.exit(app.exec())
