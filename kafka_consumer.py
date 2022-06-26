from kafka import KafkaConsumer

consumer = KafkaConsumer("peter-topic",
                         bootstrap_servers="192.168.56.107:9092,192.168.56.108:9092,192.168.56.112:9092",
                         enable_auto_commit=True,
                         auto_offset_reset='latest')

def receive_message():
    for message in consumer:
        print("%s"%(message.value.decode('utf-8')))

if __name__=="__main__":
    receive_message()
    print("함수 실행 완료")

