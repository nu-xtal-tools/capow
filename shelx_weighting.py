### For use with: CAPOW (calculation and plotting of optimised weights)    ###

#this version of weighting scheme ensures that fm less than zero is set to zero

import numpy as np
import math, sys
from copy import deepcopy

class shelx_weighting_calc():
    def __init__(self, n_independant_params, scale_factor,fm,fc,sigf,newres,bintype):
        self.sth = []
        self.fcf_weights = []
        self.F_v_F = []
        self.d = []
        self.sinth = []
        self.isig = []
        self.sinthl_lst = []
        self.grid_size = 9
        self.start_defined = False
        self.n_independant_params = n_independant_params 
        self.scale_factor = scale_factor
        ## basic setup ##
        self.F_c = fc
        fm_array = np.asarray(fm)
        set_to_zero = fm_array < 0
        fm_array[set_to_zero] = 0
        self.F_m = fm_array
        self.resoln = newres
        self.sig_F = sigf
        self.minimization_setup(bintype)
        self.error = ""

    def calculate_start(self,fo,fc,sig_fo):
        """code from cctbx, calculates grid search starting points"""
        sigmas_sq = sig_fo*sig_fo
        p = (fo + 2*fc)/3
        p2 = p*p
        x = sum(((fo-fc)**2-sig_fo)*(p2/sigmas_sq))
        y = sum((p2**2)/sigmas_sq)
        z = sum(p)
        start_a = np.sqrt(max(0.0001,0.64*x/max(1e-8,y)))
        start_b = 0.5*z*(start_a**2)/len(sig_fo)
        return start_a, start_b
    
    def compute_chi_sq(self,fo,fc,sig_fo,a,b): 
        """same as cctbx function"""
        ## vals - replace with array ###
        q = 1.0
        ####
        p = (fo + 2*fc)/3        
        s = sig_fo
        w = q/(s**2 + (a*p)**2 + b*p)
        w_tot = sum(w*np.square(fo-self.scale_factor*fc))
        if w_tot < 0:
                self.error_messages("chi less than zero: %f, %f" %(a, b)) 
        return w_tot

    def error_messages(self, message):
        self.error = message
        
    ##### make lists numpy arrays
    def minimization_setup(self,bintype):
        """setup for minimization grid search """
        fc = np.array(self.F_c)
        fo = np.array(self.F_m)
        sig_fo = np.array(self.sig_F)
        resolution = np.array(self.resoln)
        fo /= self.scale_factor
        sig_fo /= self.scale_factor
        if self.n_independant_params >= len(fo)/2:
            error_message= "Error: variance/goof value will be affected as number of independant parameters is greater than half of the total number of reflections."
            self.error_messages(error_message)
            self.good_to_go = False
        else:
            self.good_to_go = True
            ##### determing a and b starting values
            ##### sorting fc and fo for binning
            if bintype == "I":
                bin_ordering = fc/max(fc) #bins sorted into equal size bins, based on fc/fc(max)
            elif bintype == "R":
                bin_ordering = resolution/max(resolution)
            zipped = zip(bin_ordering, fo, fc,sig_fo) #list of tuples
            sort = sorted(zipped) #sorts them numerically based on first input list
            fc_sq = []
            fo_sq = []
            sigmas = [] #sorted sigma values to use in weight calculation
            bin_order_list = []
            for i in range(0,len(sort)): #adding sorted tuples from above into lists
                foz = sort[i][1]
                fcz = sort[i][2]
                sigmaz = sort[i][3]
                fc_sq.append(fcz)
                fo_sq.append(foz)
                sigmas.append(sigmaz)
                bin_val = sort[i][0]
                bin_order_list.append(bin_val)
            self.fc_sq = np.array(fc_sq)
            self.fo_sq = np.array(fo_sq)
            self.sigmas = np.array(sigmas)
            self.bin_val = np.array(bin_order_list)
            #### setting up binning
            self.n_bins = 10
            bin_max = 0
            self.bin_limits = [] #list
            self.bin_count = [] #number of vals in each bin
            for i in range(self.n_bins):
                self.bin_limits.append(int(math.ceil(i+1)*len(fc)/self.n_bins))
            self.bin_count.append(self.bin_limits[0])
            for i in range(self.n_bins-1):
                self.bin_count.append(self.bin_limits[i+1]-self.bin_limits[i])
            #otherwise would complain of being out of limits with i+1

            self.n = len(fo)//(len(fo)-self.n_independant_params) # double divide means no remainders, therefore function is not massively sensitive to number of independant params

    def minimize_variance(self,a_step_stop,b_step_stop, start_a, start_b):
            """grid search code - to find minimized variance between 10 bins"""
            if self.good_to_go == True:
                #### figuring out a and b, grid search
                grid_size = self.grid_size
                gridding = np.zeros([grid_size,grid_size])
                into_while = False
                all_var = []
                all_goof = []
                ab = []
                a_step = 0.2*start_a
                b_step = 0.4*start_b
                while(a_step > a_step_stop and b_step >b_step_stop):
                    into_while = True
                    binned_chi_sq = [deepcopy(gridding) for i in range(self.n_bins)] # think that will work
                    start_a = max(start_a, 4*a_step) - 4*a_step
                    start_b = max(start_b, 4*b_step) - 4*b_step
                    for i_bin in range(self.n_bins):
                        lower = self.bin_limits[i_bin] - (self.bin_count[i_bin])#1)
                        upper = self.bin_limits[i_bin]
                        fo2 = self.fo_sq[lower:upper]
                        fc2 = self.fc_sq[lower:upper]
                        sigma = self.sigmas[lower:upper]
                        b = start_b
                        for j in range(grid_size):
                            a = start_a
                            b += b_step
                            if b < 0:
                                b = 0
                            for k in range(grid_size):
                                a += a_step
                                if a < 0:
                                    a = 0
                                binned_chi_sq[i_bin][j,k] += self.compute_chi_sq(fo2,fc2,sigma, a, b) # returns sum(w*np.square(fo-scale_factor*fc)) which is numerator of chi squared
                    min_variance = 9e9
                    j_min, k_min = (0,0)
                    for j in range(grid_size):
                        for k in range(grid_size):
                            variance = 0
                            goofz = 0 #sum goofs
                            for i_bin in range(self.n_bins):
                                if self.bin_count[i_bin] == 0: continue
                                if binned_chi_sq[i_bin][j,k] < 0:
                                    variance == 999999 #would fail.
                                else:
                                    goof = math.sqrt(binned_chi_sq[i_bin][j,k]*self.n/self.bin_count[i_bin]) #which should give goof.
                                    goofz += goof
                                    variance += (goof-1)**2 #adding up because its variance for all bins
                            all_goof.append(goofz)
                            all_var.append(variance)
                            a_val = start_a + k*a_step
                            b_val = start_b + j*b_step
                            ab.append("%f, %f" %(a_val, b_val)) 
                            min_variance = min(variance, min_variance)
                            if variance == min_variance:
                                j_min = j
                                k_min = k
                    start_a += k_min*a_step
                    start_b += j_min*b_step
                    if k_min == grid_size-1: #originally 8
                        a_step *=2
                        continue
                    elif k_min != 0:
                        a_step /=4
                    if j_min == grid_size-1: #originally 8
                        b_step *= 2
                        continue
                    elif j_min != 0:
                        b_step /= 4
                    if start_a <= 1e-4: a_step /= 4 #edited to put this in
                    if start_b <= 1e-3: b_step /= 4
                if into_while == False:
                    error_message= "Error: Code did not make it to grid search stage as a and b step are too small. Increase weighting start points or decrease weighting stop points size and then try again."
                    self.error_messages(error_message)
                    #sys.exit()
                if start_a > 0.2:
                    start_a = 0.2
                    start_b = 0
                a, b = start_a, start_b

                def calcw(fo,fc,sig_fo,a,b):
                    """same as cctbx olex function, returns same value hopefully"""
                    global scale_factor
                    ## vals - replace with array ###
                    q = 1.0
                    ####
                    p = (fo + 2*fc)/3        
                    s = sig_fo
                    w = q/(s**2 + (a*p)**2 + b*p)
                    return w
                w_tot = calcw(self.fo_sq,self.fc_sq,self.sigmas,a,b)
                goof_now = np.sqrt(np.sum((w_tot*((self.fo_sq-self.fc_sq)**2))/(len(self.fo_sq)-225)))
                wrf = (np.sum((w_tot*((self.fo_sq-self.fc_sq)**2)))/(np.sum(np.sqrt(w_tot)*self.fo_sq)))
                def calc_variance_for_weight(fo_sq,fc_sq,sigmas,a,b):
                    variance = 0
                    final_bin_chi = []
                    #binned variance, the stopping condition for the a and b.
                    for i_bin in range(self.n_bins):
                            lower = self.bin_limits[i_bin] - (self.bin_count[i_bin])#1)
                            upper = self.bin_limits[i_bin]
                            fo2 = fo_sq[lower:upper]
                            fc2 = fc_sq[lower:upper]
                            sigma2 = sigmas[lower:upper]
                            final_bin_chi.append(self.compute_chi_sq(fo2,fc2,sigma2, a, b))
                    for i_bin in range(self.n_bins):
                            goof = math.sqrt(final_bin_chi[i_bin]*self.n/self.bin_count[i_bin]) #which should give goof.
                            variance += (goof-1)**2 #adding up because its variance for all bins
                    return variance
                variance = calc_variance_for_weight(self.fo_sq,self.fc_sq,self.sigmas,a,b)
                if into_while == False:
                    a = "-"
                    b = "-"
                    goof_now = "-"
                    wrf = "-"
                    variance = "-"
            else:
                a = "-"
                b = "-"
                goof_now = "-"
                wrf = "-"
                variance = "-"
                
            return a,b, goof_now, wrf,variance, self.error
