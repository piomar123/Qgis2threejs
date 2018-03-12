# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis3\python\developing_plugins\Qgis2threejs\ui\q3dwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Q3DWindow(object):
    def setupUi(self, Q3DWindow):
        Q3DWindow.setObjectName("Q3DWindow")
        Q3DWindow.resize(757, 580)
        Q3DWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(Q3DWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webView = Q3DView(self.centralwidget)
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        Q3DWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Q3DWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menubar.setObjectName("menubar")
        self.menuScene = QtWidgets.QMenu(self.menubar)
        self.menuScene.setObjectName("menuScene")
        self.menuCamera = QtWidgets.QMenu(self.menuScene)
        self.menuCamera.setObjectName("menuCamera")
        self.menuControls = QtWidgets.QMenu(self.menuScene)
        self.menuControls.setObjectName("menuControls")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuPanels = QtWidgets.QMenu(self.menuWindow)
        self.menuPanels.setObjectName("menuPanels")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Q3DWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Q3DWindow)
        self.statusbar.setObjectName("statusbar")
        Q3DWindow.setStatusBar(self.statusbar)
        self.dockWidgetLayers = QtWidgets.QDockWidget(Q3DWindow)
        self.dockWidgetLayers.setObjectName("dockWidgetLayers")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeView = Q3DTreeView(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setHeaderHidden(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.dockWidgetLayers.setWidget(self.dockWidgetContents)
        Q3DWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetLayers)
        self.toolBar = QtWidgets.QToolBar(Q3DWindow)
        self.toolBar.setObjectName("toolBar")
        Q3DWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidgetConsole = QtWidgets.QDockWidget(Q3DWindow)
        self.dockWidgetConsole.setFloating(False)
        self.dockWidgetConsole.setObjectName("dockWidgetConsole")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidgetDebugView = QtWidgets.QListWidget(self.dockWidgetContents_2)
        self.listWidgetDebugView.setObjectName("listWidgetDebugView")
        self.verticalLayout_3.addWidget(self.listWidgetDebugView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditInputBox = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.lineEditInputBox.setObjectName("lineEditInputBox")
        self.horizontalLayout.addWidget(self.lineEditInputBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.dockWidgetConsole.setWidget(self.dockWidgetContents_2)
        Q3DWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetConsole)
        self.actionSTL_format = QtWidgets.QAction(Q3DWindow)
        self.actionSTL_format.setEnabled(False)
        self.actionSTL_format.setObjectName("actionSTL_format")
        self.actionWorld_Settings = QtWidgets.QAction(Q3DWindow)
        self.actionWorld_Settings.setEnabled(False)
        self.actionWorld_Settings.setObjectName("actionWorld_Settings")
        self.actionPerspective = QtWidgets.QAction(Q3DWindow)
        self.actionPerspective.setCheckable(True)
        self.actionPerspective.setChecked(True)
        self.actionPerspective.setObjectName("actionPerspective")
        self.actionOrthogonal = QtWidgets.QAction(Q3DWindow)
        self.actionOrthogonal.setCheckable(True)
        self.actionOrthogonal.setEnabled(False)
        self.actionOrthogonal.setObjectName("actionOrthogonal")
        self.actionReload = QtWidgets.QAction(Q3DWindow)
        self.actionReload.setObjectName("actionReload")
        self.actionAlwaysOnTop = QtWidgets.QAction(Q3DWindow)
        self.actionAlwaysOnTop.setCheckable(True)
        self.actionAlwaysOnTop.setChecked(False)
        self.actionAlwaysOnTop.setObjectName("actionAlwaysOnTop")
        self.actionExportToWeb = QtWidgets.QAction(Q3DWindow)
        self.actionExportToWeb.setEnabled(True)
        self.actionExportToWeb.setObjectName("actionExportToWeb")
        self.actionSaveAsImage = QtWidgets.QAction(Q3DWindow)
        self.actionSaveAsImage.setObjectName("actionSaveAsImage")
        self.actionResetCameraPosition = QtWidgets.QAction(Q3DWindow)
        self.actionResetCameraPosition.setObjectName("actionResetCameraPosition")
        self.actionOrbit = QtWidgets.QAction(Q3DWindow)
        self.actionOrbit.setCheckable(True)
        self.actionOrbit.setChecked(True)
        self.actionOrbit.setObjectName("actionOrbit")
        self.actionLayer_Panel = QtWidgets.QAction(Q3DWindow)
        self.actionLayer_Panel.setCheckable(True)
        self.actionLayer_Panel.setChecked(True)
        self.actionLayer_Panel.setEnabled(False)
        self.actionLayer_Panel.setObjectName("actionLayer_Panel")
        self.actionClose_Live_Exporter = QtWidgets.QAction(Q3DWindow)
        self.actionClose_Live_Exporter.setObjectName("actionClose_Live_Exporter")
        self.actionPluginSettings = QtWidgets.QAction(Q3DWindow)
        self.actionPluginSettings.setObjectName("actionPluginSettings")
        self.actionHelp = QtWidgets.QAction(Q3DWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuCamera.addAction(self.actionPerspective)
        self.menuCamera.addAction(self.actionOrthogonal)
        self.menuControls.addAction(self.actionOrbit)
        self.menuScene.addAction(self.actionWorld_Settings)
        self.menuScene.addAction(self.menuCamera.menuAction())
        self.menuScene.addAction(self.menuControls.menuAction())
        self.menuScene.addSeparator()
        self.menuScene.addAction(self.actionReload)
        self.menuScene.addSeparator()
        self.menuScene.addAction(self.actionResetCameraPosition)
        self.menuWindow.addAction(self.menuPanels.menuAction())
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionAlwaysOnTop)
        self.menuExport.addAction(self.actionExportToWeb)
        self.menuExport.addAction(self.actionSTL_format)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.actionSaveAsImage)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPluginSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Live_Exporter)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuScene.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExportToWeb)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionResetCameraPosition)
        self.toolBar.addAction(self.actionReload)

        self.retranslateUi(Q3DWindow)
        self.actionClose_Live_Exporter.triggered.connect(Q3DWindow.close)
        QtCore.QMetaObject.connectSlotsByName(Q3DWindow)

    def retranslateUi(self, Q3DWindow):
        _translate = QtCore.QCoreApplication.translate
        Q3DWindow.setWindowTitle(_translate("Q3DWindow", "Live Exporter - Qgis2threejs"))
        self.menuScene.setTitle(_translate("Q3DWindow", "&Scene"))
        self.menuCamera.setTitle(_translate("Q3DWindow", "Camera"))
        self.menuControls.setTitle(_translate("Q3DWindow", "Controls"))
        self.menuWindow.setTitle(_translate("Q3DWindow", "&Window"))
        self.menuPanels.setTitle(_translate("Q3DWindow", "Panels"))
        self.menuFile.setTitle(_translate("Q3DWindow", "&File"))
        self.menuExport.setTitle(_translate("Q3DWindow", "Export"))
        self.menuHelp.setTitle(_translate("Q3DWindow", "&Help"))
        self.dockWidgetLayers.setWindowTitle(_translate("Q3DWindow", "Layers"))
        self.toolBar.setWindowTitle(_translate("Q3DWindow", "toolBar"))
        self.dockWidgetConsole.setWindowTitle(_translate("Q3DWindow", "Console"))
        self.label.setText(_translate("Q3DWindow", ">>>"))
        self.actionSTL_format.setText(_translate("Q3DWindow", "Export as STL format..."))
        self.actionWorld_Settings.setText(_translate("Q3DWindow", "World Settings..."))
        self.actionPerspective.setText(_translate("Q3DWindow", "Perspective"))
        self.actionOrthogonal.setText(_translate("Q3DWindow", "Orthographic"))
        self.actionReload.setText(_translate("Q3DWindow", "Reload"))
        self.actionReload.setShortcut(_translate("Q3DWindow", "F5"))
        self.actionAlwaysOnTop.setText(_translate("Q3DWindow", "Always on Top"))
        self.actionExportToWeb.setText(_translate("Q3DWindow", "Export to Web..."))
        self.actionSaveAsImage.setText(_translate("Q3DWindow", "Save Scene as Image..."))
        self.actionResetCameraPosition.setText(_translate("Q3DWindow", "Reset Camera Position"))
        self.actionResetCameraPosition.setShortcut(_translate("Q3DWindow", "Shift+R"))
        self.actionOrbit.setText(_translate("Q3DWindow", "Orbit"))
        self.actionLayer_Panel.setText(_translate("Q3DWindow", "Layer Panel"))
        self.actionClose_Live_Exporter.setText(_translate("Q3DWindow", "Close Live Exporter"))
        self.actionPluginSettings.setText(_translate("Q3DWindow", "Plugin Settings.."))
        self.actionHelp.setText(_translate("Q3DWindow", "&Help"))

from Qgis2threejs.q3dtreeview import Q3DTreeView
from Qgis2threejs.q3dview import Q3DView
