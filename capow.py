### CAPOW (calculation and plotting of optimal weights) ###

#  NOTES:  #
# Written using pyqt (4.10.1), matplotlib (2.0.2), numpy (1.12.1), scipy (0.19.0), python (2.7.5)
# requires window_tab.py (gui) and shelx_weighting.py (code to run weighting minimization)
# input: .fcf (with .cif and .ins) or .fco (with .cif and .mas)

##Known issues:
# "RuntimeWarning: PyOS_InputHook is not available for interactive use of PyGTK" - problem is when importing pyplot from matplotlib. Works using matplotlib (2.0.2).

## To report errors/give feedback:
## - N.Johnson5@ncl.ac.uk or Michael.Probert@ncl.ac.uk

import sys, os

## Check that matplotlib, scipy, numpy, pyqt4 are all installed on computer ##

run = True #Flag, will change to false if module versions do not match.
try: 
    from matplotlib import __version__ as mp_u_vers #getting version of matplotlib on user computer
except ImportError:
    print "Program Exiting: Matplotlib module is needed to run this code. Please install and try again."
    sys.exit()
try:
    from scipy import __version__ as s_u_vers #getting version of scipyon user computer
except ImportError:
    print "Program Exiting: Scipy module is needed to run this code. Please install and try again."
    sys.exit()
try:
    from numpy import  __version__  as n_u_vers #getting version of numpy on user computer
except ImportError:
    print "Program Exiting: Numpy module is needed to run this code. Please install and try again."
    sys.exit()
try:   
    from PyQt4.Qt import PYQT_VERSION_STR as pq_u_vers # getting version of pyqt4, method from pyqt website, on user computer
except ImportError:
    print "Program Exiting: PyQt module is needed to run this code. Please install and try again."
    sys.exit()
py_u_vers = sys.version.split()[0] #getting version of python on user computer, prints long string with version number at start

## Check versions of required modules ##
def bruce(w_vers, u_vers):
    """function to return whether user version is higher, lower, or same as written version"""
    if u_vers > w_vers:
        return "H"
    elif w_vers == u_vers:
        return "S"
    else:
        return "L"

def compare_versions(written_vers, user_vers):
    """function to compare tested vs user versions of python/packages"""
    w_vers_list = written_vers.split(".")
    u_vers_list = user_vers.split(".")
    list_0 = bruce(w_vers_list[0],u_vers_list[0])
    if list_0 == "L":
        return "L"
    elif list_0 == "H":
        return "H"
    else:
        list_1 = bruce(w_vers_list[1],u_vers_list[1])
        if list_1 == "L":
            return "L"
        elif list_1 == "H":
            return "H"
        else:
            list_2 = bruce(w_vers_list[2],u_vers_list[2])
            if list_2 == "L":
                return "L"
            elif list_2 == "H":
                return "H"
            else:
                return list_2, "should not happen"


## version of python/package code, program written with
mp_w_vers = "2.0.2" #matplotlib
s_w_vers = "0.19.0" #scipy
n_w_vers = "1.12.1" #numpy
pq_w_vers = "4.10.1" #pyqt4
py_w_vers = "2.7.5" #python

## Checking if module versions are the same as what the code was written with ##

check_packages = ["", "", "", "", ""] #for use later when checking whether 

if mp_u_vers != mp_w_vers :
    check_packages[0] = compare_versions(mp_w_vers, mp_u_vers)
    if check_packages[0] == "L":
        print "Program Exiting: The code was written and tested with matplotlib (%s). Your version of matplotlib is (%s). Using an earlier version of matplotlib will cause the program to break." %(mp_w_vers, mp_u_vers)
    run = False
else:
    check_packages[0] = "S"
if s_u_vers != s_w_vers:
    run = False
    check_packages[1] = compare_versions(s_w_vers,s_u_vers)
    if check_packages[1] == "L":
        print "Program Exiting: The code was written and tested with scipy (%s). Your version of scipy is (%s). Using an earlier version of scipy may cause the program to break. " %(s_w_vers, s_u_vers)
else:
    check_packages[1] = "S"
if n_u_vers != n_w_vers:
    run = False
    check_packages[2] =  compare_versions(n_w_vers,n_u_vers)
    if check_packages[2] == "L":
        print "Program Exiting: The code was written and tested with numpy (%s). Your version of numpy is (%s). Using an earlier version of numpy may cause the program to break." %(n_w_vers, np_u_vers)
else:
    check_packages[2] = "S"
if pq_u_vers != pq_w_vers:
    run = False
    check_packages[3] = compare_versions(pq_w_vers,pq_u_vers)
    if check_packages[3] == "L":
        print "Program Exiting: The code was written and tested with PyQt4 (%s). Your version of PyQt4 is (%s). Using an earlier version of PyQt4 may cause the program to break." % (pq_w_vers, pq_u_vers)
else:
    check_packages[3] = "S"
if py_u_vers != py_w_vers:
    run = False
    check_packages[4] = compare_versions(py_w_vers,py_u_vers)
    if check_packages[4] == "L":
        print "Program Exiting: The code was written and tested with python (%s). Your version of python is (%s). Using an earlier version of python may cause the program to break." %(py_w_vers, py_u_vers)
else:
    check_packages[4] = "S"

## If modules are not the same, check if user still wants to run code ###
if run == False:
    for i in check_packages:
        if i == "L":
            print "Please update python/packages and try again."
            sys.exit()
    ## code should only be running here if there are "H" in list.
    #assumes that code is still  compatible with later versions of the packages
    print "Warning: CAPOW was written with :    \n  python:      %s \n  matplotlib:  %s \n  scipy:       %s \n  numpy:       %s \n  PyQt4:       %s" % (py_w_vers, mp_w_vers, s_w_vers, n_w_vers, pq_w_vers)
    print "This computer is using :    \n  python:      %s \n  matplotlib:  %s \n  scipy:       %s \n  numpy:       %s \n  PyQt4:       %s"% (py_u_vers, mp_u_vers, s_u_vers, n_u_vers, pq_u_vers)
    print "There may be issues with incompatibilities of functions."
    #sys.exit()
else:
    pass

print "Running CAPOW"

import math
from copy import deepcopy

from PyQt4.uic import loadUiType
from PyQt4 import QtCore, QtGui
try:
    from window_tab import Ui_MainWindow
except IOError:
    print "Program exiting: window-tab.py file is not present in this folder.  Please download a copy and try again."
    sys.exit()

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib import cm
import matplotlib.pyplot as plt #this might break with older versions of matplotlib giving a runtime error.

