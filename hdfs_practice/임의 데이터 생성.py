import datetime
import random

with open(str(datetime.datetime.now())[:10] + "-data-log", "w", encoding='utf-8') as file:
    for month in range(1, 13):
        for d in range(1, 31):
            file.write("2022-"+str(month)+"-"+str(d)+","+str(random.random()*10)+ "\n")
        
print("생성 끝")



