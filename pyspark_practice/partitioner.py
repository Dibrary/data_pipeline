import pyspark
sc = pyspark.SparkContext.getOrCreate()

RDD = sc.parallelize(range(1, 10000))
tmp = RDD.map(lambda x:(x, x*x))
tmp.take(5) # [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

RDD.map(lambda x:(x, x*x)).reduceByKey(lambda x, y: x+y).count()


import random
list = [random.randint(0, 100) for _ in range(500)]
rdd = sc.parallelize(list, 30).glom()
# type(rdd)는 ParalleCollectionRDD 라고 나온다.

rdd.collect() # 16개로 묶인 list가 30개 있다.
# collect()값을 사용하려면 변수에 담아놓고 쓰는게 빠르다.
# 계속 collect()를 쓰면 시간 걸림.

rdd.count() # 30 나온다.


tranFile = sc.textFile("datas/data_transactions.txt")
tranData = tranFile.map(lambda x: x.split("#"))
transByProd = tranData.map(lambda x:(int(x[3]), x))
# [3]번째 값이 0번째에 추가된 tuple로 구성됨

totalsByProd = transByProd.mapValues(lambda t: float(t[5]))
# 위 값은 첫 번째 값과, 5번째 값이 하나의 그룹으로 만들어진다. 이때 totalsByProd는 PipelineRDD다.
totalsByProd.take(3)
# [(68, 9506.21), (86, 4107.59), (58, 2987.22)]

temp = []
for k in totalsByProd.collect():
    temp.append((lambda x, y:x+y)(k[0],k[1]))
temp[:3] # 결과는 [9574.21, 4193.59, 3045.22] 근데 이 결과를 원한게 아니다.

from operator import add
rdd = sc.parallelize(totalsByProd.collect())
totalsByProd = rdd.reduceByKey(add) # 이렇게 할 수도 있고,
totalsByProd[:3] # [(68, 62133.9), (24, 46973.67), (48, 50163.71000000001)]

temp2 = totalsByProd.reduceByKey(lambda x, y:x+y)
temp2.take(3) # [(68, 62133.899999999994), (86, 86316.57), (58, 186539.8)]


products = sc.textFile("datas/data_products.txt").map(lambda x:x.split("#")).map(lambda x:(int(x[0]), x))
products.take(1) # [(1, ['1', 'ROBITUSSIN PEAK COLD NIGHTTIME COLD PLUS FLU', '9721.89', '10'])]]

totalsAndProds = totalsByProd.join(products) # 상품 ID가 같은 것 끼리 묶임
totalsAndProds.first() # (24, (46973.67, ['24', 'LEGO Pirates', '4150.34', '2']))

totalsWithMissingProds = products.leftOuterJoin(totalsByProd)
#(6, (['6', 'LEGO Castle', '4777.51', '10'], 43252.97))
totalsWithMissingProds = totalsByProd.rightOuterjoin(products)

missingProds = totalsWithMissingProds.filter(lambda x: x if x[1][0] == None else None).map(lambda x: x[1][1])
# PipelineRDD
missingProds.first() # ['43', 'Tomb Raider PC', '2718.14', '1']

missingProds.foreach(lambda b: print(", ".join(map(str, b))))
'''
3, Cute baby doll, battery, 1808.79, 2
63, Pajamas, 8131.85, 3
20, LEGO Elves, 4589.79, 4
43, Tomb Raider PC, 2718.14, 1
'''