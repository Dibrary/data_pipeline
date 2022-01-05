
from kafka import KafkaProducer
producer = KafkaProducer(acks=1,
                         compression_type="gzip",
                         bootstrap_servers="192.168.85.5:9092,192.168.85.6:9092,192.168.85.7:9092")

def sending_data(string):
    producer.send('SmartCar-Topic', value=bytes(string, encoding='utf8'))

if __name__=="__main__":
    text = "Hello This is Just test for using Kafka tool."
    for i in text.split(" "):
        sending_data(i)
    print("전송 완료")

