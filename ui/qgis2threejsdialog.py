# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis2\python\developing_plugins\Qgis2threejs\ui\qgis2threejsdialog.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Qgis2threejsDialog(object):
    def setupUi(self, Qgis2threejsDialog):
        Qgis2threejsDialog.setObjectName("Qgis2threejsDialog")
        Qgis2threejsDialog.resize(720, 513)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Qgis2threejsDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(Qgis2threejsDialog)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_Template = QtWidgets.QComboBox(Qgis2threejsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Template.sizePolicy().hasHeightForWidth())
        self.comboBox_Template.setSizePolicy(sizePolicy)
        self.comboBox_Template.setObjectName("comboBox_Template")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_Template)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.splitter = QtWidgets.QSplitter(Qgis2threejsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(150, 0))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(300, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 439, 388))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.propertyPagesContainer = QtWidgets.QVBoxLayout()
        self.propertyPagesContainer.setObjectName("propertyPagesContainer")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setStyleSheet("background-color:rgba(0, 0, 0, 0);")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.propertyPagesContainer.addWidget(self.textBrowser)
        self.gridLayout_13.addLayout(self.propertyPagesContainer, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.splitter)
        self.label_3 = QtWidgets.QLabel(Qgis2threejsDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_OutputFilename = QtWidgets.QLineEdit(Qgis2threejsDialog)
        self.lineEdit_OutputFilename.setObjectName("lineEdit_OutputFilename")
        self.horizontalLayout_2.addWidget(self.lineEdit_OutputFilename)
        self.toolButton_Browse = QtWidgets.QToolButton(Qgis2threejsDialog)
        self.toolButton_Browse.setObjectName("toolButton_Browse")
        self.horizontalLayout_2.addWidget(self.toolButton_Browse)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.toolButton_Settings = QtWidgets.QToolButton(Qgis2threejsDialog)
        self.toolButton_Settings.setObjectName("toolButton_Settings")
        self.horizontalLayout_7.addWidget(self.toolButton_Settings)
        self.progressBar = QtWidgets.QProgressBar(Qgis2threejsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_7.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_MessageIcon = QtWidgets.QLabel(Qgis2threejsDialog)
        self.label_MessageIcon.setMaximumSize(QtCore.QSize(32, 32))
        self.label_MessageIcon.setText("")
        self.label_MessageIcon.setObjectName("label_MessageIcon")
        self.horizontalLayout.addWidget(self.label_MessageIcon)
        self.label_Status = QtWidgets.QLabel(Qgis2threejsDialog)
        self.label_Status.setText("")
        self.label_Status.setObjectName("label_Status")
        self.horizontalLayout.addWidget(self.label_Status)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        self.pushButton_Run = QtWidgets.QPushButton(Qgis2threejsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Run.sizePolicy().hasHeightForWidth())
        self.pushButton_Run.setSizePolicy(sizePolicy)
        self.pushButton_Run.setDefault(True)
        self.pushButton_Run.setObjectName("pushButton_Run")
        self.horizontalLayout_7.addWidget(self.pushButton_Run)
        self.pushButton_Close = QtWidgets.QPushButton(Qgis2threejsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Close.sizePolicy().hasHeightForWidth())
        self.pushButton_Close.setSizePolicy(sizePolicy)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.horizontalLayout_7.addWidget(self.pushButton_Close)
        self.pushButton_Help = QtWidgets.QPushButton(Qgis2threejsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Help.sizePolicy().hasHeightForWidth())
        self.pushButton_Help.setSizePolicy(sizePolicy)
        self.pushButton_Help.setObjectName("pushButton_Help")
        self.horizontalLayout_7.addWidget(self.pushButton_Help)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Qgis2threejsDialog)
        QtCore.QMetaObject.connectSlotsByName(Qgis2threejsDialog)

    def retranslateUi(self, Qgis2threejsDialog):
        _translate = QtCore.QCoreApplication.translate
        Qgis2threejsDialog.setWindowTitle(_translate("Qgis2threejsDialog", "Qgis2threejs"))
        self.label.setText(_translate("Qgis2threejsDialog", "Template file"))
        self.label_3.setText(_translate("Qgis2threejsDialog", "Output HTML file path"))
        self.toolButton_Browse.setText(_translate("Qgis2threejsDialog", "Browse..."))
        self.toolButton_Settings.setText(_translate("Qgis2threejsDialog", "..."))
        self.progressBar.setFormat(_translate("Qgis2threejsDialog", "%p%"))
        self.pushButton_Run.setText(_translate("Qgis2threejsDialog", "Run"))
        self.pushButton_Close.setText(_translate("Qgis2threejsDialog", "Close"))
        self.pushButton_Help.setToolTip(_translate("Qgis2threejsDialog", "Open local help file with default browser."))
        self.pushButton_Help.setText(_translate("Qgis2threejsDialog", "Help"))

