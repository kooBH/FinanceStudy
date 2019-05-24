# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import datetime as dt 
from statsmodels.formula.api import ols 
import seaborn as sns;  sns.set()
import matplotlib.pyplot as plt

# https://seaborn.pydata.org/generated/seaborn.jointplot.html
def joint(target_1,target_2,col='Close',dur=240,eng='c'):
    ols_df1 = pd.read_csv('data/'+target_1 + '.csv',index_col='Date',engine = eng)
    ols_df1 = ols_df1[[col]]
    ols_df1.columns = [target_1]
    ols_df2 = pd.read_csv('data/'+target_2 + '.csv',index_col='Date',engine = eng)
    ols_df2 = ols_df2[[col]]
    ols_df2.columns = [target_2]
    new_df = pd.concat([ols_df1, ols_df2], axis=1, sort=False)
    new_df = new_df.dropna()
    new_df = new_df[-dur:]
    ret_index = new_df.pct_change()
    ret_index = ret_index.dropna()
    sns.jointplot(target_1, target_2, data = ret_index, kind='reg')

    
def isValid(target,start='2016-01-04',end='2018-12-28',eng='c'):
    val_df = pd.read_csv('data/'+target+ '.csv',index_col='Date',engine = eng)
    val_df = val_df[['Close']]
    val_df = val_df.loc[start:end]
    val_df.plot()
    