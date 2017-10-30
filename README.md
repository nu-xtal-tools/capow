# capow
Calculating and plotting optimal weights

#Introduction

CAPOW is a graphical user interface to operate two programs; one to produce normal probability plots and another to calculate the optimal a and b parameters for a SHELXL weighting scheme. The SHELXL weighting scheme has six variables which can be defined by the user (a-f). For a refinement on F2:
w=  q/(σ_(F^2)^2+(ap)^2+bp+d+e sin⁡θ 

where p = f F_o^2+(1-f)F_c^2 and q varies depending on the sign of parameter c: q = 1.0 when c = 0, q = exp⁡(c(sin⁡θ/λ)^2)  when c > 0, and q = 1 - exp⁡(c(sin⁡θ/λ)^2)  when c > 0.

Optimal a and b parameters are routinely calculated for data refined in a variety of refinement programs, with the other parameters (c, d, e = 0 and f = 1/3) remaining fixed.

#Requirements

The code has been written using python 2.7.5 and requires, PyQt4 (4.10.1), matplotlib (2.0.2), numpy (1.12.1), scipy (0.19.0) and the provided scripts to create the gui (window_tab.py) and calculate weighting scheme (shelx_weighting.py). The source code has been tested on Scientific Linux 7.0 and Windows 8 and has been written with no operating system requirements.

The program works with either a .fcf (SHELXL LIST 4 or 8) or .fco (XD2016) file and requires two other files to get additional information about the refinement.

Required files:

.fcf - .cif and .ins/.res

.fco - .cif and .mas

.cif file provides the number of independent parameters applied to refinement while the .ins/.mas file gives wavelength, weight applied and unit cell parameters.

#Operating the Program

Starting the program

The program can be run from the command line in Linux by typing the name of your python script ‘python’ followed by the name of the script ‘capow.py’. e.g. ‘python capow.py’. This also applies to windows operating system.

Opening a file

To select an .fco/.fcf file, click on the ‘Select File’ option on the toolbar. Click on the Select File option within that list. This will bring up a file dialog which will allow you to select an .fcf or.fco file. The code will then look for a file with the same name cif and ins file (fcf) or \_lsm.cif and .mas file (fco) with the same name as the selected file. If these do not exist, you will be prompted to select one. 

#Editing Normal Probability Plot

After you have selected a file, a normal probability plot will be drawn using the currently applied weighting scheme according to the mas/ins file in the Normal Probability Plot tab. Any cutoffs that were applied to the data will NOT be applied here. 
You have the option of changing the weighting scheme applied, using the boxes labelled a-f above the plot. Cutoffs to data can be changed by selecting the desired inequality from the dropdown boxes on the right hand side of the plot. I < 1 for example, means display only reflections that have an I of less than one.

The plot axes can also be changed by filling in the boxes labelled x and y with numbers. The ‘DRK’ button sets limits to -4 and 4, as in DRKplot. ‘Clr’ removes values from these boxes.

To apply the desired changes, click ‘Apply’ button. If there is an error, it should be displayed in the information box, below the apply button.

Information about the normal probability plot, weighting scheme applied, no of reflections in plot, will be visible in this box.
If a reflection is clicked on, information about that reflection (and others closeby) is displayed in this box. The reflection indicies (h,k,l) alongside structure factors, standard uncertainties and position of the reflection on the graph. If more than 25 reflections are close by, nothing will be printed. To investigate densely populated areas of reflections, use the magnifying glass button to zoom into the area on the graph and try again.

Calculating optimal a and b parameters

Operation of script

After an fco/fcf file has been input, it is possible to calculate optimal a and b parameters by clicking the ‘calculate weighting parameters’ button. A number of options exist for the data to be used.
To use the starting a and b values for the grid search as calculated using a and b, ensure ‘Calculate Start’ box is checked. If not, weighting start points are required to be entered in the boxes provided.
Weight can be binned based on intensity or resolution, depending on which box checked.
The stopping point of the grid search can be adjusted from the codes original default of (a = 0.0001 and b = 0.005) using the boxes provided.

The data can also be filtered using the weighting cutoffs boxes. Select the appropriate inequality and enter the desired number in the corresponding box. I > 1, means that only reflections with I > 1 will be used in the calculation.
Below these options is a small text box that will provide information if there are any errors in operation. The table below this will display the calculated a and b values alongside other information about the data used once weighting schemes have been calculated.
If ‘ – ‘ appears for a, b, goof and wr2 when the weighting is calculated, this means the code has been unable to reach the grid search stage, adjust either the stopping points (make them smaller) or the starting points (make sure calculate start is unchecked if you choose to do this) and try again. For multipole data we have found it best to reduce a and b stopping points to at least a = 0.00001 and b = 0.0005, though smaller values will get closer to the true minimum bin variance.
To send a set of calculated a and b values to the normal probability tab, select the desired row by clicking on it. It should now be highlighted. Then click ‘Send Weights to Tab1’ and the weights in the normal probability plot will now be the calculated ones.
To clear the table of information, select ‘clear weights’.
