# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
file = 'ClassMatcherTest.csv'
import pandas as pd
from pandas import DataFrame
Data = pd.read_csv(file, encoding = 'latin-1', delimiter = ',', skiprows=None)

Data = Data.to_numpy()

Data = {'Name': Data[:,0], 'Number': Data[:,1], 'Class': Data[:,2]}
Data = DataFrame(Data, columns = ['Name', 'Number', 'Class'])


OrgData = Data.sort_values('Class')
print(OrgData)


