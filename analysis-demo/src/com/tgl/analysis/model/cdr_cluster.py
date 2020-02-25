# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from keras.layers.core import Activation, Dense
from keras.models import Sequential
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
from sklearn.manifold import TSNE
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import export_graphviz
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller as ADF


def programmer_7():
    """
    k：聚类中心数
    threshold：离散点阈值
    iteration：聚类最大循环次数
    """
    inputfile = 'data/data.xls'
    k = 3
    threshold = 8
    iteration = 500
    data = pd.read_excel(inputfile, index_col='rownum',usecols = [0,7,11])
    # 数据标准化
    data_zs = 1.0 * (data - data.mean()) / data.std()

    model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)
    model.fit(data_zs)

    # 标准化数据及其类别
    # 每个样本对应的类别

    #print(data_zs)

    r = pd.concat(
        [data_zs, pd.Series(model.labels_, index=data.index)], axis=1)
    r.columns = list(data.columns) + [u'聚类类别']

    norm = []
    for i in range(k):  # 逐一处理
        norm_tmp = r[['flowSize','wasteTime']][r[u'聚类类别'] == i] - \
            model.cluster_centers_[i]
        # 求出绝对距离
        norm_tmp = norm_tmp.apply(np.linalg.norm, axis=1)
        # 求相对距离并添加
        norm.append(norm_tmp / norm_tmp.median())

    norm = pd.concat(norm)
    # 正常点
    norm[norm <= threshold].plot(style='go')
    # 离群点
    discrete_points = norm[norm > threshold]
    discrete_points.plot(style='ro')

    print(len(discrete_points))

    # 标记离群点
    for i in range(len(discrete_points)):
        _id = discrete_points.index[i]
        n = discrete_points.iloc[i]
        print('_id:%s ; n:%d'%(_id,n))
        #plt.annotate('(%s, %0.2f)' % (_id, n), xy=(_id, n), xytext=(_id, n))

    plt.xlabel(u'编号')
    plt.ylabel(u'相对距离')
    plt.show()


if __name__ == "__main__":
    # programmer_1()
    # programmer_2()
    # programmer_3()
    # data_zs, r = programmer_4()
    # programmer_5(data_zs, r)
    # programmer_6()
    programmer_7()
    # programmer_8()
    pass