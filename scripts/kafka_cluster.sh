# Script to create a Kafka cluster
# Using Bitnami Kafka Helm Chart

# First, we need to create a namespace for the Kafka cluster
# This is done by running the following command:

helm install location bitnami/kafka

# Kafka can be accessed by consumers via port 9092 on the following DNS name from within your cluster:       

# `location-kafka.default.svc.cluster.local`

# Each Kafka broker can be accessed by producers via port 9092 on the following DNS name(s) from within your 
# cluster:

# `location-kafka-0.location-kafka-headless.default.svc.cluster.local:9092`

# To create a pod that you can use as a Kafka client run the following commands:

kubectl run location-kafka-client --restart='Never' --image docker.io/bitnami/kafka:2.8.1-debian-10-r73 --namespace default --command -- sleep infinity
