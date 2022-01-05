from kafka import KafkaConsumer

consumer = KafkaConsumer("SmartCar-Topic",
                         bootstrap_servers="master.hadoop.com:9092,slave1.hadoop.com:9092,slave2.hadoop.com:9092",
                         enable_auto_commit=True,
                         auto_offset_reset='latest')

def receive_message():
    for message in consumer:
        print("%s"%(message.value.decode('utf-8')))

if __name__=="__main__":
    receive_message()
    print("함수 실행 완료")