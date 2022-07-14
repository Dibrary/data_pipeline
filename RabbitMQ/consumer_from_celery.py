

import pika

class Consumer:
    def __init__(self):
        self.__url = '192.168.56.110'
        self.__port = 5672
        self.__vhost = '/'
        self.__cred = pika.PlainCredentials('temp', 'temp')
        self.__queue = '27833958-3bd5-32aa-b973-578986db8b92'
        # self.__queue = 'celeryev.5bb12304-ba32-4a3d-bb39-17971d466d8d'
        # 위 큐로는 이 문구만 계속 들어온다.Received b'{"hostname": "celery@localhost.localdomain", "utcoffset": -9, "pid": 2286, "clock": 946, "freq": 2.0, "active": 0, "processed": 6, "loadavg": [0.0, 0.02, 0.05], "sw_ident": "py-celery", "sw_ver": "5.1.2", "sw_sys": "Linux", "timestamp": 1657758444.1007519, "type": "worker-heartbeat"}'
        # <class 'bytes'>
        return

    def on_message(channel, method_frame, header_frame, body):
        print('Received %s' % body) # b'가 달려서 나온다. 즉, bytes 자료형으로 나온다.
        print(type(body))
        return

    def main(self):
        conn = pika.BlockingConnection(pika.ConnectionParameters(self.__url, self.__port, self.__vhost, self.__cred))
        chan = conn.channel()
        chan.basic_consume(
            queue = self.__queue,
            on_message_callback = Consumer.on_message,
            auto_ack = True # 메시지를 소비했을 때 자동으로 ack를 날리는 것이다. ack를 rabbitMQ에 전송하면 소비된 메시지는 제거된다.
        )
        print('Consumer is starting...')
        chan.start_consuming()
        return

consumer = Consumer()
consumer.main()


