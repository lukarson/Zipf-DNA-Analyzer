from PyQt5 import QtCore, QtWidgets
import dna


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(421, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(421, 450))
        MainWindow.setMaximumSize(QtCore.QSize(421, 450))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")

        # Group boxes
        self.fileGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.fileGroupBox.setGeometry(QtCore.QRect(20, 20, 381, 191))
        self.fileGroupBox.setObjectName("fileGroupBox")
        self.settingsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.settingsGroupBox.setGeometry(QtCore.QRect(20, 230, 381, 161))
        self.settingsGroupBox.setObjectName("settingsGroupBox")

        # Buttons
        self.browseButton = QtWidgets.QPushButton(self.fileGroupBox)
        self.browseButton.setGeometry(QtCore.QRect(260, 80, 111, 28))
        self.browseButton.setObjectName("browseButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(310, 400, 93, 28))
        self.closeButton.setObjectName("closeButton")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(190, 400, 101, 28))
        self.generateButton.setObjectName("generateButton")
        self.generateButton.setDisabled(True)

        # Checkboxes
        self.expCheckBox = QtWidgets.QCheckBox(self.settingsGroupBox)
        self.expCheckBox.setGeometry(QtCore.QRect(30, 90, 111, 20))
        self.expCheckBox.setChecked(True)
        self.expCheckBox.setObjectName("expCheckBox")
        self.dLogCheckBox = QtWidgets.QCheckBox(self.settingsGroupBox)
        self.dLogCheckBox.setGeometry(QtCore.QRect(180, 90, 191, 20))
        self.dLogCheckBox.setObjectName("dLogCheckBox")
        self.histCheckBox = QtWidgets.QCheckBox(self.settingsGroupBox)
        self.histCheckBox.setGeometry(QtCore.QRect(180, 120, 191, 20))
        self.histCheckBox.setObjectName("histCheckBox")
        self.logCheckBox = QtWidgets.QCheckBox(self.settingsGroupBox)
        self.logCheckBox.setGeometry(QtCore.QRect(30, 120, 111, 20))
        self.logCheckBox.setObjectName("logCheckBox")

        # Labels
        self.kLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.kLabel.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.kLabel.setObjectName("kLabel")
        self.pLabel = QtWidgets.QLabel(self.settingsGroupBox)
        self.pLabel.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.pLabel.setObjectName("pLabel")
        self.oLabel = QtWidgets.QLabel(self.fileGroupBox)
        self.oLabel.setGeometry(QtCore.QRect(10, 110, 201, 31))
        self.oLabel.setObjectName("oLabel")
        self.iLabel = QtWidgets.QLabel(self.fileGroupBox)
        self.iLabel.setGeometry(QtCore.QRect(10, 20, 201, 31))
        self.iLabel.setObjectName("iLabel")

        # Combo box
        self.kComboBox = QtWidgets.QComboBox(self.settingsGroupBox)
        self.kComboBox.setGeometry(QtCore.QRect(120, 30, 51, 20))
        self.kComboBox.setObjectName("kComboBox")
        self.kComboBox.addItem("")
        self.kComboBox.addItem("")
        self.kComboBox.addItem("")
        self.kComboBox.addItem("")
        self.kComboBox.addItem("")
        self.kComboBox.addItem("")
        self.kComboBox.addItem("")
        self.kComboBox.addItem("")
        self.kComboBox.addItem("")
        self.kComboBox.addItem("")
        self.kComboBox.setCurrentIndex(2)

        # Line edits
        self.iLineEdit = QtWidgets.QLineEdit(self.fileGroupBox)
        self.iLineEdit.setGeometry(QtCore.QRect(10, 50, 361, 22))
        self.iLineEdit.setObjectName("iLineEdit")
        self.iLineEdit.setReadOnly(True)
        self.oLineEdit = QtWidgets.QLineEdit(self.fileGroupBox)
        self.oLineEdit.setGeometry(QtCore.QRect(10, 140, 361, 22))
        self.oLineEdit.setText("")
        self.oLineEdit.setObjectName("oLineEdit")

        self.fileGroupBox.raise_()
        self.settingsGroupBox.raise_()
        self.closeButton.raise_()
        self.generateButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        # Behaviors
        self.closeButton.clicked.connect(onCloseButtonClicked)
        self.generateButton.clicked.connect(self.onGenerateButtonClicked)
        self.browseButton.clicked.connect(self.openFileNameDialog)

        # Initiate UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zipf DNA Distribution"))
        self.closeButton.setText(_translate("MainWindow", "Zamknij"))
        self.generateButton.setText(_translate("MainWindow", "Generuj"))
        self.settingsGroupBox.setTitle(_translate("MainWindow", "Ustawienia generacji"))
        self.expCheckBox.setText(_translate("MainWindow", "wykładniczy"))
        self.dLogCheckBox.setText(_translate("MainWindow", "podwójnie logarytmiczny"))
        self.histCheckBox.setText(_translate("MainWindow", "histogram"))
        self.logCheckBox.setText(_translate("MainWindow", "logarytmiczny"))
        self.kLabel.setText(_translate("MainWindow", "Długość słów k:"))
        self.kComboBox.setItemText(0, _translate("MainWindow", "1"))
        self.kComboBox.setItemText(1, _translate("MainWindow", "2"))
        self.kComboBox.setItemText(2, _translate("MainWindow", "3"))
        self.kComboBox.setItemText(3, _translate("MainWindow", "4"))
        self.kComboBox.setItemText(4, _translate("MainWindow", "5"))
        self.kComboBox.setItemText(5, _translate("MainWindow", "6"))
        self.kComboBox.setItemText(6, _translate("MainWindow", "7"))
        self.kComboBox.setItemText(7, _translate("MainWindow", "8"))
        self.kComboBox.setItemText(8, _translate("MainWindow", "9"))
        self.kComboBox.setItemText(9, _translate("MainWindow", "10"))
        self.pLabel.setText(_translate("MainWindow", "Wykresy:"))
        self.fileGroupBox.setTitle(_translate("MainWindow", "Plik wejściowy i wyjściowy"))
        self.browseButton.setText(_translate("MainWindow", "Wybierz plik..."))
        self.oLabel.setText(_translate("MainWindow", "Zapisz do pliku o nazwie:"))
        self.iLabel.setText(_translate("MainWindow", "Ścieżka do pliku z sekwencją DNA:"))

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                                                            caption="Wybierz plik z kodem DNA",
                                                            filter="All Files (*);;Text Files (*.txt)",
                                                            options=options)
        if not fileName:
            return

        parsed = dna.parseFile(fileName)

        if parsed is None:
            dna.displayMessage(1)
        else:
            self.iLineEdit.setText(fileName)
            raw_filename = fileName.split("/")[-1].split(".")[0]
            raw_path = fileName.split(raw_filename)[0]
            self.oLineEdit.setText(raw_path + "zipf_dist_" + raw_filename + ".csv")
            self.generateButton.setDisabled(False)

    def onGenerateButtonClicked(self):
        parsed = dna.parseFile(self.iLineEdit.text())
        outFileText = self.oLineEdit.text().replace(' ', '').split(".")

        if parsed is None:
            dna.displayMessage(1)

        elif outFileText[0] == "" or outFileText[1] != "csv":
            dna.displayMessage(2)

        else:
            checkboxes = [self.expCheckBox, self.logCheckBox, self.dLogCheckBox, self.histCheckBox]
            k = int(self.kComboBox.currentText())

            for c in checkboxes:
                if c.isChecked():
                    print(c.text())

            dna.generateZipfDistribution(parsed, self.oLineEdit.text(), k)
            dna.displayMessage(0)


def onCloseButtonClicked():
    QtCore.QCoreApplication.instance().quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
