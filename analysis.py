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
#print (sys.argv)

#Start off by assuming we are working in Windows
#folder = input("Please enter the directory that you would like to work in:")
folder = "C:/Users/martindale.40/Box Sync/Palmer Lab Research-Martindale/Hemoglobin_Purification/hHb Purification/TFF-hHb-48";
#print(folder);
os.chdir(folder);
#print(os.listdir());
file = "TFF-hHb-48_Batch_Data.xlsx";
excel = pd.ExcelFile(file);

Input = pd.read_excel(excel, "Input");
washLysis = pd.read_excel(excel, "WashLysis");
TFF = pd.read_excel(excel, "TFF");
spectra = pd.read_excel(excel, "Spectra");

print(Input.head())
print(washLysis.head())
print(TFF.head())
print(spectra.head(1))