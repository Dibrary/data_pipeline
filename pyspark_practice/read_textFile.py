import pyspark
from parsing_func import extractInformation
sc = pyspark.SparkContext.getOrCreate()

data_from_file = sc.textFile("datas/VS14MORT.txt")




