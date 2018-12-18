import platform
import sys
if platform.system() == 'Windows':
    sys.path.append('C:/Liang/abcpp_master/abcpp')
elif platform.system() == 'Darwin':
    sys.path.append('/Users/dudupig/Documents/GitHub/Code/Pro2/Python_p2')
#
# import os
# os.environ['R_HOME'] = 'C:\Program Files\R\R-3.5.1' #path to your R installation
# os.environ['R_USER'] = 'C:\Liang\Project2_cooperation\venv\Lib\site-packages\rpy2' #path depends on where you installed Python. Mine is the Anaconda distribution


import rpy2.robjects as robjects

# test : evaluating R code
robjects.r('''
        # create a function `f`
        f <- function(r, verbose=FALSE) {
            if (verbose) {
                cat("I am calling f().\n")
            }
            2 * pi * r
        }
        # call the function `f` with argument value 3
        f(3)
        ''')
