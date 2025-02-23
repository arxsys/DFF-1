# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vertrex/dff-pro/dff/ui/gui/resources/sqlitemanager.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_SQLiteManager(object):
    def setupUi(self, SQLiteManager):
        SQLiteManager.setObjectName(_fromUtf8("SQLiteManager"))
        SQLiteManager.resize(933, 526)
        self.verticalLayout_4 = QtGui.QVBoxLayout(SQLiteManager)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(SQLiteManager)
        self.splitter.setFrameShadow(QtGui.QFrame.Plain)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.databaseTree = QtGui.QTreeWidget(self.layoutWidget)
        self.databaseTree.setObjectName(_fromUtf8("databaseTree"))
        self.databaseTree.header().setVisible(True)
        self.verticalLayout_2.addWidget(self.databaseTree)
        self.refreshButton = QtGui.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshButton.setIcon(icon)
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.verticalLayout_2.addWidget(self.refreshButton)
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.t = QtGui.QVBoxLayout(self.tab_3)
        self.t.setMargin(0)
        self.t.setObjectName(_fromUtf8("t"))
        self.tableResultLayout = QtGui.QVBoxLayout()
        self.tableResultLayout.setObjectName(_fromUtf8("tableResultLayout"))
        self.t.addLayout(self.tableResultLayout)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.queryEdit = QtGui.QTextEdit(self.tab_4)
        self.queryEdit.setObjectName(_fromUtf8("queryEdit"))
        self.verticalLayout_5.addWidget(self.queryEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.queryRun = QtGui.QPushButton(self.tab_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/tasks")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.queryRun.setIcon(icon1)
        self.queryRun.setObjectName(_fromUtf8("queryRun"))
        self.horizontalLayout.addWidget(self.queryRun)
        self.selectDatabase = QtGui.QComboBox(self.tab_4)
        self.selectDatabase.setObjectName(_fromUtf8("selectDatabase"))
        self.horizontalLayout.addWidget(self.selectDatabase)
        self.horizontalLayout.setStretch(1, 70)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.customStack = QtGui.QStackedWidget(self.tab_4)
        self.customStack.setObjectName(_fromUtf8("customStack"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.customResultLayout = QtGui.QVBoxLayout()
        self.customResultLayout.setObjectName(_fromUtf8("customResultLayout"))
        self.horizontalLayout_2.addLayout(self.customResultLayout)
        self.customStack.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.queryMessage = QtGui.QTextEdit(self.page_2)
        self.queryMessage.setObjectName(_fromUtf8("queryMessage"))
        self.horizontalLayout_3.addWidget(self.queryMessage)
        self.customStack.addWidget(self.page_2)
        self.verticalLayout_5.addWidget(self.customStack)
        self.verticalLayout_5.setStretch(0, 20)
        self.verticalLayout_5.setStretch(2, 80)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.schemaTable = QtGui.QTableWidget(self.tab_5)
        self.schemaTable.setObjectName(_fromUtf8("schemaTable"))
        self.schemaTable.setColumnCount(6)
        self.schemaTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.schemaTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.schemaTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.schemaTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.schemaTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.schemaTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.schemaTable.setHorizontalHeaderItem(5, item)
        self.schemaTable.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.schemaTable)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.actionExport_selection_CSV = QtGui.QAction(SQLiteManager)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/extract.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_selection_CSV.setIcon(icon2)
        self.actionExport_selection_CSV.setObjectName(_fromUtf8("actionExport_selection_CSV"))
        self.actionExtract_Binary_BLOB = QtGui.QAction(SQLiteManager)
        self.actionExtract_Binary_BLOB.setIcon(icon2)
        self.actionExtract_Binary_BLOB.setObjectName(_fromUtf8("actionExtract_Binary_BLOB"))
        self.actionDecode_date_column = QtGui.QAction(SQLiteManager)
        self.actionDecode_date_column.setObjectName(_fromUtf8("actionDecode_date_column"))
        self.actionReset_column = QtGui.QAction(SQLiteManager)
        self.actionReset_column.setObjectName(_fromUtf8("actionReset_column"))

        self.retranslateUi(SQLiteManager)
        self.tabWidget.setCurrentIndex(0)
        self.customStack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SQLiteManager)

    def retranslateUi(self, SQLiteManager):
        SQLiteManager.setWindowTitle(_translate("SQLiteManager", "Form", None))
        self.databaseTree.headerItem().setText(0, _translate("SQLiteManager", "Database(s)", None))
        self.refreshButton.setText(_translate("SQLiteManager", "Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SQLiteManager", "Browse table", None))
        self.queryRun.setText(_translate("SQLiteManager", "Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("SQLiteManager", "Custom query", None))
        item = self.schemaTable.horizontalHeaderItem(0)
        item.setText(_translate("SQLiteManager", "ID", None))
        item = self.schemaTable.horizontalHeaderItem(1)
        item.setText(_translate("SQLiteManager", "Name", None))
        item = self.schemaTable.horizontalHeaderItem(2)
        item.setText(_translate("SQLiteManager", "Type", None))
        item = self.schemaTable.horizontalHeaderItem(3)
        item.setText(_translate("SQLiteManager", "Not Null", None))
        item = self.schemaTable.horizontalHeaderItem(4)
        item.setText(_translate("SQLiteManager", "Default", None))
        item = self.schemaTable.horizontalHeaderItem(5)
        item.setText(_translate("SQLiteManager", "PK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("SQLiteManager", "Schema", None))
        self.actionExport_selection_CSV.setText(_translate("SQLiteManager", "Export selection (CSV)", None))
        self.actionExport_selection_CSV.setToolTip(_translate("SQLiteManager", "Export selection to CSV", None))
        self.actionExtract_Binary_BLOB.setText(_translate("SQLiteManager", "Extract Binary (BLOB)", None))
        self.actionDecode_date_column.setText(_translate("SQLiteManager", "Decode date (column)", None))
        self.actionReset_column.setText(_translate("SQLiteManager", "Reset column", None))

import gui_rc
