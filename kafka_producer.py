
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(acks=0,
                         compression_type='gzip',
                         bootstrap_servers="192.168.56.107:9092,192.168.56.108:9092,192.168.56.112:9092",
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

def sending_data(string):
    # producer.send('peter-topic', value=bytes(string, encoding='utf8'))
    # producer.send('peter-topic', b'Hee')

    data = {'str': 'result '+string}
    producer.send('peter-topic', value=data)
    producer.flush()

if __name__=="__main__":
    text = "Hello This is Just test for using Kafka tool."
    for i in text.split(" "):
        print(f"보내는 값 {i}")
        sending_data(i)


    print("전송 완료")

