# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window-tab.ui'
#
# Created: Mon Oct 30 14:58:17 2017
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

### For use with capow.py - calculation and plotting of optimised weights

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
        MainWindow.resize(1220, 928)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1201, 871))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.normal_plot_tab = QtGui.QWidget()
        self.normal_plot_tab.setObjectName(_fromUtf8("normal_plot_tab"))
        self.layoutWidget = QtGui.QWidget(self.normal_plot_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1178, 811))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.a_edit = QtGui.QLineEdit(self.layoutWidget)
        self.a_edit.setObjectName(_fromUtf8("a_edit"))
        self.horizontalLayout.addWidget(self.a_edit)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.b_edit = QtGui.QLineEdit(self.layoutWidget)
        self.b_edit.setObjectName(_fromUtf8("b_edit"))
        self.horizontalLayout.addWidget(self.b_edit)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.c_edit = QtGui.QLineEdit(self.layoutWidget)
        self.c_edit.setObjectName(_fromUtf8("c_edit"))
        self.horizontalLayout.addWidget(self.c_edit)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.d_edit = QtGui.QLineEdit(self.layoutWidget)
        self.d_edit.setObjectName(_fromUtf8("d_edit"))
        self.horizontalLayout.addWidget(self.d_edit)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.e_edit = QtGui.QLineEdit(self.layoutWidget)
        self.e_edit.setObjectName(_fromUtf8("e_edit"))
        self.horizontalLayout.addWidget(self.e_edit)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.f_edit = QtGui.QLineEdit(self.layoutWidget)
        self.f_edit.setObjectName(_fromUtf8("f_edit"))
        self.horizontalLayout.addWidget(self.f_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.mplwindow = QtGui.QWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow.sizePolicy().hasHeightForWidth())
        self.mplwindow.setSizePolicy(sizePolicy)
        self.mplwindow.setMinimumSize(QtCore.QSize(766, 766))
        self.mplwindow.setObjectName(_fromUtf8("mplwindow"))
        self.mplvl = QtGui.QVBoxLayout(self.mplwindow)
        self.mplvl.setMargin(0)
        self.mplvl.setObjectName(_fromUtf8("mplvl"))
        self.horizontalLayout_2.addWidget(self.mplwindow)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.resoln_lower_eq = QtGui.QComboBox(self.layoutWidget)
        self.resoln_lower_eq.setMaximumSize(QtCore.QSize(55, 16777215))
        self.resoln_lower_eq.setObjectName(_fromUtf8("resoln_lower_eq"))
        self.gridLayout_2.addWidget(self.resoln_lower_eq, 4, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 2)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(180, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)
        self.i_sig_filt = QtGui.QLineEdit(self.layoutWidget)
        self.i_sig_filt.setMaximumSize(QtCore.QSize(200, 16777215))
        self.i_sig_filt.setObjectName(_fromUtf8("i_sig_filt"))
        self.gridLayout_2.addWidget(self.i_sig_filt, 1, 3, 1, 1)
        self.i_filt = QtGui.QLineEdit(self.layoutWidget)
        self.i_filt.setMaximumSize(QtCore.QSize(200, 16777215))
        self.i_filt.setObjectName(_fromUtf8("i_filt"))
        self.gridLayout_2.addWidget(self.i_filt, 0, 3, 1, 1)
        self.i_filt_eq = QtGui.QComboBox(self.layoutWidget)
        self.i_filt_eq.setMaximumSize(QtCore.QSize(55, 16777215))
        self.i_filt_eq.setObjectName(_fromUtf8("i_filt_eq"))
        self.gridLayout_2.addWidget(self.i_filt_eq, 0, 2, 1, 1)
        self.i_sig_filt_eq = QtGui.QComboBox(self.layoutWidget)
        self.i_sig_filt_eq.setMaximumSize(QtCore.QSize(55, 16777215))
        self.i_sig_filt_eq.setObjectName(_fromUtf8("i_sig_filt_eq"))
        self.gridLayout_2.addWidget(self.i_sig_filt_eq, 1, 2, 1, 1)
        self.resoln_upper_eq = QtGui.QComboBox(self.layoutWidget)
        self.resoln_upper_eq.setMaximumSize(QtCore.QSize(55, 16777215))
        self.resoln_upper_eq.setObjectName(_fromUtf8("resoln_upper_eq"))
        self.gridLayout_2.addWidget(self.resoln_upper_eq, 2, 2, 1, 1)
        self.resoln_upper_filt = QtGui.QLineEdit(self.layoutWidget)
        self.resoln_upper_filt.setMaximumSize(QtCore.QSize(200, 16777215))
        self.resoln_upper_filt.setObjectName(_fromUtf8("resoln_upper_filt"))
        self.gridLayout_2.addWidget(self.resoln_upper_filt, 2, 3, 1, 1)
        self.label_18 = QtGui.QLabel(self.layoutWidget)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 2, 1, 1, 1)
        self.resoln_lower_filt = QtGui.QLineEdit(self.layoutWidget)
        self.resoln_lower_filt.setMaximumSize(QtCore.QSize(200, 16777215))
        self.resoln_lower_filt.setObjectName(_fromUtf8("resoln_lower_filt"))
        self.gridLayout_2.addWidget(self.resoln_lower_filt, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_23 = QtGui.QLabel(self.layoutWidget)
        self.label_23.setMinimumSize(QtCore.QSize(45, 0))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout.addWidget(self.label_23)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(180, 0))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 2)
        self.clear_button = QtGui.QPushButton(self.layoutWidget)
        self.clear_button.setMaximumSize(QtCore.QSize(35, 16777215))
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.gridLayout.addWidget(self.clear_button, 2, 4, 1, 1)
        self.drk_button = QtGui.QPushButton(self.layoutWidget)
        self.drk_button.setMaximumSize(QtCore.QSize(35, 16777215))
        self.drk_button.setObjectName(_fromUtf8("drk_button"))
        self.gridLayout.addWidget(self.drk_button, 1, 4, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(45, 0))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 2)
        self.y_max = QtGui.QLineEdit(self.layoutWidget)
        self.y_max.setMaximumSize(QtCore.QSize(80, 16777215))
        self.y_max.setObjectName(_fromUtf8("y_max"))
        self.gridLayout.addWidget(self.y_max, 2, 3, 1, 1)
        self.x_min = QtGui.QLineEdit(self.layoutWidget)
        self.x_min.setMaximumSize(QtCore.QSize(80, 16777215))
        self.x_min.setObjectName(_fromUtf8("x_min"))
        self.gridLayout.addWidget(self.x_min, 1, 2, 1, 1)
        self.x_max = QtGui.QLineEdit(self.layoutWidget)
        self.x_max.setMaximumSize(QtCore.QSize(80, 16777215))
        self.x_max.setObjectName(_fromUtf8("x_max"))
        self.gridLayout.addWidget(self.x_max, 1, 3, 1, 1)
        self.y_min = QtGui.QLineEdit(self.layoutWidget)
        self.y_min.setMaximumSize(QtCore.QSize(80, 16777215))
        self.y_min.setObjectName(_fromUtf8("y_min"))
        self.gridLayout.addWidget(self.y_min, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.apply_button = QtGui.QPushButton(self.layoutWidget)
        self.apply_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.apply_button.setObjectName(_fromUtf8("apply_button"))
        self.verticalLayout.addWidget(self.apply_button)
        self.mpl_figs = QtGui.QListWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl_figs.sizePolicy().hasHeightForWidth())
        self.mpl_figs.setSizePolicy(sizePolicy)
        self.mpl_figs.setMinimumSize(QtCore.QSize(400, 0))
        self.mpl_figs.setAutoFillBackground(False)
        self.mpl_figs.setObjectName(_fromUtf8("mpl_figs"))
        self.verticalLayout.addWidget(self.mpl_figs)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.normal_plot_tab, _fromUtf8(""))
        self.weight_scheme_tab = QtGui.QWidget()
        self.weight_scheme_tab.setObjectName(_fromUtf8("weight_scheme_tab"))
        self.weighting_tableview = QtGui.QTableView(self.weight_scheme_tab)
        self.weighting_tableview.setGeometry(QtCore.QRect(10, 310, 1171, 451))
        self.weighting_tableview.setObjectName(_fromUtf8("weighting_tableview"))
        self.layoutWidget_2 = QtGui.QWidget(self.weight_scheme_tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(960, 30, 201, 191))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setHorizontalSpacing(1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.resoln_lower_eq_2 = QtGui.QComboBox(self.layoutWidget_2)
        self.resoln_lower_eq_2.setMaximumSize(QtCore.QSize(55, 16777215))
        self.resoln_lower_eq_2.setObjectName(_fromUtf8("resoln_lower_eq_2"))
        self.gridLayout_3.addWidget(self.resoln_lower_eq_2, 3, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget_2)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 2)
        self.label_12 = QtGui.QLabel(self.layoutWidget_2)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 2)
        self.i_sig_filt_2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.i_sig_filt_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.i_sig_filt_2.setObjectName(_fromUtf8("i_sig_filt_2"))
        self.gridLayout_3.addWidget(self.i_sig_filt_2, 1, 3, 1, 1)
        self.i_filt_2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.i_filt_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.i_filt_2.setObjectName(_fromUtf8("i_filt_2"))
        self.gridLayout_3.addWidget(self.i_filt_2, 0, 3, 1, 1)
        self.i_filt_eq_2 = QtGui.QComboBox(self.layoutWidget_2)
        self.i_filt_eq_2.setMaximumSize(QtCore.QSize(55, 16777215))
        self.i_filt_eq_2.setObjectName(_fromUtf8("i_filt_eq_2"))
        self.gridLayout_3.addWidget(self.i_filt_eq_2, 0, 2, 1, 1)
        self.i_sig_filt_eq_2 = QtGui.QComboBox(self.layoutWidget_2)
        self.i_sig_filt_eq_2.setMaximumSize(QtCore.QSize(55, 16777215))
        self.i_sig_filt_eq_2.setObjectName(_fromUtf8("i_sig_filt_eq_2"))
        self.gridLayout_3.addWidget(self.i_sig_filt_eq_2, 1, 2, 1, 1)
        self.resoln_lower_filt_2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.resoln_lower_filt_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.resoln_lower_filt_2.setObjectName(_fromUtf8("resoln_lower_filt_2"))
        self.gridLayout_3.addWidget(self.resoln_lower_filt_2, 3, 3, 1, 1)
        self.resoln_upper_eq_2 = QtGui.QComboBox(self.layoutWidget_2)
        self.resoln_upper_eq_2.setMaximumSize(QtCore.QSize(55, 16777215))
        self.resoln_upper_eq_2.setObjectName(_fromUtf8("resoln_upper_eq_2"))
        self.gridLayout_3.addWidget(self.resoln_upper_eq_2, 2, 2, 1, 1)
        self.label_17 = QtGui.QLabel(self.layoutWidget_2)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 2, 1, 1, 1)
        self.resoln_upper_filt_2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.resoln_upper_filt_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.resoln_upper_filt_2.setObjectName(_fromUtf8("resoln_upper_filt_2"))
        self.gridLayout_3.addWidget(self.resoln_upper_filt_2, 2, 3, 1, 1)
        self.calc_weight_button = QtGui.QPushButton(self.weight_scheme_tab)
        self.calc_weight_button.setGeometry(QtCore.QRect(40, 150, 231, 31))
        self.calc_weight_button.setObjectName(_fromUtf8("calc_weight_button"))
        self.tab2_infobox = QtGui.QListWidget(self.weight_scheme_tab)
        self.tab2_infobox.setGeometry(QtCore.QRect(10, 230, 1171, 71))
        self.tab2_infobox.setObjectName(_fromUtf8("tab2_infobox"))
        self.calculate_start_check = QtGui.QCheckBox(self.weight_scheme_tab)
        self.calculate_start_check.setGeometry(QtCore.QRect(80, 40, 191, 26))
        self.calculate_start_check.setChecked(True)
        self.calculate_start_check.setTristate(False)
        self.calculate_start_check.setObjectName(_fromUtf8("calculate_start_check"))
        self.label_20 = QtGui.QLabel(self.weight_scheme_tab)
        self.label_20.setGeometry(QtCore.QRect(960, 0, 191, 33))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.bintype_intensity = QtGui.QCheckBox(self.weight_scheme_tab)
        self.bintype_intensity.setGeometry(QtCore.QRect(80, 90, 94, 26))
        self.bintype_intensity.setChecked(True)
        self.bintype_intensity.setAutoExclusive(True)
        self.bintype_intensity.setObjectName(_fromUtf8("bintype_intensity"))
        self.bintype_resolution = QtGui.QCheckBox(self.weight_scheme_tab)
        self.bintype_resolution.setGeometry(QtCore.QRect(80, 110, 94, 26))
        self.bintype_resolution.setAutoExclusive(True)
        self.bintype_resolution.setObjectName(_fromUtf8("bintype_resolution"))
        self.label_21 = QtGui.QLabel(self.weight_scheme_tab)
        self.label_21.setGeometry(QtCore.QRect(40, 60, 191, 33))
        self.label_21.setToolTip(_fromUtf8(""))
        self.label_21.setWhatsThis(_fromUtf8(""))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.weight_scheme_tab)
        self.label_22.setGeometry(QtCore.QRect(40, 10, 241, 33))
        self.label_22.setToolTip(_fromUtf8(""))
        self.label_22.setWhatsThis(_fromUtf8(""))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_24 = QtGui.QLabel(self.weight_scheme_tab)
        self.label_24.setGeometry(QtCore.QRect(720, 0, 191, 33))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.weight_scheme_tab)
        self.label_25.setGeometry(QtCore.QRect(720, 110, 191, 33))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.copy_weights = QtGui.QPushButton(self.weight_scheme_tab)
        self.copy_weights.setGeometry(QtCore.QRect(20, 780, 161, 31))
        self.copy_weights.setObjectName(_fromUtf8("copy_weights"))
        self.clearweights = QtGui.QPushButton(self.weight_scheme_tab)
        self.clearweights.setGeometry(QtCore.QRect(1010, 780, 161, 31))
        self.clearweights.setObjectName(_fromUtf8("clearweights"))
        self.layoutWidget1 = QtGui.QWidget(self.weight_scheme_tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(720, 150, 199, 74))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_4 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_13 = QtGui.QLabel(self.layoutWidget1)
        self.label_13.setToolTip(_fromUtf8(""))
        self.label_13.setWhatsThis(_fromUtf8(""))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)
        self.a_stop = QtGui.QLineEdit(self.layoutWidget1)
        self.a_stop.setObjectName(_fromUtf8("a_stop"))
        self.gridLayout_4.addWidget(self.a_stop, 0, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.layoutWidget1)
        self.label_14.setToolTip(_fromUtf8(""))
        self.label_14.setWhatsThis(_fromUtf8(""))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)
        self.b_stop = QtGui.QLineEdit(self.layoutWidget1)
        self.b_stop.setObjectName(_fromUtf8("b_stop"))
        self.gridLayout_4.addWidget(self.b_stop, 1, 1, 1, 1)
        self.layoutWidget2 = QtGui.QWidget(self.weight_scheme_tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(720, 30, 201, 74))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_15 = QtGui.QLabel(self.layoutWidget2)
        self.label_15.setToolTip(_fromUtf8(""))
        self.label_15.setWhatsThis(_fromUtf8(""))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)
        self.a_start = QtGui.QLineEdit(self.layoutWidget2)
        self.a_start.setObjectName(_fromUtf8("a_start"))
        self.gridLayout_5.addWidget(self.a_start, 0, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.layoutWidget2)
        self.label_16.setToolTip(_fromUtf8(""))
        self.label_16.setWhatsThis(_fromUtf8(""))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_5.addWidget(self.label_16, 1, 0, 1, 1)
        self.b_start = QtGui.QLineEdit(self.layoutWidget2)
        self.b_start.setObjectName(_fromUtf8("b_start"))
        self.gridLayout_5.addWidget(self.b_start, 1, 1, 1, 1)
        self.tabWidget.addTab(self.weight_scheme_tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSelect_File = QtGui.QMenu(self.menubar)
        self.menuSelect_File.setObjectName(_fromUtf8("menuSelect_File"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClear_Weights = QtGui.QAction(MainWindow)
        self.actionClear_Weights.setObjectName(_fromUtf8("actionClear_Weights"))
        self.actionClear_Filters = QtGui.QAction(MainWindow)
        self.actionClear_Filters.setObjectName(_fromUtf8("actionClear_Filters"))
        self.actionClear_All = QtGui.QAction(MainWindow)
        self.actionClear_All.setObjectName(_fromUtf8("actionClear_All"))
        self.actionSelect_File = QtGui.QAction(MainWindow)
        self.actionSelect_File.setObjectName(_fromUtf8("actionSelect_File"))
        self.menuSelect_File.addAction(self.actionSelect_File)
        self.menubar.addAction(self.menuSelect_File.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CAPOW", None))
        self.label.setText(_translate("MainWindow", "a:", None))
        self.label_2.setText(_translate("MainWindow", "b:", None))
        self.label_3.setText(_translate("MainWindow", "c:", None))
        self.label_4.setText(_translate("MainWindow", "d:", None))
        self.label_5.setText(_translate("MainWindow", "e:", None))
        self.label_6.setText(_translate("MainWindow", "f:", None))
        self.label_7.setText(_translate("MainWindow", "I/sig(I):", None))
        self.label_8.setText(_translate("MainWindow", "I:", None))
        self.label_18.setText(_translate("MainWindow", "Resoln:", None))
        self.label_23.setText(_translate("MainWindow", "Plot Axes:", None))
        self.label_9.setText(_translate("MainWindow", "x:", None))
        self.clear_button.setText(_translate("MainWindow", "Clr", None))
        self.drk_button.setText(_translate("MainWindow", "DRK", None))
        self.label_10.setText(_translate("MainWindow", "y:", None))
        self.apply_button.setText(_translate("MainWindow", "Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.normal_plot_tab), _translate("MainWindow", "Normal Probability Plot", None))
        self.label_11.setText(_translate("MainWindow", "I/sig(I):", None))
        self.label_12.setText(_translate("MainWindow", "I:", None))
        self.label_17.setText(_translate("MainWindow", "Resoln:", None))
        self.calc_weight_button.setText(_translate("MainWindow", "Calculate Weighting Parameters", None))
        self.calculate_start_check.setText(_translate("MainWindow", "Calculate Start", None))
        self.label_20.setText(_translate("MainWindow", "Weighting Cutoffs:", None))
        self.bintype_intensity.setText(_translate("MainWindow", "Intensity", None))
        self.bintype_resolution.setText(_translate("MainWindow", "Resolution", None))
        self.label_21.setText(_translate("MainWindow", "Weighting Binning:", None))
        self.label_22.setText(_translate("MainWindow", "Use SHELX a and b starting values:", None))
        self.label_24.setText(_translate("MainWindow", "Weighting Start Points:", None))
        self.label_25.setText(_translate("MainWindow", "Weighting Stop Points:", None))
        self.copy_weights.setText(_translate("MainWindow", "Send Weights to Tab1", None))
        self.clearweights.setText(_translate("MainWindow", "Clear Weights", None))
        self.label_13.setText(_translate("MainWindow", "a stop:", None))
        self.label_14.setText(_translate("MainWindow", "b stop:", None))
        self.label_15.setText(_translate("MainWindow", "a start:", None))
        self.label_16.setText(_translate("MainWindow", "b start:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.weight_scheme_tab), _translate("MainWindow", "Weighting Scheme", None))
        self.menuSelect_File.setTitle(_translate("MainWindow", "Select File", None))
        self.actionClear_Weights.setText(_translate("MainWindow", "Clear Weights", None))
        self.actionClear_Filters.setText(_translate("MainWindow", "Clear Filters", None))
        self.actionClear_All.setText(_translate("MainWindow", "Clear All", None))
        self.actionSelect_File.setText(_translate("MainWindow", "Select File", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
