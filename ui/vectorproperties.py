# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis3\python\developing_plugins\Qgis2threejs\ui\vectorproperties.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VectorPropertiesWidget(object):
    def setupUi(self, VectorPropertiesWidget):
        VectorPropertiesWidget.setObjectName("VectorPropertiesWidget")
        VectorPropertiesWidget.resize(354, 481)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(VectorPropertiesWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setContentsMargins(8, -1, 6, -1)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_ObjectType = QtWidgets.QLabel(VectorPropertiesWidget)
        self.label_ObjectType.setMinimumSize(QtCore.QSize(50, 0))
        self.label_ObjectType.setObjectName("label_ObjectType")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_ObjectType)
        self.comboBox_ObjectType = QtWidgets.QComboBox(VectorPropertiesWidget)
        self.comboBox_ObjectType.setObjectName("comboBox_ObjectType")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_ObjectType)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.label_ObjectTypeMessage = QtWidgets.QLabel(VectorPropertiesWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_ObjectTypeMessage.setFont(font)
        self.label_ObjectTypeMessage.setStyleSheet("font-weight: bold;")
        self.label_ObjectTypeMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ObjectTypeMessage.setWordWrap(True)
        self.label_ObjectTypeMessage.setObjectName("label_ObjectTypeMessage")
        self.verticalLayout_2.addWidget(self.label_ObjectTypeMessage)
        self.groupBox_zCoordinate = QtWidgets.QGroupBox(VectorPropertiesWidget)
        self.groupBox_zCoordinate.setObjectName("groupBox_zCoordinate")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_zCoordinate)
        self.verticalLayout_6.setContentsMargins(9, 3, 9, 3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_zCoordinate)
        self.label_2.setMinimumSize(QtCore.QSize(46, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.radioButton_zValue = QtWidgets.QRadioButton(self.groupBox_zCoordinate)
        self.radioButton_zValue.setObjectName("radioButton_zValue")
        self.buttonGroup_altitude = QtWidgets.QButtonGroup(VectorPropertiesWidget)
        self.buttonGroup_altitude.setObjectName("buttonGroup_altitude")
        self.buttonGroup_altitude.addButton(self.radioButton_zValue)
        self.horizontalLayout_2.addWidget(self.radioButton_zValue)
        self.radioButton_mValue = QtWidgets.QRadioButton(self.groupBox_zCoordinate)
        self.radioButton_mValue.setObjectName("radioButton_mValue")
        self.buttonGroup_altitude.addButton(self.radioButton_mValue)
        self.horizontalLayout_2.addWidget(self.radioButton_mValue)
        self.radioButton_Expression = QtWidgets.QRadioButton(self.groupBox_zCoordinate)
        self.radioButton_Expression.setChecked(True)
        self.radioButton_Expression.setObjectName("radioButton_Expression")
        self.buttonGroup_altitude.addButton(self.radioButton_Expression)
        self.horizontalLayout_2.addWidget(self.radioButton_Expression)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, -1, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.label_zExpression = QtWidgets.QLabel(self.groupBox_zCoordinate)
        self.label_zExpression.setMinimumSize(QtCore.QSize(46, 0))
        self.label_zExpression.setObjectName("label_zExpression")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_zExpression)
        self.fieldExpressionWidget_altitude = QgsFieldExpressionWidget(self.groupBox_zCoordinate)
        self.fieldExpressionWidget_altitude.setMinimumSize(QtCore.QSize(0, 20))
        self.fieldExpressionWidget_altitude.setObjectName("fieldExpressionWidget_altitude")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fieldExpressionWidget_altitude)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_zCoordinate)
        self.label_3.setMinimumSize(QtCore.QSize(46, 0))
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_altitudeMode = QtWidgets.QComboBox(self.groupBox_zCoordinate)
        self.comboBox_altitudeMode.setObjectName("comboBox_altitudeMode")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_altitudeMode)
        self.verticalLayout_6.addLayout(self.formLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox_zCoordinate)
        self.groupBox_Styles = QtWidgets.QGroupBox(VectorPropertiesWidget)
        self.groupBox_Styles.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_Styles.setObjectName("groupBox_Styles")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_Styles)
        self.gridLayout_8.setContentsMargins(9, 3, 9, 3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_Styles = QtWidgets.QVBoxLayout()
        self.verticalLayout_Styles.setObjectName("verticalLayout_Styles")
        self.gridLayout_8.addLayout(self.verticalLayout_Styles, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_Styles)
        self.groupBox_Features = QtWidgets.QGroupBox(VectorPropertiesWidget)
        self.groupBox_Features.setObjectName("groupBox_Features")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_Features)
        self.verticalLayout_3.setContentsMargins(9, 3, 9, 3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_AllFeatures = QtWidgets.QRadioButton(self.groupBox_Features)
        self.radioButton_AllFeatures.setObjectName("radioButton_AllFeatures")
        self.verticalLayout_3.addWidget(self.radioButton_AllFeatures)
        self.radioButton_IntersectingFeatures = QtWidgets.QRadioButton(self.groupBox_Features)
        self.radioButton_IntersectingFeatures.setChecked(True)
        self.radioButton_IntersectingFeatures.setObjectName("radioButton_IntersectingFeatures")
        self.verticalLayout_3.addWidget(self.radioButton_IntersectingFeatures)
        self.verticalLayout_Feature = QtWidgets.QVBoxLayout()
        self.verticalLayout_Feature.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_Feature.setObjectName("verticalLayout_Feature")
        self.checkBox_Clip = QtWidgets.QCheckBox(self.groupBox_Features)
        self.checkBox_Clip.setChecked(True)
        self.checkBox_Clip.setObjectName("checkBox_Clip")
        self.verticalLayout_Feature.addWidget(self.checkBox_Clip)
        self.verticalLayout_3.addLayout(self.verticalLayout_Feature)
        self.verticalLayout_2.addWidget(self.groupBox_Features)
        self.groupBox_Attrs = QtWidgets.QGroupBox(VectorPropertiesWidget)
        self.groupBox_Attrs.setObjectName("groupBox_Attrs")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_Attrs)
        self.verticalLayout_4.setContentsMargins(9, 3, 9, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_ExportAttrs = QtWidgets.QCheckBox(self.groupBox_Attrs)
        self.checkBox_ExportAttrs.setChecked(False)
        self.checkBox_ExportAttrs.setObjectName("checkBox_ExportAttrs")
        self.verticalLayout_4.addWidget(self.checkBox_ExportAttrs)
        self.formLayout_Label = QtWidgets.QFormLayout()
        self.formLayout_Label.setContentsMargins(2, -1, 2, -1)
        self.formLayout_Label.setObjectName("formLayout_Label")
        self.label = QtWidgets.QLabel(self.groupBox_Attrs)
        self.label.setEnabled(False)
        self.label.setMinimumSize(QtCore.QSize(76, 0))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_Label.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_Label = QtWidgets.QComboBox(self.groupBox_Attrs)
        self.comboBox_Label.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Label.sizePolicy().hasHeightForWidth())
        self.comboBox_Label.setSizePolicy(sizePolicy)
        self.comboBox_Label.setMaximumSize(QtCore.QSize(270, 16777215))
        self.comboBox_Label.setObjectName("comboBox_Label")
        self.formLayout_Label.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_Label)
        self.verticalLayout_4.addLayout(self.formLayout_Label)
        self.verticalLayout_Label = QtWidgets.QVBoxLayout()
        self.verticalLayout_Label.setObjectName("verticalLayout_Label")
        self.verticalLayout_4.addLayout(self.verticalLayout_Label)
        self.verticalLayout_2.addWidget(self.groupBox_Attrs)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(VectorPropertiesWidget)
        self.radioButton_IntersectingFeatures.toggled['bool'].connect(self.checkBox_Clip.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(VectorPropertiesWidget)

    def retranslateUi(self, VectorPropertiesWidget):
        _translate = QtCore.QCoreApplication.translate
        VectorPropertiesWidget.setWindowTitle(_translate("VectorPropertiesWidget", "Form"))
        self.label_ObjectType.setText(_translate("VectorPropertiesWidget", "Object type"))
        self.label_ObjectTypeMessage.setText(_translate("VectorPropertiesWidget", "This type is experimental. Some 3D model files fail to be loaded."))
        self.groupBox_zCoordinate.setTitle(_translate("VectorPropertiesWidget", "&Z coordinate"))
        self.label_2.setText(_translate("VectorPropertiesWidget", "Altitude"))
        self.radioButton_zValue.setText(_translate("VectorPropertiesWidget", "Z Value"))
        self.radioButton_mValue.setText(_translate("VectorPropertiesWidget", "M Value"))
        self.radioButton_Expression.setText(_translate("VectorPropertiesWidget", "Expression"))
        self.label_3.setText(_translate("VectorPropertiesWidget", "Mode"))
        self.groupBox_Styles.setTitle(_translate("VectorPropertiesWidget", "&Style"))
        self.groupBox_Features.setTitle(_translate("VectorPropertiesWidget", "&Feature"))
        self.radioButton_AllFeatures.setText(_translate("VectorPropertiesWidget", "All features"))
        self.radioButton_IntersectingFeatures.setText(_translate("VectorPropertiesWidget", "Features that intersect with map canvas extent"))
        self.checkBox_Clip.setText(_translate("VectorPropertiesWidget", "Clip geometries"))
        self.groupBox_Attrs.setTitle(_translate("VectorPropertiesWidget", "&Attribute and label"))
        self.checkBox_ExportAttrs.setText(_translate("VectorPropertiesWidget", "Export attributes"))
        self.label.setText(_translate("VectorPropertiesWidget", "Label field"))

from qgis.gui import QgsFieldExpressionWidget
