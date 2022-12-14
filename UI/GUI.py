# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab2LandMarksDetection = QtWidgets.QTabWidget(self.centralwidget)
        self.tab2LandMarksDetection.setObjectName("tab2LandMarksDetection")
        self.tab1FaceShape = QtWidgets.QWidget()
        self.tab1FaceShape.setObjectName("tab1FaceShape")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab1FaceShape)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.faceShapeModel1Widget = QtWidgets.QWidget(self.tab1FaceShape)
        self.faceShapeModel1Widget.setObjectName("faceShapeModel1Widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.faceShapeModel1Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.faceShapeModel1Label = QtWidgets.QLabel(self.faceShapeModel1Widget)
        self.faceShapeModel1Label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.faceShapeModel1Label.setFont(font)
        self.faceShapeModel1Label.setObjectName("faceShapeModel1Label")
        self.verticalLayout.addWidget(self.faceShapeModel1Label)
        self.tab1Model1FaceShapeImageLabel = QtWidgets.QLabel(self.faceShapeModel1Widget)
        self.tab1Model1FaceShapeImageLabel.setText("")
        self.tab1Model1FaceShapeImageLabel.setObjectName("tab1Model1FaceShapeImageLabel")
        self.verticalLayout.addWidget(self.tab1Model1FaceShapeImageLabel)
        self.tab1Model1FaceShapeResultLabel = QtWidgets.QLabel(self.faceShapeModel1Widget)
        self.tab1Model1FaceShapeResultLabel.setText("")
        self.tab1Model1FaceShapeResultLabel.setObjectName("tab1Model1FaceShapeResultLabel")
        self.verticalLayout.addWidget(self.tab1Model1FaceShapeResultLabel)
        self.horizontalLayout_3.addWidget(self.faceShapeModel1Widget)
        self.verticalLineTab1FaceShape = QtWidgets.QFrame(self.tab1FaceShape)
        self.verticalLineTab1FaceShape.setFrameShape(QtWidgets.QFrame.VLine)
        self.verticalLineTab1FaceShape.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLineTab1FaceShape.setObjectName("verticalLineTab1FaceShape")
        self.horizontalLayout_3.addWidget(self.verticalLineTab1FaceShape)
        self.faceShapeModel2Widget = QtWidgets.QWidget(self.tab1FaceShape)
        self.faceShapeModel2Widget.setObjectName("faceShapeModel2Widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.faceShapeModel2Widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.faceShapeModel2Label = QtWidgets.QLabel(self.faceShapeModel2Widget)
        self.faceShapeModel2Label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.faceShapeModel2Label.setFont(font)
        self.faceShapeModel2Label.setObjectName("faceShapeModel2Label")
        self.verticalLayout_2.addWidget(self.faceShapeModel2Label)
        self.tab1Model2FaceShapeImageLabel = QtWidgets.QLabel(self.faceShapeModel2Widget)
        self.tab1Model2FaceShapeImageLabel.setText("")
        self.tab1Model2FaceShapeImageLabel.setObjectName("tab1Model2FaceShapeImageLabel")
        self.verticalLayout_2.addWidget(self.tab1Model2FaceShapeImageLabel)
        self.tab1Model2ResultLabel = QtWidgets.QLabel(self.faceShapeModel2Widget)
        self.tab1Model2ResultLabel.setText("")
        self.tab1Model2ResultLabel.setObjectName("tab1Model2ResultLabel")
        self.verticalLayout_2.addWidget(self.tab1Model2ResultLabel)
        self.horizontalLayout_3.addWidget(self.faceShapeModel2Widget)
        self.tab2LandMarksDetection.addTab(self.tab1FaceShape, "")
        self.tab2LandMarks = QtWidgets.QWidget()
        self.tab2LandMarks.setObjectName("tab2LandMarks")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab2LandMarks)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.landMarksLabel = QtWidgets.QLabel(self.tab2LandMarks)
        self.landMarksLabel.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.landMarksLabel.setFont(font)
        self.landMarksLabel.setObjectName("landMarksLabel")
        self.verticalLayout_3.addWidget(self.landMarksLabel)
        self.landMarksViewerWidget = QtWidgets.QWidget(self.tab2LandMarks)
        self.landMarksViewerWidget.setObjectName("landMarksViewerWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.landMarksViewerWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tab2landMarksFaceImageViewerLabel = QtWidgets.QLabel(self.landMarksViewerWidget)
        self.tab2landMarksFaceImageViewerLabel.setText("")
        self.tab2landMarksFaceImageViewerLabel.setObjectName("tab2landMarksFaceImageViewerLabel")
        self.horizontalLayout_2.addWidget(self.tab2landMarksFaceImageViewerLabel)
        self.line = QtWidgets.QFrame(self.landMarksViewerWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.tab2LandMarksResultLabel = QtWidgets.QLabel(self.landMarksViewerWidget)
        self.tab2LandMarksResultLabel.setText("")
        self.tab2LandMarksResultLabel.setObjectName("tab2LandMarksResultLabel")
        self.horizontalLayout_2.addWidget(self.tab2LandMarksResultLabel)
        self.verticalLayout_3.addWidget(self.landMarksViewerWidget)
        self.tab2LandMarksDetection.addTab(self.tab2LandMarks, "")
        self.horizontalLayout.addWidget(self.tab2LandMarksDetection)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRun = QtWidgets.QMenu(self.menuFile)
        self.menuRun.setObjectName("menuRun")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRun_Model_I = QtWidgets.QAction(MainWindow)
        self.actionRun_Model_I.setObjectName("actionRun_Model_I")
        self.actionRun_Model_II = QtWidgets.QAction(MainWindow)
        self.actionRun_Model_II.setObjectName("actionRun_Model_II")
        self.actionLandMarks_Model = QtWidgets.QAction(MainWindow)
        self.actionLandMarks_Model.setObjectName("actionLandMarks_Model")
        self.actionModel_1 = QtWidgets.QAction(MainWindow)
        self.actionModel_1.setObjectName("actionModel_1")
        self.actionModel_2 = QtWidgets.QAction(MainWindow)
        self.actionModel_2.setObjectName("actionModel_2")
        self.actionLandMarks = QtWidgets.QAction(MainWindow)
        self.actionLandMarks.setObjectName("actionLandMarks")
        self.actionModel_3 = QtWidgets.QAction(MainWindow)
        self.actionModel_3.setObjectName("actionModel_3")
        self.actionModel_4 = QtWidgets.QAction(MainWindow)
        self.actionModel_4.setObjectName("actionModel_4")
        self.menuRun.addAction(self.actionLandMarks_Model)
        self.menuRun.addAction(self.actionModel_1)
        self.menuRun.addAction(self.actionModel_2)
        self.menuSave.addAction(self.actionLandMarks)
        self.menuSave.addAction(self.actionModel_3)
        self.menuSave.addAction(self.actionModel_4)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuRun.menuAction())
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.tab2LandMarksDetection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.faceShapeModel1Label.setText(_translate("MainWindow", "Face Shape Classification Model I"))
        self.faceShapeModel2Label.setText(_translate("MainWindow", "Face Shape Classification Model II"))
        self.tab2LandMarksDetection.setTabText(self.tab2LandMarksDetection.indexOf(self.tab1FaceShape), _translate("MainWindow", "Tab 1"))
        self.landMarksLabel.setText(_translate("MainWindow", "Land Marks Model"))
        self.tab2LandMarksDetection.setTabText(self.tab2LandMarksDetection.indexOf(self.tab2LandMarks), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuOptions.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen.setText(_translate("MainWindow", "Open "))
        self.actionRun_Model_I.setText(_translate("MainWindow", "Run Model I"))
        self.actionRun_Model_II.setText(_translate("MainWindow", "Run Model II"))
        self.actionLandMarks_Model.setText(_translate("MainWindow", "LandMarks Model"))
        self.actionModel_1.setText(_translate("MainWindow", "Model 1"))
        self.actionModel_2.setText(_translate("MainWindow", "Model 2"))
        self.actionLandMarks.setText(_translate("MainWindow", "LandMarks"))
        self.actionModel_3.setText(_translate("MainWindow", "Model 1"))
        self.actionModel_4.setText(_translate("MainWindow", "Model 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
