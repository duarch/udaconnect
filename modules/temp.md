To create a pod that you can use as a Kafka client run the following commands:

    kubectl run my-location-kafka-client --restart='Never' --image docker.io/bitnami/kafka:2.8.1-debian-10-r57 --namespace default --command -- sleep infinity
    kubectl exec --tty -i my-location-kafka-client --namespace default -- bash

    PRODUCER:
        kafka-console-producer.sh --broker-list my-location-kafka-0.my-location-kafka-headless.default.svc.cluster.local:9092 --topic location

    CONSUMER:
        kafka-console-consumer.sh --bootstrap-server my-location-kafka.default.svc.cluster.local:9092 --topic location 
        kafka-console-consumer.sh --bootstrap-server my-location-kafka.default.svc.cluster.local:9092 --topic location --from-beginning
```
