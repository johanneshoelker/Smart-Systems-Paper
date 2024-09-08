import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


def getSMAData():
    path_errors = './errortimestamps.csv'
    path_features = './featureslist.csv'
    df_errors = pd.read_csv(path_errors)
    df_features = pd.read_csv(path_features)
    total_features = list(df_features[(df_features['True/False'] == 'TRUE') | (df_features['True/False'] == 'NotAvailable')]['Features'])
    tot_feat = pd.read_csv('./totfeat.csv')
    tot_feat = list(tot_feat['feat'])
    xtrain_dfs = {}
    xtest_dfs = {}
    ytrain_dfs = {}
    ytest_dfs = {}
    for inverter in range(19):
        inv = 'inv_'+str(inverter)
        tot_feat.append('ErrBits')
        df_inv_0 = pd.read_csv('./downsampledata/'+str(inverter)+'.csv')
        df_inv_0['Timestamp'] = pd.to_datetime(df_inv_0['Timestamp'])
        df_inv_0.sort_values(by='Timestamp', inplace=True)
        df_inv_0 = df_inv_0.set_index(df_inv_0['Timestamp'])
        df_inv_0.shape


        format = '%Y-%m-%d %H:%M:%S'
        error_date = datetime.strptime(df_errors[(df_errors['Inverter'] == inverter) & (df_errors['had_failure'] == True)]['failure_time'].values[0][0:19], format)
        start_date = error_date-timedelta(days= 60)
        end_date = error_date+timedelta(days= 1*30)
        split_date = error_date-timedelta(days= 1*30)

        df_inv_0 = df_inv_0[(df_inv_0.index > start_date) & (df_inv_0.index < end_date)]
        df_inv_0 = pd.get_dummies(df_inv_0)

        for feat in tot_feat:
            if feat not in df_inv_0.columns:
                df_inv_0[feat] = 0
        df_inv_0 = df_inv_0[tot_feat]
        df_inv_0 = df_inv_0.dropna()
        df_target = df_inv_0[['ErrBits']]
        tot_feat.remove('ErrBits')
        df_inv_0 = df_inv_0[tot_feat]

        xtrain, xtest = df_inv_0[(df_inv_0.index >= start_date) & (df_inv_0.index< split_date)], df_inv_0[(df_inv_0.index >= split_date) & (df_inv_0.index< end_date)]
        ytrain, ytest = df_target[(df_target.index >= start_date) & (df_target.index< split_date)], df_target[(df_target.index >= split_date) & (df_target.index< end_date)]
        print(xtrain.shape, xtest.shape)
        xtrain_dfs[inv] = xtrain
        xtest_dfs[inv] = xtest
        ytrain_dfs[inv] = ytrain
        ytest_dfs[inv] = ytest
    return xtrain_dfs, xtest_dfs, ytrain_dfs, ytest_dfs