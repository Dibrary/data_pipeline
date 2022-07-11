
import pika

class Consumer:
    def __init__(self):
        self.__url = 'localhost'
        self.__port = 5672
        self.__vhost = 'mq_test'
        self.__cred = pika.PlainCredentials('guest', 'guest')
        self.__queue = 't_msg_q'
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
            auto_ack = True
        )
        print('Consumer is starting...')
        chan.start_consuming()
        return

consumer = Consumer()
consumer.main()







'''
socket.gaierror: [Errno 11001] getaddrinfo failed
위 에러가 나면 IP주소가 맞지 않는 경우다.
'''