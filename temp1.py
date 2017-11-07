#from pyspark.sql import SparkSession
#spark = SparkSession.builder.master("local")

#rdd1 = spark.sparkContext.parallelize(['a', 'b', 'c', 'd'])
#rdd2 = spark.sparkContext.parallelize([('a',[1,2,3]), ('b',[5,6,9])])

from pyspark.context import SparkContext as sc

lines = sc.textFile()
