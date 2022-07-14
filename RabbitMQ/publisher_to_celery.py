

import pika

url = "192.168.56.110"
port = 5672
vhost = "/"
cred = pika.PlainCredentials('temp', 'temp') # virtual host에 접근 권한이 부여된 계정 사용. (guest는 localhost에서만 가능)
queue = '27833958-3bd5-32aa-b973-578986db8b92' # 여기서 Celery 실행으로 생긴 Queue name을 사용하면 안 들어가진다.

conn = pika.BlockingConnection(pika.ConnectionParameters(url, port, vhost, cred))
chan = conn.channel()
for i in range(20):
    chan.basic_publish(
        exchange="", # 빈 값은 default exchange를 사용한다는 말.
        routing_key=queue,
        body=f"1, {i}"
    )
conn.close()

print("정상 처리 완료")


'''
셀러리를 사용해서 계산하면
셀러리 업무가 rabbitMQ에 자동으로 큐가 생성되면서 비동기 방식으로 처리가 되고 반환된다.

그 셀러리가 생성한 큐에 직접 파이썬으로 넣어줄 필요가 없다.
'''