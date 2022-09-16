import pyspark
sc = pyspark.SparkContext.getOrCreate()

data = sc.parallelize([('A',22),('Al',23),('S',4),('Af',12),('Am',9)])
print(data) # ParallelCollectionRDD[0] at readRDDFromFile at PythonRDD 이렇게 나온다.
print(data.collect()) # type은 list로 나온다. 즉, 객체 내 데이터에 접근 가능해짐.

