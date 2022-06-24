
'''
key로 데이터 찾고,
해당 데이터 없으면 추가하는 코드.
'''


import redis

conn = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)

key = 'flink'
# tmp_value = conn.smembers(key)
# print(tmp_value, type(tmp_value))
# 아무 값도 안 들어 있으면 set() <class 'set'> 으로 나온다.

id, title = input().split()

check_value = conn.smembers(key)
if check_value == set():
    print("없음")

    conn.sadd(key, f'[{id}]::[{title}]')
    print("들어감")
else:
    print(check_value)
    for set_value in check_value:

        ided, titled = set_value.decode('utf-8').split("::")
        # if ided != id and title != titled: # id와 title이 다른 경우 들어간다.
        # 위 조건문이 필요 없는게, 이미 있으면(id, title이 같으면) 안 들어간다.

        conn.sadd(key, f'[{id}]::[{title}]')
    print("기존 값에 추가")




# conn.sadd(key, '[Dibrary::hello world]')



