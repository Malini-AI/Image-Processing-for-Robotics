#!/usr/bin/env python
# coding: utf-8

from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd


df = pd.read_csv('orb.csv')
d = pd.pivot_table(df,index='col1',columns='col2',values='result')
d.fillna(0,inplace=True)
