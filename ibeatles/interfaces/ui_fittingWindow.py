# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/ui_fittingWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1218, 773)
        MainWindow.setMinimumSize(QtCore.QSize(300, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.rightFrame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightFrame.sizePolicy().hasHeightForWidth())
        self.rightFrame.setSizePolicy(sizePolicy)
        self.rightFrame.setMinimumSize(QtCore.QSize(300, 400))
        self.rightFrame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.rightFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.rightFrame.setObjectName(_fromUtf8("rightFrame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.rightFrame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.toolBox = QtGui.QToolBox(self.rightFrame)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 254, 227))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.material_groupBox = QtGui.QGroupBox(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.material_groupBox.sizePolicy().hasHeightForWidth())
        self.material_groupBox.setSizePolicy(sizePolicy)
        self.material_groupBox.setTitle(_fromUtf8(""))
        self.material_groupBox.setObjectName(_fromUtf8("material_groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.material_groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.material_groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.hkl_list_ui = QtGui.QComboBox(self.material_groupBox)
        self.hkl_list_ui.setMinimumSize(QtCore.QSize(100, 0))
        self.hkl_list_ui.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hkl_list_ui.setObjectName(_fromUtf8("hkl_list_ui"))
        self.horizontalLayout.addWidget(self.hkl_list_ui)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.material_groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(75, 0))
        self.label_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.bragg_edge_calculated = QtGui.QLabel(self.material_groupBox)
        self.bragg_edge_calculated.setMinimumSize(QtCore.QSize(50, 0))
        self.bragg_edge_calculated.setMaximumSize(QtCore.QSize(50, 16777215))
        self.bragg_edge_calculated.setObjectName(_fromUtf8("bragg_edge_calculated"))
        self.horizontalLayout_2.addWidget(self.bragg_edge_calculated)
        self.bragg_edge_units = QtGui.QLabel(self.material_groupBox)
        self.bragg_edge_units.setObjectName(_fromUtf8("bragg_edge_units"))
        self.horizontalLayout_2.addWidget(self.bragg_edge_units)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addWidget(self.material_groupBox)
        self.lambda_range_selected = QtGui.QGroupBox(self.page)
        self.lambda_range_selected.setObjectName(_fromUtf8("lambda_range_selected"))
        self.gridLayout = QtGui.QGridLayout(self.lambda_range_selected)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lambda_min_label = QtGui.QLabel(self.lambda_range_selected)
        self.lambda_min_label.setObjectName(_fromUtf8("lambda_min_label"))
        self.gridLayout.addWidget(self.lambda_min_label, 0, 0, 1, 1)
        self.lambda_min_lineEdit = QtGui.QLineEdit(self.lambda_range_selected)
        self.lambda_min_lineEdit.setObjectName(_fromUtf8("lambda_min_lineEdit"))
        self.gridLayout.addWidget(self.lambda_min_lineEdit, 0, 1, 1, 1)
        self.lambda_min_units = QtGui.QLabel(self.lambda_range_selected)
        self.lambda_min_units.setObjectName(_fromUtf8("lambda_min_units"))
        self.gridLayout.addWidget(self.lambda_min_units, 0, 2, 1, 1)
        self.lambda_max_label = QtGui.QLabel(self.lambda_range_selected)
        self.lambda_max_label.setObjectName(_fromUtf8("lambda_max_label"))
        self.gridLayout.addWidget(self.lambda_max_label, 1, 0, 1, 1)
        self.lambda_max_lineEdit = QtGui.QLineEdit(self.lambda_range_selected)
        self.lambda_max_lineEdit.setObjectName(_fromUtf8("lambda_max_lineEdit"))
        self.gridLayout.addWidget(self.lambda_max_lineEdit, 1, 1, 1, 1)
        self.lambda_max_units = QtGui.QLabel(self.lambda_range_selected)
        self.lambda_max_units.setObjectName(_fromUtf8("lambda_max_units"))
        self.gridLayout.addWidget(self.lambda_max_units, 1, 2, 1, 1)
        self.verticalLayout_7.addWidget(self.lambda_range_selected)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 274, 312))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.step1_step2_instructions_label = QtGui.QTextEdit(self.page_2)
        self.step1_step2_instructions_label.setEnabled(False)
        self.step1_step2_instructions_label.setMinimumSize(QtCore.QSize(0, 50))
        self.step1_step2_instructions_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.step1_step2_instructions_label.setReadOnly(True)
        self.step1_step2_instructions_label.setObjectName(_fromUtf8("step1_step2_instructions_label"))
        self.verticalLayout_6.addWidget(self.step1_step2_instructions_label)
        self.instructions_step1_button = QtGui.QPushButton(self.page_2)
        self.instructions_step1_button.setEnabled(False)
        self.instructions_step1_button.setObjectName(_fromUtf8("instructions_step1_button"))
        self.verticalLayout_6.addWidget(self.instructions_step1_button)
        self.step4_groupBox = QtGui.QGroupBox(self.page_2)
        self.step4_groupBox.setEnabled(False)
        self.step4_groupBox.setObjectName(_fromUtf8("step4_groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.step4_groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.fit_table_active_cell_button = QtGui.QPushButton(self.step4_groupBox)
        self.fit_table_active_cell_button.setEnabled(False)
        self.fit_table_active_cell_button.setObjectName(_fromUtf8("fit_table_active_cell_button"))
        self.verticalLayout_2.addWidget(self.fit_table_active_cell_button)
        self.label_4 = QtGui.QLabel(self.step4_groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.create_fitting_story_button = QtGui.QPushButton(self.step4_groupBox)
        self.create_fitting_story_button.setObjectName(_fromUtf8("create_fitting_story_button"))
        self.verticalLayout_2.addWidget(self.create_fitting_story_button)
        self.verticalLayout_6.addWidget(self.step4_groupBox)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.toolBox)
        self.bottomFrame = QtGui.QFrame(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomFrame.sizePolicy().hasHeightForWidth())
        self.bottomFrame.setSizePolicy(sizePolicy)
        self.bottomFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.bottomFrame.setObjectName(_fromUtf8("bottomFrame"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.bottomFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.bottomFrame)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.show_all_bins = QtGui.QRadioButton(self.groupBox_2)
        self.show_all_bins.setChecked(True)
        self.show_all_bins.setObjectName(_fromUtf8("show_all_bins"))
        self.horizontalLayout_5.addWidget(self.show_all_bins)
        self.show_only_active_bins = QtGui.QRadioButton(self.groupBox_2)
        self.show_only_active_bins.setObjectName(_fromUtf8("show_only_active_bins"))
        self.horizontalLayout_5.addWidget(self.show_only_active_bins)
        self.show_only_lock_bins = QtGui.QRadioButton(self.groupBox_2)
        self.show_only_lock_bins.setObjectName(_fromUtf8("show_only_lock_bins"))
        self.horizontalLayout_5.addWidget(self.show_only_lock_bins)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.advanced_table_checkBox = QtGui.QCheckBox(self.bottomFrame)
        self.advanced_table_checkBox.setEnabled(True)
        self.advanced_table_checkBox.setChecked(False)
        self.advanced_table_checkBox.setObjectName(_fromUtf8("advanced_table_checkBox"))
        self.horizontalLayout_4.addWidget(self.advanced_table_checkBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.header_table = QtGui.QTableWidget(self.bottomFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_table.sizePolicy().hasHeightForWidth())
        self.header_table.setSizePolicy(sizePolicy)
        self.header_table.setMinimumSize(QtCore.QSize(1180, 0))
        self.header_table.setMaximumSize(QtCore.QSize(1180, 22))
        self.header_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.header_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.header_table.setAutoScroll(True)
        self.header_table.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.header_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectColumns)
        self.header_table.setCornerButtonEnabled(True)
        self.header_table.setObjectName(_fromUtf8("header_table"))
        self.header_table.setColumnCount(13)
        self.header_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.header_table.setHorizontalHeaderItem(12, item)
        self.header_table.horizontalHeader().setVisible(True)
        self.header_table.horizontalHeader().setHighlightSections(True)
        self.header_table.horizontalHeader().setStretchLastSection(False)
        self.header_table.verticalHeader().setVisible(False)
        self.header_table.verticalHeader().setHighlightSections(False)
        self.header_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.header_table)
        self.value_table = QtGui.QTableWidget(self.bottomFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_table.sizePolicy().hasHeightForWidth())
        self.value_table.setSizePolicy(sizePolicy)
        self.value_table.setMinimumSize(QtCore.QSize(1180, 0))
        self.value_table.setMaximumSize(QtCore.QSize(1180, 16777215))
        self.value_table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.value_table.setFrameShadow(QtGui.QFrame.Sunken)
        self.value_table.setLineWidth(1)
        self.value_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.value_table.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.value_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectColumns)
        self.value_table.setObjectName(_fromUtf8("value_table"))
        self.value_table.setColumnCount(21)
        self.value_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.value_table.setHorizontalHeaderItem(20, item)
        self.value_table.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.value_table)
        self.verticalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        QtCore.QObject.connect(self.hkl_list_ui, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), MainWindow.hkl_list_changed)
        QtCore.QObject.connect(self.value_table, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), MainWindow.value_table_right_click)
        QtCore.QObject.connect(self.value_table, QtCore.SIGNAL(_fromUtf8("cellClicked(int,int)")), MainWindow.selection_in_value_table_of_rows_cell_clicked)
        QtCore.QObject.connect(self.value_table, QtCore.SIGNAL(_fromUtf8("itemSelectionChanged()")), MainWindow.selection_in_value_table_changed)
        QtCore.QObject.connect(self.advanced_table_checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), MainWindow.advanced_table_clicked)
        QtCore.QObject.connect(self.show_all_bins, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.update_table)
        QtCore.QObject.connect(self.show_only_active_bins, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.update_table)
        QtCore.QObject.connect(self.show_only_lock_bins, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.update_table)
        QtCore.QObject.connect(self.instructions_step1_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.initialize_all_parameters_button_clicked)
        QtCore.QObject.connect(self.lambda_min_lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), MainWindow.min_or_max_lambda_manually_changed)
        QtCore.QObject.connect(self.lambda_max_lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), MainWindow.min_or_max_lambda_manually_changed)
        QtCore.QObject.connect(self.fit_table_active_cell_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.fit_table_active_cell_checked)
        QtCore.QObject.connect(self.create_fitting_story_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.create_fitting_story_checked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "h,k,l", None))
        self.label_2.setText(_translate("MainWindow", "calculated", None))
        self.bragg_edge_calculated.setText(_translate("MainWindow", "N/A", None))
        self.bragg_edge_units.setText(_translate("MainWindow", "A", None))
        self.lambda_range_selected.setTitle(_translate("MainWindow", "Range Selected", None))
        self.lambda_min_label.setText(_translate("MainWindow", "Lambda min", None))
        self.lambda_min_units.setText(_translate("MainWindow", "A", None))
        self.lambda_max_label.setText(_translate("MainWindow", "Lambda max", None))
        self.lambda_max_units.setText(_translate("MainWindow", "A", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Bragg Edge Infos", None))
        self.step1_step2_instructions_label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">step1 - makes all bins <span style=\" font-weight:600;\">active</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">step2 -<span style=\" font-weight:600;\"> </span>selects Bragg Edge peak</p></body></html>", None))
        self.instructions_step1_button.setToolTip(_translate("MainWindow", "Program determines inital guess value of parameters and fits data using 1 global bin", None))
        self.instructions_step1_button.setText(_translate("MainWindow", "step3 - Initialize All Parameters", None))
        self.step4_groupBox.setTitle(_translate("MainWindow", "step4", None))
        self.fit_table_active_cell_button.setText(_translate("MainWindow", "Fit Table Active Cell", None))
        self.label_4.setText(_translate("MainWindow", "or", None))
        self.create_fitting_story_button.setText(_translate("MainWindow", "Create Fitting Story ...", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Fitting Instructions", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Bins To Display", None))
        self.show_all_bins.setText(_translate("MainWindow", "Show All", None))
        self.show_only_active_bins.setText(_translate("MainWindow", "Show Only Active", None))
        self.show_only_lock_bins.setText(_translate("MainWindow", "Show Only Lock", None))
        self.advanced_table_checkBox.setText(_translate("MainWindow", "Advanced Fitting", None))
        item = self.header_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Row", None))
        item = self.header_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Col", None))
        item = self.header_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lock", None))
        item = self.header_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Active", None))
        item = self.header_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fitting Confidence", None))
        item = self.header_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "D-spacing", None))
        item = self.header_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sigma", None))
        item = self.header_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Alpha", None))
        item = self.header_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "A1", None))
        item = self.header_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "A2", None))
        item = self.header_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "A5", None))
        item = self.header_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "A6", None))
        item = self.header_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Intensity", None))
        item = self.value_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "Err.", None))
        item = self.value_table.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "Val.", None))
        item = self.value_table.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "Err.", None))

import icons_rc
