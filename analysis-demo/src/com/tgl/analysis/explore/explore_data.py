# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

pd.set_option('display.max_rows',50000)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

inputfile = 'data/data.xls'

data = pd.read_excel(inputfile, index_col='rownum',usecols = [0,6, 7])


#data = data[data['tradeType']!=4]

print np.isnan(data).any()

print data.describe()