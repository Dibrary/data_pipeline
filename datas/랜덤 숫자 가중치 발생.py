import random

tmp = dict()
for i in range(100000):
    value = (random.choices([1,2,3,4,5],[98.5,0.24,0.24,0.24,0.24]))[0]
    if value not in tmp:
        tmp[value] = 1
    else:
        tmp[value] += 1
    # print(random.choices([1,2,3,4,5],[98.5,0.24,0.24,0.24,0.24])) # 이렇게 가중치를 줘서 값 뽑을 수 있다.

print(tmp)

'''
{1: 99073, 5: 227, 2: 253, 3: 219, 4: 228}
{1: 99022, 2: 234, 3: 227, 5: 279, 4: 238} 이렇게 나온다.

'''