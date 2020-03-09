from pyspark.sql import SQLContext
from pyspark.sql.types import *

from pyspark import SparkContext
from pyspark import SparkConf



conf = SparkConf()
conf.setAppName('liuwei')
conf.setMaster('local')
sc = SparkContext(conf=conf)

lines = sc.textFile('D:/learning/spark/spark-2.3.3-bin-hadoop2.7/README.md', 1)
counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)).reduceByKey(lambda x, y:x+y)

schema = StructType([
        StructField("name", StringType(), True),
        StructField("lettercount", LongType(), True)])

sqlContext = SQLContext(sc)
schemacc1 = sqlContext.createDataFrame(counts,schema)
schemacc1.registerTempTable("cc1")

result = sqlContext.sql("SELECT * FROM cc1 where lettercount>3")

data_ps = result.toPandas()

print data_ps.describe()


#result.show()
