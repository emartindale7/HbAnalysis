# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 10:24:43 2018

@author: martindale.40
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from scipy.optimize import curve_fit
import pandas as pd
import glob
import os
import sys



#Start off by assuming we are working in Windows
##############################################################################
#GET WORKING DIRECTORY
##############################################################################
for n,x in enumerate(os.listdir()):
    print("["+str(n)+"]: "+x)
    
#folder = input("Please enter the directory that you would like to work in:")
#folder = "C:/Users/martindale.40/Box Sync/Palmer Lab Research-Martindale/Hemoglobin_Purification/hHb Purification/TFF-hHb-48";
#print(folder);
#os.chdir(folder);
#print(os.listdir());
path = os.path.dirname(os.path.realpath(__file__));
path = path+"/test/";
##############################################################################

##############################################################################
#READ IN DATA FROM EXCEL FILE AND SAVE AS DATAFRAME OBJECTS
##############################################################################
file = path+"TFF-hHb-48_Batch_Data.xlsx";
excel = pd.ExcelFile(file);

sub = path+"/dataframes"
if not os.path.isdir(sub):
    os.makedirs(sub)

for x in excel.sheet_names:
        df = pd.read_excel(excel,x);
        df.to_pickle(sub+"/"+x+".pk1")
##############################################################################