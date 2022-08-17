modbus_data = []

from collections import defaultdict

split_datas = defaultdict(list)

with open("C:\\Users\\kkdh8\\Desktop\\MODBUS.csv", encoding='utf8') as f:
    tmp = None
    for idx, x in enumerate(f):
        if x[0] == "/":
            continue
            # tmp = x
            # datas[tmp] = []
        else:
            row_data = list(x.split(","))
            modbus_data.append((row_data[2], row_data[1]))

'''
위 처럼 코드를 작성하면 

[('10001', '1'), // modbus주소, 값
 ('1002', '1'),
 ('10003', '1'),
 ('10004', '1'),
 ('10005', '1'),
 ('10006', '1'),
 ('10007', '1'),
 ('10008', '1'),
 ('10009', '1'),
 ('10010', '1'),
 ('10011', '1'),
 ('10012', '1'),
 ('10013', '1'),
 ('10014', '1'),
 ('10015', '1'),
 ('10016', '1'),
 ('10017', '1'),
 ('10018', '1'),
 ('10019', '1'),
 ('30001', '1'),
 ('10020', '1'),
 ('1', '1'),
 ('10021', '1'),
 ('2', '1'),
 ('3', '1')]
 
 데이터가 담긴다. 
'''