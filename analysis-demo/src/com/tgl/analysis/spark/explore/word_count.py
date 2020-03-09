#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
#from __future__ import print_function

import sys
from operator import add

#os.environ['SPARK_HOME']="D:\learning\spark\spark-2.3.3-bin-hadoop2.7"
#sys.path.append("D:\learning\spark\spark-2.3.3-bin-hadoop2.7\python")



from pyspark import SparkContext
from pyspark import SparkConf


if __name__ == "__main__":
   # if len(sys.argv) != 2:
        # print("Usage: wordcount <file>", file=sys.stderr)
        # exit(-1)
    conf = SparkConf()
    conf.setAppName('liuwei')
    conf.setMaster('local')
    sc = SparkContext(conf=conf)
    #sc._jsc.hadoopConfiguration().set("fs.s3a.access.key", "AKIA5IIEQNDDWXRIZYX5")
    #sc._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "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")
    lines = sc.textFile('D:/learning/spark/spark-2.3.3-bin-hadoop2.7/README.md', 1)
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    sc.stop()
