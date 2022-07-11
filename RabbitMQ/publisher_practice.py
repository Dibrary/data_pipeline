
import pika

url = "localhost"
port = 5672
vhost = "mq_test"
cred = pika.PlainCredentials('guest', 'guest')
queue = 't_msg_q'

conn = pika.BlockingConnection(pika.ConnectionParameters(url, port, vhost, cred))
chan = conn.channel()
for i in range(20):
    chan.basic_publish(
        exchange="",
        routing_key=queue,
        body="Hello World "+str(i)
    )
conn.close()

print("정상 처리 완료")



