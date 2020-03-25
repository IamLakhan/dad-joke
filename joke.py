# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'joke.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from gtts import gTTS 
import os 


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(164, 37)
        self.button = QtWidgets.QPushButton(Form)
        self.button.setGeometry(QtCore.QRect(-2, 0, 171, 41))
        self.button.setObjectName("button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dad Jokes"))
        self.button.setText(_translate("Form", "I am bored"))
        self.button.clicked.connect(self.jokes)

    def jokes(self):
        url = "https://icanhazdadjoke.com/"

        response = requests.get(url, headers={"Accept": "application/json"})

        data = response.json()
        mytext = str(data["joke"])
        language = 'en'
        tts = gTTS(text=mytext, lang=language, slow=False) 
        tts.save("welcome.mp3") 
        os.system("mpg321 welcome.mp3")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
