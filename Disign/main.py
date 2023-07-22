
from distutils.log import info
import sys
import shutil
import os
from PyQt6 import QtCore, QtGui, QtWidgets
import logo_rc
from  systemMain import Ui_MainWindow
from reg import Ui_Form
from info import Ui_info_Window



app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
RegWindow = QtWidgets.QWidget()
InfoWindow = QtWidgets.QWidget()

uiMain = Ui_MainWindow()
uiMain.setupUi(MainWindow)

uiReg = Ui_Form()
uiReg.setupUi(RegWindow)

uiInfo = Ui_info_Window()
uiInfo.setupUi(InfoWindow)

MainWindow.show()
#sys.exit(app.exec())

def openReg():
    
    MainWindow.close()
    uiReg.setupUi(RegWindow)
    RegWindow.show()
    
    uiReg.regRegButton.clicked.connect(regPerson)
    uiReg.regBackButton.clicked.connect(backFromReg)

def backFromReg():
    
    RegWindow.close()
    MainWindow.show()
 

def backFromInfo():

    InfoWindow.close()
    MainWindow.show()


def openInfo():

    #uiInfo.setupUi(InfoWindow)

    accept = QtWidgets.QMessageBox()
    accept.setWindowTitle('Подготовка')
    accept.setText('''Для более качественного распознавания отодвиньтесь на расстояние
половины вытянутой руки, снимите очки и другие головные уборы''')
    accept.setIcon(QtWidgets.QMessageBox.Icon.Information)
    accept.exec()

    sys.path.insert(0, "C://VS Code//Face//BioBackend")
    from tandem import tandem
    from checkPhoto import checkphoto
    
    personalNumber = checkphoto()
    if personalNumber != None:
        infoStudent = tandem(personalNumber)

        uiInfo.personalNumber_label.setText(personalNumber)
        uiInfo.firstName_label.setText(infoStudent['firstName'][0])
        uiInfo.middleName_label.setText(infoStudent['middleName'][0])
        uiInfo.surnameName_label.setText(infoStudent['surname'][0])
        uiInfo.telephone_label.setText(infoStudent['telephone'][0])
        uiInfo.program_label.setText(infoStudent['programTitle'][0])
        uiInfo.gtoup_label.setText(infoStudent['group'][0])
        uiInfo.form_label.setText(infoStudent['form'][0])
        uiInfo.payment_label.setText(infoStudent['compensation'][0])
        uiInfo.course_label.setText(str(infoStudent['course'][0]))
        MainWindow.close()
        InfoWindow.show()
        uiInfo.infBackButton.clicked.connect(backFromInfo)
    else:
        error = QtWidgets.QMessageBox()
        error.setWindowTitle('Ошибка')
        error.setText(f'Студент не найден\nПроверьте камеру')
        error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        error.exec()

def regPerson():


    personalNumber = int(uiReg.lineEdit.text())
    sys.path.insert(0, "C://VS Code//Face//BioBackend")
    from makephoto import makephoto
    #os.chdir('..')
    len = makephoto(personalNumber)

    if len != 0:
        accept = QtWidgets.QMessageBox()
        accept.setWindowTitle('Успешно')
        accept.setText(f'Студент {personalNumber} успешно зарегистрирован!')
        accept.setIcon(QtWidgets.QMessageBox.Icon.Information)
        accept.exec()
        #uiReg.lineEdit.setText('')
    else:
        shutil.rmtree(f'{os.getcwd()}/Images/{personalNumber}')
        error = QtWidgets.QMessageBox()
        error.setWindowTitle('Ошибка')
        error.setText(f'Студент {personalNumber} не зарегистрирован\nПроверьте камеру')
        error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        error.exec()
        #uiReg.lineEdit.setText('')
        




uiMain.regButton.clicked.connect(openReg)
uiMain.IdentButton.clicked.connect(openInfo)




    

sys.exit(app.exec())

