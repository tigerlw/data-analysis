# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import MySQLdb
import pandas.io.sql as sql



def describe_data():
    inputfile = 'data/data.xls'

    data = pd.read_excel(inputfile, index_col='rownum', usecols=[0, 7, 11])

    # data = data[data['tradeType']!=4]

    print data.describe()


def distribute_data():
    inputfile = 'data/data.xls'
    data = pd.read_excel(inputfile, index_col='rownum', usecols=[0,7])

    print data['flowSize']

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.hist(sorted(data['flowSize']), bins=100)
    plt.xlabel('flowSize')
    plt.ylabel('ttt')
    plt.show()


def read_data_mysql():
    conn = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8')
    dataframe = sql.read_sql_query("select flowtag,cnt,total_flow,accum_flow,percent from cdr_rs",conn)

    df = dataframe.set_index('flowtag')

    df = df['cnt']

    df.plot()
    plt.show()











if __name__ == "__main__":
    pd.set_option('display.max_rows', 50000)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    np.set_printoptions(suppress=True)
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    #describe_data()
    #distribute_data()
    read_data_mysql()

