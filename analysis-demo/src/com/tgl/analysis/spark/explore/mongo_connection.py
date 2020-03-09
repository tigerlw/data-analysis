#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from pyspark.sql import SparkSession

# set PYSPARK_PYTHON to python36
#os.environ['PYSPARK_PYTHON'] = '/usr/bin/python36'

# load mongo data
input_uri = "mongodb://192.168.0.104:27017/ocsdb.flowlog"
output_uri = "mongodb://192.168.0.104:27017/ocsdb.flowlogtest"

my_spark = SparkSession\
    .builder\
    .appName("MyApp")\
    .config("spark.mongodb.input.uri", input_uri)\
    .config("spark.mongodb.output.uri", output_uri)\
    .config('spark.jars.packages','org.mongodb.spark:mongo-spark-connector_2.11:2.3.3')\
    .getOrCreate()

df = my_spark.read.format('com.mongodb.spark.sql').load()

df.show()

pas = df.toPandas()

print(pas.describe())

df.write.format('com.mongodb.spark.sql').mode('append').save()