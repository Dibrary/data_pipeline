
import pika

url = "localhost"
port = 5672
vhost = "mq_test"
cred = pika.PlainCredentials('guest', 'guest')
queue = 't_msg_q'

conn = pika.BlockingConnection(pika.ConnectionParameters(url, port, vhost, cred))
# print(conn)
# 정상으로 연결되면 에러 문구 없이
'''
<BlockingConnection impl=<SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x00000238B4249B08> params=<ConnectionParameters host=localhost port=5672 virtual_host=mq_test ssl=False>>>
출력된다.
'''
