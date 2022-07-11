
import pika

url = "localhost"
port = 5672
vhost = "mq_test"
cred = pika.PlainCredentials('guest', 'guest') # virtual host에 접근 권한이 부여된 계정 사용. (guest는 localhost에서만 가능)
queue = 't_msg_q'

conn = pika.BlockingConnection(pika.ConnectionParameters(url, port, vhost, cred))
chan = conn.channel()
for i in range(20):
    chan.basic_publish(
        exchange="", # 빈 값은 default exchange를 사용한다는 말.
        routing_key=queue,
        body="Hello World "+str(i)
    )
conn.close()

print("정상 처리 완료")



