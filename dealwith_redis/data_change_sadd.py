import redis

conn = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)

tmp_value = conn.smembers('temp')
print(tmp_value, type(tmp_value))


# print(tmp_value.decode('utf-8'), type(tmp_value.decode('utf-8')))
# sadd로 넣은 데이터는 decode가 안 됨. 정확히는 set 자체라서 안 됨. 한 줄씩은 될까?

for k in tmp_value:
    print(k.decode('utf-8')) # 한 줄씩 decode는 된다.

print("가져오기 완료.")

print(conn.keys()) # 이렇게 하면 전체 키들 모두 볼 수 있다.

# conn.flushall() # 이거 하면 전체 key 지워진다.
