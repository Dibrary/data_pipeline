import pyspark
from partitioner import totalsByProd, products

sc = pyspark.SparkContext.getOrCreate()

missingProds = products.subtractByKey(totalsByProd).values
# missingProds객체는 method라고 나온다.
missingProds().foreach(lambda b: print(", ".join(map(str, b)))) # 출력을 하려면 method는 실행해줘야 함.
# 결과는 같다.

prodTotCogroup = totalsByProd.cogroup(products)
prodTotCogroup.collect()[:1]
'''
이렇게 하면 [(24, (<pyspark.resultiterable.ResultIterable object at 0x000001E30B97D7B0>,
                 <pyspark.resultiterable.ResultIterable object at 0x000001E30D51A4D0>))] 이렇게 나옴.

위 값중에 첫 번째꺼는 단일값(46973.67), 두 번째꺼는 리스트 나온다 (['24', 'LEGO Pirates', '4150.34', '2'])
'''
# 일일이 값 확인 해 보니 isEmpty에 해당되는 값은 [] 이다.

tmp = prodTotCogroup.filter(lambda x:x if [k for k in x[1][0]] == [] else None) # x가 iterable 객체라서 list comprehension으로 풀어서 비교함.
tmp.foreach(lambda x: print(", ".join(map(str, x[1][1]))))
'''
['3', 'Cute baby doll, battery', '1808.79', '2']
['63', 'Pajamas', '8131.85', '3']
['43', 'Tomb Raider PC', '2718.14', '1']
['20', 'LEGO Elves', '4589.79', '4']
'''