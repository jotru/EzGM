from EzGM import *
startTime = time()
# 1.) Create the cs object for record selection, check which parameters are required for the gmpe you are using.
cs = cs_master(Tstar = np.arange(0.4,2.4,0.2), gmpe = 'Boore_Atkinson_2008', database = 'NGA_W1', pInfo = 1)

# 2.) Create target spectrum
cs.create(site_param = {'vs30': 620}, rup_param = {'rake': 0.0, 'mag': [6.5, 6.0]}, 
          dist_param = {'rjb': [30, 50]}, Hcont=None, T_Tgt_range  = [0.1,4.5], 
          im_Tstar = 0.25, epsilon = None, cond = 1, useVar = 1, outdir = 'Outputs')   

# Plot target spectrum
cs.plot(tgt = 1, sim = 0, rec = 0, save = 1, show = 1)

# 3.) Select the ground motions
cs.select(nGM=30, selection=2, Sa_def='RotD50', isScaled = 1, maxScale = 4,
            Mw_lim=None, Vs30_lim=None, Rjb_lim=None, fault_lim=None, nTrials = 20,  
            weights = [1,2,0.3], seedValue  = 0, nLoop = 2, penalty = 0, tol = 10)   

# Plot the CS with simulated spectra and spectra of selected records
cs.plot(tgt = 0, sim = 1, rec = 1, save = 1, show = 1)

# 4.) Download selected ground motions from NGA-West2 Database [http://ngawest2.berkeley.edu/]
cs.nga_download(username = 'example_username', pwd = 'example_password123456')

# 5.) !!! Write the selected ground motions to the text files and locate in output directory
# You have to have records already inside Records.zip file for this option
# If database=='NGA_W2' you can first download the records via nga_download method and then use write option
cs.write(cs = 1, recs = 1)

# Calculate the total time passed
RunTime(startTime)