import numpy as np
import scipy.stats as stats
try:
    from shelx_weighting import shelx_weighting_calc 
except ImportError:
    print "Program exiting: shelx_weighting.py is not present in this folder. Please download a copy and try again."
    sys.exit()
###
        
class Main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self,scale_factor):
        super(Main, self).__init__()
        self.setupUi(self)
        self.qlist_item = QtGui.QListWidgetItem(self.mpl_figs)
        self.tab2_info = QtGui.QListWidgetItem(self.tab2_infobox)
        self.scale_factor = scale_factor
        self.set_up() #sets up gui and matplotlib widget
        self.file_selected = False #Flag incase user trys to run weighting scheme code before a file has been selected, if False error message will show.

    def set_up(self):
        """Function to connect all the buttons and set up the table headers for the widget"""
        #connecting buttons and functions
        self.apply_button.clicked.connect(self.recalc_fig)
        self.calc_weight_button.clicked.connect(self.calculate_weighting_scheme)
        self.copy_weights.clicked.connect(self.send_weights)
        self.drk_button.clicked.connect(self.drk_lim)
        self.clear_button.clicked.connect(self.clr_lim)
        self.clearweights.clicked.connect(self.clear_weights)
        self.actionSelect_File.triggered.connect(self.select_file)
        # adding equality signs into filter tables
        self.i_filt_eq.insertItem(0,">")
        self.i_filt_eq.insertItem(1,"<")
        self.i_sig_filt_eq.insertItem(0,">")
        self.i_sig_filt_eq.insertItem(1,"<")
        self.i_filt_eq_2.insertItem(0,">")
        self.i_filt_eq_2.insertItem(1,"<")
        self.i_sig_filt_eq_2.insertItem(0,">")
        self.i_sig_filt_eq_2.insertItem(1,"<")
        self.resoln_upper_eq.insertItem(0,"<") #swapped this round to make it read nicer. Resoln < 1 (so will keep all values of resolution that are less than 1.)
        self.resoln_upper_eq_2.insertItem(0,"<") #swapped
        self.resoln_lower_eq_2.insertItem(0,">") #swapped
        self.resoln_lower_eq.insertItem(0,">") #swapped
        self.filt_eq =  ">"
        self.sig_filt_eq = ">"
        #naming header for weighting scheme tab table
        headers = ["a","b","goof","wr2","stop a","stop b","I cutoff","Isig cutoff","resoln <","resoln >","no of reflns","start a","start b","bin","bin variance"]
        self.tablemodel = QtGui.QStandardItemModel() #internet says to make it a model to work
        self.tablemodel.setHorizontalHeaderLabels(headers)
        self.weighting_tableview.setModel(self.tablemodel)
        #sets up matplotlib widget
        self.fig1 = plt.figure()
        self.ax1f1 = self.fig1.add_subplot(1,1,1)
        self.ax1f1.plot([-4,4],[-4,4],'--',color='r') #plotting expected plot line
        self.canvas = FigureCanvas(self.fig1)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas,self.mplwindow, coordinates=True)
        self.mplvl.addWidget(self.toolbar)

    def select_file(self):
        """Allows user to select a file to use and then creates normal probability plot from the data"""
        dlg = QtGui.QFileDialog()
        marker = os.getcwd()
        plt.cla() #clear matplotlib
        file_name = QtGui.QFileDialog.getOpenFileName(self, 'Select structure factor file', marker,"fcf or fco files (*.fcf *.fco)")
        #file_name = QtGui.QFileDialog.getOpenFileName(self, 'Select structure factor file', '/home/',"fcf or fco files (*.fcf *.fco)") #change '/home/' to change the folder the code opens first.
        file_name = str(file_name)
        self.code_run = True #flag to stop weighting scheme code from running. Used later
        if os.path.isfile(file_name) == False: #if user did not select a file
            self.qlist_item.setText("Error: File has not been selected")
        else:
            self.i_file = file_name
            #self.addmpl()
            self.calc_weight_button.setEnabled(True)
            self.file_selected = True #Flag incase user trys to run weighting scheme code before a file has been selected
            ### Reset  items from a potential previous file
            self.lamda = 0.0
            self.shelx_a = 0.0
            self.shelx_b = 0.0
            self.mas_a = 0.0
            self.mas_b = 0.0
            self.mas_c = 0.0
            self.mas_d = 0.0
            self.mas_e = 0.0
            self.mas_f = 0.3333333333
            self.n_independant_params = ""
            ### reset fields in normal probability plot tab ####
            i_filt =self.i_filt.setText("")
            i_sig_filt = self.i_sig_filt.setText("")
            resoln_upper_filt = self.resoln_upper_filt.setText("")
            resoln_lower_filt = self.resoln_lower_filt.setText("")
            self.clr_lim()
            self.tab2_info.setText("")
            self.qlist_item.setText("")
            ### reset fields in weighting calculator tab ###
            self.clear_weights()
            self.resoln_upper_filt_2.setText("")
            self.resoln_lower_filt_2.setText("")
            self.i_filt_2.setText("")
            self.i_sig_filt_2.setText("")
            self.i_filt_2.setText("")
            self.i_sig_filt_2.setText("")
            self.a_stop.setText("")
            self.b_stop.setText("")
            self.a_start.setText("") #need to check for float
            self.b_start.setText("") #need to check for float
            self.i_filt_eq.setCurrentIndex(0)
            self.i_sig_filt_eq.setCurrentIndex(0)
            #need shelx to be checked, and weighting binning, I to be checked.
            ### need cif file to get number of independant parameters
            file_loc_list = os.path.split(file_name) #separating file name from folders: using os for file functions so is useable on other operating systems
            self.calculate_start_check.setChecked(True)
            self.bintype_intensity.setChecked(True)
            self.bintype_resolution.setChecked(False)
            self.i_filt_eq_2.setCurrentIndex(0)
            self.i_sig_filt_eq_2.setCurrentIndex(0)
            marker = file_loc_list[0] #marker to be used when opening file dialog to select file, opens in folder that fco/fcf file was selected from
            ### code will look for and select a cif file with the same starting name as input file, if no file, will open a file dialog to select one ###
            no_cif = False
            if file_name[-3:] == "fco":
                try:
                    potential_lsm_file_lst = os.path.split(file_name)
                    new_file_name = potential_lsm_file_lst[1][0:-4] + "_lsm.cif"#xd_lsm.cif made during xdlsm refinement
                    potential_lsm_file = os.path.join(potential_lsm_file_lst[0], new_file_name)
                    open(potential_lsm_file,"r")
                    cif_file = potential_lsm_file
                except IOError:
                    cif_file = QtGui.QFileDialog.getOpenFileName(self, 'Select cif file', marker, "cif file (*.cif)")
                    if os.path.isfile(str(cif_file)) == False: #if user did not select a file
                        self.qlist_item.setText("Error: Cif file has not been selected")
                        no_cif = True
            else:
                try:
                    potential_cif_file_lst = os.path.split(file_name)
                    new_cif_file = potential_cif_file_lst[1][0:-3]+ "cif"
                    potential_cif_file = os.path.join(potential_cif_file_lst[0], new_cif_file)
                    open(potential_cif_file,"r")
                    cif_file = potential_cif_file
                except IOError:
                    cif_file = QtGui.QFileDialog.getOpenFileName(self, 'Select cif file', marker, "cif file (*.cif)")
                    if os.path.isfile(str(cif_file)) == False: #if user did not select a file
                        self.qlist_item.setText("Error: Cif file has not been selected")
                        no_cif = True
            if no_cif == True:
                pass
            else:
                for line in open(cif_file,"r").readlines():
                    if line.startswith("_refine_ls_number_parameters"):
                        n_params = line.split()[1]
                        self.n_independant_params = float(n_params)
                if self.n_independant_params == "":
                    self.cif_info = False #error capture for later
                    self.qlist_item.setText("Number of independant parameters is not present in cif file. Program has stopped.")
                else:
                    self.cif_info = True
                    self.addmpl()

    def addmpl(self):
        """gets values to create normal probability plot"""
        run_flag = self.get_graph_values(self.i_file) #STOP/GO depending on if graph values have been extracted successfully
        if run_flag == "STOP": #if run flag is STOP then values have not been extracted successfully from code.
            self.code_run = False #This flag stops weighting scheme code from being able to run if there was a problem with importing files
        elif run_flag == "NoP": #no parameter from cif
            self.code_run = False
        elif run_flag == "NoI": #no info from ins/mas
            self.code_run = False
        elif run_flag == "NoV": #no values found in fcf/fco
            self.code_run = False
        else:
            self.R2_text = ""
            self.clear_weights()
            y = [-4,0,4] #x and y for expected normal probability line
            x = [-4,0,4] 
            def onpick2(event):
                    """ function to return information about reflections clicked on in normal probability plot"""
                    ind = event.ind
                    text_box_text = ""
                    text_box_list = ["Reflections Selected:","label:resoln:(fm,fc,sig(F)):,(graph x,y)"]
                    if len(ind) < 25:
                        for i in ind:
                            text_box_list.append("%s : %f : (%f, %f, %f) : (%f, %f)"%(self.labels[i],np.take(self.no_col,i) ,np.take(self.fm_only,i),np.take(self.fc_only,i),np.take(self.sigf_only,i),np.take(self.res[0][0], i), np.take(self.res[0][1], i)))
                    if len(text_box_list) > 0:
                        text_box_text = "\n".join(text_box_list)#
                    if len(self.R2_text) != 0:
                        text_box_text = self.R2_text + "\n" + text_box_text
                    self.qlist_item.setText(text_box_text)
            f = 1/3.0 #default f value
            if self.i_file[-3:] == "fcf":
                if self.weight_applied == True:
                    self.calc_graph(-99999,-99999,999999,-999999,self.shelx_a,self.shelx_b,0.0,0.0,0.0,f) #shelx_a and shelx_b taken from ins file
                else:
                    self.calc_graph(-99999,-99999,999999,-999999,-2.0,0.0,0.0,0.0,0.0,f) #-2.0 is xd default, a < -1.0 gives statistical weights
            else:
                self.calc_graph(-99999,-99999,999999,-999999,self.mas_a,self.mas_b,self.mas_c,self.mas_d,self.mas_e,self.mas_f)
            x_min= False   
            x_max= False   
            y_min= False   
            y_max = False
            plt.cla()
            self.plot_norm(x_min,x_max,y_min,y_max)
            self.ax1f1.plot(x,y,'--',color='r')
            self.canvas.draw()
            self.canvas.mpl_connect('pick_event', onpick2)
            
    def select_info_file(self,marker,file_type):
        """function to bring up file dialog to select info - ins/mas file to provide extra information about refinement - lambda, applied weight"""
        dlg = QtGui.QFileDialog()
        if file_type == "fcf":
            file_name = QtGui.QFileDialog.getOpenFileName(self, 'Select .ins or .res file', marker,"ins file (*.ins *.res)")
        elif file_type == "fco":
            file_name = QtGui.QFileDialog.getOpenFileName(self, 'Select .mas file', marker,"mas file (*.mas )")
        #self.info_file.setText(file_name)
        #self.info_file_name
        if os.path.isfile(str(file_name)) == False: #if user did not select a file
                self.qlist_item.setText("Error: No ins/mas file has not been selected")
                file_name = False
        return file_name

    def check_info_file(self,i_file, file_type):
        """ checks that info file exists"""
        info_file_lst = os.path.split(i_file)
        if file_type == "fcf":
            new_file_name = info_file_lst[1][0:-3] + "ins"
            info_file = os.path.join(info_file_lst[0], new_file_name)
            file_type="fcf"
        elif file_type == "fco":
            new_file_name = info_file_lst[1][0:-3] + "mas"
            info_file = os.path.join(info_file_lst[0], new_file_name)
            file_type ="fco"
        try:
            open_ins = open(info_file,"r")# ##potential issue if ins file does not have same name as fcf file
        except IOError:
            marker = os.path.split(i_file)[0]
            info_file = self.select_info_file(marker, file_type)
        return info_file

    def get_graph_values(self,i_file):
        """function to obtain values of fc, fm and su from imported file. Calculates resolution from lambda for fcf file."""
        f= open(i_file,"r") #open selected file
        g=f.readlines()
        s = 0
        start_defined = False
        self.F_c = []
        self.F_m = []
        self.sig_F = []
        self.sth = []
        self.resoln = []
        self.F_v_F = []
        file_type = i_file[-3:] #xd = fco, shelx = fcf
        self.labels_all = []
        self.sinth_all = []
        if file_type == "fco":
            for line in g:
                s += 1
                if line.startswith(" _refln_XD_refine_code"):
                    start = s
                    val_order = [4,3,5] # order of line split for [fm, fc, fsig], to be used when getting values from file
                    start_defined = True
                elif line.startswith("data_"):
                   self.code_mark = line.split("_")[1] #gets data flag name from xd.mas
            info_file_name = self.check_info_file(i_file, "fco")
            if info_file_name == False:
                no_info_file = True #No ins/mas file has been selected
            else:
                no_info_file = False
                open_fco_name = open(info_file_name,"r")
                open_fco = open_fco_name.readlines()
                for line in open_fco:
                    if line.startswith("WEIGHT") or line.startswith("!WEIGHT"):
                        weight_line = line.split()
                        self.mas_a = float(weight_line[1])
                        self.mas_b =float(weight_line[2])
                        self.mas_c =float(weight_line[3])
                        self.mas_d =float(weight_line[4])
                        self.mas_e =float(weight_line[5])
                        self.mas_f = float(weight_line[6])
                        self.weight_applied = True
                        self.a_edit.setText(str(self.mas_a))
                        self.b_edit.setText(str(self.mas_b))
                        self.c_edit.setText(str(self.mas_c))
                        self.d_edit.setText(str(self.mas_d))
                        self.e_edit.setText(str(self.mas_e))
                        self.f_edit.setText(str(self.mas_f))
                    elif line.startswith("WAVE"):
                        wave_line = line.split()
                        self.lamda = float(wave_line[1])
                open_fco_name.close()
        elif file_type == "fcf":
            start_string = "NOTDEFINED"
            self.code_mark = "[Plot Name]"
            #### get weights and unit cell parameters from filename.ins ####
            info_file_name = self.check_info_file(i_file, "fcf")
            if info_file_name == False:
                no_info_file = True
            else:
                no_info_file = False
                open_ins_name = open(info_file_name,"r")
                open_ins = open_ins_name.readlines()
                for line in open_ins:
                    if line.startswith("CELL"):
                        cell_params = line.split()
                        self.lamda = float(cell_params[1])
                        unit_a =float(cell_params[2])
                        unit_b =float(cell_params[3])
                        unit_c =float(cell_params[4])
                        #numpy uses angles in radians for trig, so need to convert (as we will use these values later)
                        unit_alpha =np.radians(float(cell_params[5]))
                        unit_beta =np.radians(float(cell_params[6]))
                        unit_gamma= np.radians(float(cell_params[7]))
                    elif line.startswith("WGHT"):
                        #takes weight values from ins file to use in graph.
                        shelx_weight = line.split()
                        self.shelx_a = float(shelx_weight[1])
                        self.shelx_b = float(shelx_weight[2])
                        self.weight_applied = True
                        self.a_edit.setText(str(self.shelx_a))
                        self.b_edit.setText(str(self.shelx_b))
                        self.c_edit.setText("0.0")
                        self.d_edit.setText("0.0")
                        self.e_edit.setText("0.0")
                        self.f_edit.setText("1/3")
                        #shelx currently only calculates a and b.
                        #send these values to initial graph
                open_ins_name.close()
            ######
            for line in g:
                s += 1
                if line.startswith("_shelx_refln_list_code"):
                    list_code = line.split()[1]
                    if list_code == "4":
                        #start_defined = True
                        start_string = " _refln_observed_status"
                        val_order = [4, 3, 5] #[Fm2, Fc2,Fsig2]
                    elif list_code == "8":
                        start_string = " _shelx_refinement_sigma"
                        #start_defined = True
                        val_order = [3, 5, 4] #[Fm2, Fc2 ,Fsig2]
                    else:
                        start_defined = False
                        self.qlist_item.setText("Code can only work with LIST 4 and 8")
                        break
                elif line.startswith(start_string) or line.startswith(" %s" %start_string): #sometimes there is an extra space before the start string in fcf
                    start = s
                    start_defined = True
        else:
            start_defined = False
            self.qlist_item.setText("Program only works with .fco or .fcf (LIST 4,8).")
        if self.cif_info == False:
            self.code_running = False
            return "NoP" #meaning we do not have the number of independant parameters from the cif
        elif no_info_file == True:
            self.code_running = False
            return "NoI"            
        elif start_defined == False: #if start of list has not been defined, code will break
                self.qlist_item.setText("Error: Values not found in file.")
                self.code_running = False
                self.recalc = False #so that graph cannot be recalculated because there is no file
                return "STOP" #have been unable to get values from input file therefore will not make graph and print error message
        else:
            for i in range(start,len(g)):
                l = g[i]
                lst = l.split()
                if len(lst) == 0: continue
                self.F_m.append(float(lst[val_order[0]]))
                self.F_c.append(float(lst[val_order[1]]))
                self.sig_F.append(float(lst[val_order[2]]))
                #get key of hkl for labels #
                ha = int(lst[0])
                la =int(lst[2])
                ku = int(lst[1])
                h = str(ha).rjust(4, " ")
                k = str(ku).rjust(4, " ")
                lz = str(la).rjust(4, " ")     
                key_lst = [h,k,lz]
                key = "".join(key_lst)
                key = key.lstrip()
                self.labels_all.append(key)
                if file_type == "fcf":
                    #formula for triclinic from giacavazzo pg 66
                    denom = (1- (np.cos(unit_alpha))**2 - (np.cos(unit_beta))**2 - (np.cos(unit_gamma))**2 + 2*np.cos(unit_alpha)*np.cos(unit_beta)*np.cos(unit_gamma))
                    term1 =(ha**2/unit_a**2)*(np.sin(unit_alpha)**2)
                    term2 =(ku**2/unit_b**2)*(np.sin(unit_beta)**2)
                    term3 = (la**2/unit_c**2)*(np.sin(unit_gamma)**2)
                    term4 =((2*ku*la)/(unit_b*unit_c))*(np.cos(unit_beta)*np.cos(unit_gamma) - np.cos(unit_alpha))
                    term5 =((2*ha*la)/(unit_a*unit_c))*(np.cos(unit_alpha)*np.cos(unit_gamma) - np.cos(unit_beta))
                    term6 = ((2*ku*ha)/(unit_b*unit_a))*(np.cos(unit_beta)*np.cos(unit_alpha) - np.cos(unit_gamma))
                    num = term1  + term2 +term3 +term4+ term5 +term6
                    one_dhkl = np.sqrt(num/denom) #as value calculated is 1/dhkl**2
                    resoln = self.lamda*one_dhkl/2
                    self.sth.append(resoln)
                    sinthl = one_dhkl/2
                    self.resoln.append(sinthl)
                elif file_type == "fco":
                    self.sth.append(float(lst[6])*self.lamda) #should this not be *lamda, isn't valule in fco sinth/lamda (think it is)
                    self.resoln.append(float(lst[6]))
                else:
                    self.sth.append(1)
            if len(self.F_m) == 0:
                self.qlist_item.setText("No values found in file.")
                return "NoV"
            else:
                self.code_running = True
                self.recalc = True # preliminarily allowing graph to be recalculated as values have been collected
                return "GO" #values have been collected, therefore return go to show that code should continue

        
    def calc_graph(self,i_filt,i_sig_filt,resoln_upper_filt,resoln_lower_filt,a,b,c,d,e,f):
        """function to produce normal probability plot"""
        if self.code_running == False: #Check that values from fco/fcf have been gathered.
            pass
        else:
            ### lists for values to be plotted
            F_val = []
            f_sub = []
            f_m_only = []
            sig_f_only = []
            f_c_only = []
            fc = [] #colour of points
            #set weight string for printing
            if a <= -1:
                self.weight_string = "Weighting applied:\n Statistical weights \n"
            else:
                self.weight_string = "Weighting applied:\n a: %f, b:%f, c%f, d:%f, e:%f, f: %f\n" %(round(a,6), round(b,6), round(c,6), round(d,6), round(e,6),round(f,6))
            i_sig = []
            labels = []
            w = []
            def calc_and_append(i,a,b,c,d,e,f):
                """function to calculate weighting value for each reflection and append values to lists for further use"""
                s = self.sig_F[i]
                if c > 0:
                        q = np.exp(c*self.sth[i])
                elif c< 0:
                        q = 1 - np.exp(c*self.sth[i])
                else: #c == 0
                    q = 1.0
                if a < -1.0: #statistical weights
                    a = 0.0
                    b = 0.0
                    c = 0.0
                    d = 0.0
                    e = 0.0
                    f = 1/3.0
                    #p = (f*self.F_m[i] + (1-f)*self.F_c[i])
                    base = (s**2)
                    w2 = base/q
                elif a > -1.0:
                    p = (f*self.F_m[i] + (1-f)*self.F_c[i])
                    base = (s**2 + (a*p)**2 + b*p + d + (self.sth[i]/self.lamda)*e)
                    w2 = base/q
                else: # a = -0.1, unit weights
                    #p = 0.0
                    w2 = 1.0
                #base = (s**2 + (a*p)**2 + b*p + d + (self.sth[i]/self.lamda)*e)
                #w2 = base/q
                        #w_tot = sum(w*np.square(fo-scale_factor*fc))
                w.append(np.sqrt(w2))
                f_no = ((self.F_c[i]-self.F_m[i]))/np.sqrt(w2) # need w in there somehow.
                i_sig.append(self.F_m[i]/self.sig_F[i])
                f_m_only.append(self.F_m[i])
                sig_f_only.append(self.sig_F[i])
                fc.append(self.resoln[i]) #change this based on what you want colour to be!! - probably want this to be an option (resoln is sintheta/lamda)
                F_val.append(f_no) #Fval is the observed resolution value
                f_c_only.append(self.F_c[i])
                labels.append(self.labels_all[i])
            less_than = 0
            for i in range(0,len(self.F_m)):
                #if np.sqrt(self.F_m[i]) > 0.0: #cutoff makes it match drkplot,
                if self.F_m[i] > -9999999999.0: #0.0: # as square rooting a number less than 0 would make np.sqrt freak out - think this line should be changed to the 0.0!!!!!!!!!!
                    resoln_i = float(self.resoln[i]) #resolution being sintheta/lamda
                    ### filtering reflections based on limits ###
                    utrue =  resoln_i >= resoln_lower_filt #is the resolution number above the lower filt
                    ltrue =  resoln_upper_filt >= resoln_i # is resolution number below the upper filt
                    # lower filt < resolution < upper filt == good! :D
                    if utrue == True:
                        if ltrue == True:
                            if self.filt_eq == ">":
                                if self.F_m[i] >= i_filt:
                                    if self.sig_filt_eq == ">":
                                        if self.F_m[i]/self.sig_F[i] >= i_sig_filt:
                                                calc_and_append(i,a,b,c,d,e,f) # append
                                    elif self.sig_filt_eq == "<":
                                        if self.F_m[i]/self.sig_F[i] <= i_sig_filt:
                                                calc_and_append(i,a,b,c,d,e,f) #when this condition is hit, then removed, bad things happen (oh yes because it is reset
                            elif self.filt_eq == "<":
                                if self.F_m[i] <= i_filt:
                                    if self.sig_filt_eq == ">":
                                        if self.F_m[i]/self.sig_F[i] >= i_sig_filt:
                                                calc_and_append(i,a,b,c,d,e,f) # append
                                    elif self.sig_filt_eq == "<":
                                        if self.F_m[i]/self.sig_F[i] <= i_sig_filt:
                                                calc_and_append(i,a,b,c,d,e,f) #append
                else:
                    less_than += 1
            if len(F_val) == 0: #if this occurs there are no values in the list, therefore no graph will be drawn
                self.nocalc_text = "No values match this criteria"
                text_box_text = self.nocalc_text
                self.qlist_item.setText(text_box_text)
                self.recalc = False
            else:
                self.recalc = True
                self.res = stats.probplot(F_val)
                zipped = zip(F_val,fc,i_sig,labels,w,f_m_only,sig_f_only,f_c_only) #sort in order
                sort = sorted(zipped) #sorts by first column.
                self.no_col = []
                self.labels = []
                self.weights = []
                self.fm_only = []
                self.sigf_only = []
                self.fc_only = []
                for item in sort:
                    self.no_col.append(item[1])
                    self.labels.append(item[3])
                    self.weights.append(item[4])
                    self.fm_only.append(item[5])
                    self.sigf_only.append(item[6])
                    self.fc_only.append(item[7])
        

            def calculate_R2(F_val):
                """function to calculate R^2 value of normal probability plot"""
                res_m = self.res[1][0]
                res_c = self.res[1][1]
                y_avg = np.mean(F_val)
                tot_sq = 0
                reg_sq = 0
                norm_sq_tot = 0
                se_sq = 0
                goof_tot = 0
                for i in range(0,len(self.res[0][0])):
                    x = self.res[0][0][i]
                    y = self.res[0][1][i]
                    ypred = res_m*x+res_c
                    ssr = (ypred - y_avg)**2
                    sst = (y - y_avg)**2
                    se = (y - ypred)**2
                    norm_sq = (y-x)**2
                    tot_sq += sst
                    reg_sq += ssr
                    se_sq += se
                    norm_sq_tot += norm_sq
                    if x == 0:
                        pass
                    else:
                        goof_add = ((y-x)**2)/x #calculating goodness of fit
                    goof_tot += goof_add
                R2_straight = 1- (norm_sq_tot/tot_sq)
                return 1 - se_sq/tot_sq, R2_straight#R2
            R2_val, r2_s = calculate_R2(F_val)
            self.R2_text = "%sR2 : %f \nR2 straight: %f \nNo. of Reflections: %d \n"%(self.weight_string, R2_val, r2_s, len(F_val))
            text_box_text = self.R2_text
            self.qlist_item.setText(text_box_text)

    def recalc_fig(self):
        """function triggered by apply button on normal probability plot tab, recalculates plot with defined weight and/or data limits and axes"""
        self.run_recalc = True #set as true, used for while loop to check that a -f and limits are all numerical or fractions
        while self.run_recalc == True: #using while loop to allow stopping of function if values are non-numeric, or file is missing.
            if self.file_selected == False:
                self.qlist_item.setText("Error: File has not been selected")
                break
            if self.cif_info == False:
                self.qlist_item.setText("Error: number of independant parameters is not in cif file")
                break
            a_val = self.a_edit.text()
            if len(a_val) < 1: #if there is nothing in box, len = 0, set default (0.0)
                a_val = 0.0
            else:
                a_val = self.check_int(a_val)
                if a_val == "False":
                    break
            b_val =self.b_edit.text()
            if len(b_val) < 1:
                b_val = 0.0
            else:
                b_val = self.check_int(b_val)
                if b_val == "False":
                    break
            c_val =self.c_edit.text()
            if len(c_val) < 1:
                c_val = 0.0
            else:
                c_val = self.check_int(c_val)
                if c_val == "False":
                    break
            d_val =self.d_edit.text()
            if len(d_val) < 1:
                d_val = 0.0
            else:
                d_val = self.check_int(d_val)
                if d_val == "False":
                    break
            e_val =self.e_edit.text()
            if len(e_val) < 1:
                e_val = 0.0
            else:
                e_val = self.check_int(e_val)
                if e_val == "False":
                    break
            f_val = self.f_edit.text()
            if len(f_val) < 1:
                f_val = 1/3.0 #default === 1/3.0
            else:
                f_val = self.check_int(f_val)
                if f_val == "False":
                    break
            self.filt_eq =  self.i_filt_eq.currentText() #checking which inequality sign is selected for intensity filter
            self.sig_filt_eq =  self.i_sig_filt_eq.currentText()#checking which inequality sign is selected intensity/s.u. filter
            i_filt =self.i_filt.text()
            i_sig_filt = self.i_sig_filt.text()
            resoln_upper_filt = self.resoln_upper_filt.text()
            resoln_lower_filt = self.resoln_lower_filt.text()
            if len(self.i_sig_filt.text()) > 0:
                i_sig_filt= self.check_int(i_sig_filt)
                if i_sig_filt == False:
                    break
            else:
                if self.sig_filt_eq == ">":
                    i_sig_filt = -9999999999.9
                else:
                    i_sig_filt = 9999999999.9
            if len(self.i_filt.text()) > 0:
                i_filt = self.check_int(i_filt)
                if i_filt == False:
                    break
            else:
                if self.filt_eq == ">":
                    i_filt = -9999999999.9
                else:
                    i_filt = 9999999999.9
            ### checking resoln_upper_filt and lower _filt ####
            if resoln_upper_filt == "":
                resoln_upper_filt = 9999999999999.0
            else:
                resoln_lower_filt =self.check_int(resoln_lower_filt)
                if resoln_lower_filt == False:
                    break
            if resoln_lower_filt == "":
                resoln_lower_filt = -99999999999999.0
            else:
                resoln_upper_filt = self.check_int(resoln_upper_filt)
                if resoln_upper_filt == False:
                    break
            #check they are all numerical values
            plt.cla()
            self.calc_graph(i_filt,i_sig_filt,resoln_upper_filt,resoln_lower_filt,a_val, b_val, c_val, d_val, e_val,f_val)
            if self.recalc == True: #checks there are values in list still after things have been filtered out True/False, assigned in calc_graph based on whether there are items in value lists after filters applied
                def check(a):
                    """checks if graphical limits are floats or not"""
                    if len(a) < 1:
                        return False
                    else:
                        try:
                                a = float(a)
                                return a
                        except ValueError:
                                return False
                x_min_val = check(self.x_min.text())
                x_max_val =  check(self.x_max.text())
                y_min_val =  check(self.y_min.text())
                y_max_val =  check(self.y_max.text())
                self.plot_norm(x_min_val, x_max_val, y_min_val, y_max_val)
            self.run_recalc = False #to stop while loop from running

    def plot_norm(self,x_min,x_max,y_min,y_max):
        """plots normal probability plot, if limits not defined, max or min value used as limit to show all points"""
        ### need to split up resolutions for graph ###
        res_resolncut = []
        res2_resolncut = []
        upper = 2.0
        lower = 0.0
        colour = []      
        res2 = self.ax1f1.scatter(self.res[0][0],self.res[0][1],c=self.no_col, lw=0, s=10,picker=True)#line_picker)
        y = [-4,0,4]
        x = [-4,0,4]
        self.ax1f1.plot(x,y,'--',color='r')
        self.ax1f1.axhline(y=0,ls="-",c="black")
        self.ax1f1.axvline(x=0,ls="-",c="black")
        if x_min != False:
            if x_max != False:
                self.ax1f1.set_xlim([x_min,x_max])
            else:
                self.ax1f1.set_xlim([x_min,plt.xlim()[1]])
        if x_max != False:
            if x_min != False:
                pass
            else:
                self.ax1f1.set_xlim([plt.xlim()[0] ,x_max])
        if y_min != False:
            if y_max != False:
                self.ax1f1.set_ylim([y_min,y_max])
            else:
                self.ax1f1.set_ylim([y_min,plt.ylim()[1]])
        if y_max != False:
            if y_min != False:
                pass
            else:
                self.ax1f1.set_ylim([plt.ylim()[0],y_max])
        self.ax1f1.set_xlabel("Expected Residuals")
        self.ax1f1.set_ylabel("Ordered Residuals")
        self.fig1.canvas.draw()

    def check_frac(self,y):
        """function to check if input value for weight/limit is a fraction and if so extract value"""
	frac = y.split("/")
	def is_number(x):
            try:
                no = float(x)
                return True
            except ValueError:
                return False
	if len(frac) == 2:
		if is_number(frac[0]) == True and is_number(frac[1]) == True: #makes sure both items in list can be floats
			new_no = float(frac[0])/float(frac[1])
			fraction = new_no
		else:
			fraction = "False"
	else:
		fraction = "False"
	return fraction

    def check_int(self,string):
        """function to check if input value for weight/limit in normal probability plot is a float and if so extract value"""
        if string == "":
            return string
        else:
            try:
                    no = float(string)
            except ValueError:
                    if "/" in string:
                        no = self.check_frac(string) #so fractions can also be input
                    else:
                        no = "False" #using it as a string as if value = 0.0, will be evaluated as false when it shouldn't be.
            if no == "False":
                text_box_text = "One of the input values is not a number or a fraction:\n        graph not recalculated"
                self.qlist_item.setText(text_box_text)
            return no
    
    def check_int_weight(self,string):
        """function to check if input for cutoffs in weighting tab is a number"""
        if string == "":
            return string
        else:
            try:
                    no = float(string)
            except ValueError:
                    if "/" in string:
                        no = self.check_frac(string)
                    else:
                        no = "False"
            if no == "False":
                text_box_text = "One of the input values is not a number or a fraction:\n        graph not recalculated"
                self.tab2_info.setText(text_box_text)
            return no
    
    def calculate_weighting_scheme(self):
        """calculates optimal a and b parameters using weighting scheme code from python script"""
        #f_c, f_m, sig_f
        #check input values are numerical]
        all_num=True
        resoln_upper = self.check_int_weight(self.resoln_upper_filt_2.text()) 
        resoln_lower =self.check_int_weight(self.resoln_lower_filt_2.text())
        i_remove = self.check_int_weight(self.i_filt_2.text())
        isig_remove = self.check_int_weight(self.i_sig_filt_2.text())
        i_val  = self.check_int_weight(self.i_filt_2.text())
        isig_val = self.check_int_weight(self.i_sig_filt_2.text())
        all_num = True
        if resoln_upper == "False" or resoln_lower == "False" or i_remove == "False" or isig_remove == "False" or i_val == "False" or isig_val == "False":
            all_num = False
        #check that input values are numbers.
        if self.file_selected == False:
            self.tab2_info.setText("Error: File has not been selected")
        elif all_num == False:
            self.tab2_info.setText("Error: One or more of cutoffs is not a number.")
            #pass
        elif self.code_run == False: #Stop  running if there was an issue importing files
            self.tab2_info.setText("Error: Problem importing files. Weighting code cannot run.")
        else:
            self.tab2_info.setText("")
            Fmlist = []
            Fclist = []
            sigflist = []
            resolnlist = []
            self.calc_weight_button.setEnabled(False)
            table_column = []
            Fmlist = deepcopy(self.F_m)
            Fclist =deepcopy(self.F_c)
            sigflist =deepcopy(self.sig_F)
            resolnlist = deepcopy(self.resoln)
            F_c = np.array(Fclist)
            F_m = np.array(Fmlist)
            sig_F = np.array(sigflist)
            resolution = np.array(resolnlist)
            stop_run = False
            bintype = self.weight_bin_style()
            new_Fm = []
            new_Fc = []
            new_sigF = []
            newres = []
            isig_table = ""
            i_table = ""
            ru_table = ""
            rl_table = ""
            noreflns = len(new_Fm)
            #run = shelx_weighting_calc olex_weighting_scheme(self.n_independant_params, self.scale_factor, new_Fm, new_Fc, new_sigF, newres, bintype) #setting up class from weighting scheme python scripts.
            new_Fm, new_Fc, new_sigF, newres, i_table,isig_table, ru_table, rl_table,noreflns = self.sort_data(F_m, F_c, sig_F, resolution)
            zero_indicies = new_Fm < 0 #need reset to zero as in olex
            new_Fm[zero_indicies] = 0
            run = shelx_weighting_calc(self.n_independant_params, self.scale_factor, new_Fm, new_Fc, new_sigF, newres, bintype) #setting up class from weighting scheme python scripts.
            if self.calculate_start_check.checkState() == 2: #check state of checkbox.
                calc_start = True
                start_a = 0
                start_b = 0
                start_a, start_b = run.calculate_start(F_m, F_c, sig_F) #these vals all data, sorting would start here before put into file
                a_stop = self.check_int_weight(self.a_stop.text())
                b_stop = self.check_int_weight(self.b_stop.text())
                if a_stop == "False" or b_stop == "False":
                    self.tab2_info.setText("Error: One or more Weighting Stopping Points not a number.")
                    stop_run = True
            else:
                calc_start = False
                start_a = self.check_int_weight(self.a_start.text()) #need to check for float
                start_b = self.check_int_weight(self.b_start.text()) #need to check for float
                a_stop = self.check_int_weight(self.a_stop.text())
                b_stop = self.check_int_weight(self.b_stop.text())
                if start_a == "" or start_b == "":
                    self.tab2_info.setText("Error: No starting a or b values set. Please input values or check Calculate Start box and try again")
                    stop_run = True
                elif start_a == "False" or start_b == "False":
                    self.tab2_info.setText("Error: One or more Weighting Starting Points not a number.")
                    stop_run = True
                elif a_stop == "False" or b_stop == "False":
                    self.tab2_info.setText("Error: One or more Weighting Stopping Points not a number.")
                    stop_run = True
            if stop_run == False:
                if a_stop == "" or b_stop == "":
                    a_stop = 1e-4
                    b_stop = 5e-3
