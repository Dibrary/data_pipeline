
import redis

conn = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)
# conn.set('test', '[Dibrary::hello world]')
# conn.set('test', '[Kwang::hello world]') # 이렇게 입력하면 2개가 들어가는게 아니다. 맨 마지막꺼만 들어감.

'''
CLI에서는 

(error) WRONGTYPE Operation against a key holding the wrong kind of value
이런 에러가 나면서 확인 못함.

'''

# conn.set('test', '[Dibrary::hello world]', '[Kwang::hello world]') # 이렇게는 못 넣는다.
key = 'temp'
conn.sadd(key, '[Dibrary::hello world]')
conn.sadd(key, '[kwang::hello world]')
conn.sadd(key, '[Seon::hello world]')

# 이렇게 넣으려 해도 위 WRONGTYPE 에러 난다.
# 이미 test라는 key가 있어서 그렇다. temp라고 만들면 에러 안남.
# sadd로 하면 CLI에서 확인 가능.


print("입력 완료.")





