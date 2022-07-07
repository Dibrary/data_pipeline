from kafka import KafkaProducer

producer = KafkaProducer(acks=1,
                         compression_type='gzip',
                         bootstrap_servers='192.168.56.107:9092,192.168.56.108:9092,192.168.56.112:9092')

for i in range(1, 11):
    if i%2 == 1:
        producer.send('peter-topic', key='1', value='%d - key=1' )
    else:
        producer.send('peter-topic', key='2', value='%d - key=1')