#                else:
#                    a_stop = float(a_stop)
#                    b_stop = float(b_stop)
                    #olex defaults
                a,b,goof,wr2,variance, error = run.minimize_variance(a_stop,b_stop,start_a, start_b)
                if len(error) > 0:
                    self.tab2_info.setText(error)
                table_column = []
                table_vals = [a,b,goof,wr2,a_stop,b_stop,i_table,isig_table, ru_table, rl_table,noreflns,start_a,start_b,bintype,variance]
                for i in table_vals:
                    item = QtGui.QStandardItem(str(i))
                    table_column.append(item)
                self.tablemodel.appendRow(table_column)
                self.weighting_tableview.setModel(self.tablemodel)
                if a == "-" and b == "-":
                    self.tab2_info.setText("CAPOW could not search for weighting scheme, try smaller stopping values or adjusting starting values.")
            self.calc_weight_button.setEnabled(True)
            
    def weight_bin_style(self):
        """function to check which weighting bin is required"""
        if self.bintype_intensity.checkState() == 2:
            bintype = "I"
        #elif self.bintype_resolution.checkState() == 2:
        else: #either intensity is ticked or resolution is ticked.   
            bintype = "R"
        return bintype
    
    def sort_data(self, Fm, Fc, sigF, resolution):
        """function to apply cutoffs to data for weighting scheme calculator"""
        #create lists to populate during application of cutoffs
        remove_index = []
        remove_resup = []
        remove_reslow = []
        remove_i = []
        remove_isig = []
        resulting_list = []
        ints = []
        # obtain input values from weighting tab
        resoln_upper =self.resoln_upper_filt_2.text() 
        resoln_lower =self.resoln_lower_filt_2.text()
        i_remove = self.i_filt_2.text()
        isig_remove = self.i_sig_filt_2.text()        
        i_filt_eq = self.i_filt_eq_2.currentText()
        isig_filt_eq = self.i_sig_filt_eq_2.currentText()
        i_val  = self.i_filt_2.text()
        isig_val = self.i_sig_filt_2.text()
        isig_table = ""
        i_table = ""
        ru_table = ""
        rl_table = ""
        if resoln_upper != "":
            remove_resup = resolution > float(resoln_upper) #want to remove everything above, so only want indexes of those above
            ru_table = "> %s" % resoln_upper
        if resoln_lower != "":
            remove_reslow = resolution < float(resoln_lower) #find values with a resoltion of less than resoln_lower, produces list True False whether this condition is met
            rl_table = "> %s" % resoln_lower
        #### resoln cutoff upper###
        if len(remove_resup) > 0:
            if len(remove_reslow) > 0:
                ints = [i for i in range(0, len(Fm)) if remove_resup[i] == True] #whether above condition is met, remove_resup list of true falses, only want index of those that are true
                resulting_list = list(ints)
                ints = []
                ints = [i for i in range(0, len(Fm)) if remove_reslow[i] == True]
                resulting_list.extend(x for x in ints if x not in resulting_list) #add values to resulting list if true in remove_reslow (and not already in resulting list)
                ints = []
            else:
                ints = [i for i in range(0, len(Fm)) if remove_resup[i] == True]
                resulting_list = list(ints)
                ints = []
        elif len(remove_reslow) > 0: #resolution cutoff lower
            ints = [i for i in range(0, len(Fm)) if remove_reslow[i] == True]
            resulting_list = list(ints)
            ints = []
        ### check i cutoff##
        if i_val != "":
            if i_filt_eq == "<":
                remove_i = Fm > float(i_val) #so selects all Fm values that are greater than the cutoff
            elif i_filt_eq == ">":
                #then check list
                remove_i = Fm < float(i_val)
            i_table = "%s %s" % (i_filt_eq,i_val)
            if len(resulting_list) > 0:
                #if the resulting list has values in, need to make sure that there are no doubles included in resulting list when lower indicies joined on
                ints = []
                ints = [i for i in range(0, len(Fm)) if remove_i[i] == True]
                resulting_list.extend(x for x in ints if x not in resulting_list)
                ints = []
            else:
                ints = [i for i in range(0, len(Fm)) if remove_i[i] == True]
                resulting_list = list(ints)
        ####
        fmsig = Fm/sigF
        ### i/s.u. cutoff
        if isig_val != "":
            if isig_filt_eq == "<":
                remove_isig = fmsig > float(isig_val) #so selects all Fm values that are greater than the cutoff
            elif isig_filt_eq == ">":
                remove_isig = fmsig < float(isig_val)
            isig_table = "%s %s" % (isig_filt_eq,isig_val)
            if len(resulting_list) > 0:
                #if the resulting list has values in, need to make sure that there are no doubles included in resulting list when lower indicies joined on
                ints = []
                ints = [i for i in range(0, len(Fm)) if remove_isig[i] == True]
                resulting_list.extend(x for x in ints if x not in resulting_list)
                ints = []
            else:
                ints = []
                ints = [i for i in range(0, len(Fm)) if remove_isig[i] == True]
                resulting_list = list(ints)
                ints = []  
        if len(resulting_list) > 0:
            new_Fm = np.delete(Fm, resulting_list)
            new_Fc =np.delete(Fc, resulting_list)
            new_sigF = np.delete(sigF, resulting_list)
            new_res = np.delete(resolution, resulting_list)
        else:
            new_Fm =Fm
            new_Fc =Fc
            new_sigF = sigF
            new_res = resolution
        cutoffs_list = []
        noreflns = len(new_Fm)
        return new_Fm, new_Fc, new_sigF, new_res,i_table,isig_table, ru_table, rl_table,noreflns

    def drk_lim(self):
        """inserts plot limits to mirror DRKplot into normal probability plot tab"""
        self.x_min.setText("-4")
        self.x_max.setText("4")
        self.y_min.setText("-4")
        self.y_max.setText("4")

    def clr_lim(self):
        """removes plot limits from drk plot tab"""
        self.x_min.setText("")
        self.x_max.setText("")
        self.y_min.setText("")
        self.y_max.setText("")
    
    def clear_weights(self):
        """Clears all saved weights from weighting scheme table"""
        self.tablemodel = ""
        headers = ["a","b","goof","wr2","stop a","stop b","i cutoff","isig cutoff","resoln upper","resoln lower","no. of reflns","start a","start b","binning", "bin variance"]
        self.tablemodel = QtGui.QStandardItemModel() #internet says to make it a model to work
        self.tablemodel.setHorizontalHeaderLabels(headers)
        self.weighting_tableview.setModel(self.tablemodel)

    def send_weights(self):
        """Sends selected weights from weighting scheme table to normal probability plot tab"""
        #which row is selected?
        selectedindexes = self.weighting_tableview.selectedIndexes()
        #no selectedRows() function for tableview apparently, so have to get selected values
        row = [] #(i.row() for i in selectedindexes if i.row() not in row)]
        for i in selectedindexes:
            rowindex =  i.row()
            if rowindex not in row:
                row.append(rowindex)
        #making sure only one row has been selected
        if len(row) == 1:
            row_val = row[0]
            #gets selected values
            selected_a =str(self.tablemodel.item(row_val,0).text())
            selected_b = str(self.tablemodel.item(row_val,1).text())
            #sets a and b from tab one as selected values
            self.a_edit.setText(str(selected_a))
            self.b_edit.setText(str(selected_b))
            self.c_edit.setText("0.0")
            self.d_edit.setText("0.0")
            self.e_edit.setText("0.0")
            self.f_edit.setText("1/3")
        elif len(row) == 0:
            self.tab2_info.setText("Error: No row selected")
        else:
            self.tab2_info.setText("Error: More than one row selected")
            
if __name__ == '__main__':
    #import sys
    #from PyQt4 import QtGui
    app = QtGui.QApplication(sys.argv)
    main = Main(1.0) #scale factor used in weight calculation, code assumes it is one. Change here if not.
    main.show()
    sys.exit(app.exec_())
