# Kafka config examples with Python and Protobuf

Basic kafka setups with Kafka broker,controller with Python3 services,
consumer and producer exchanging messages serialized with Protobuf.

Why?
No good reason besides experimentation

## Instructions
* Set carefully .env
* Install locally `protoc` to compile ProtoBuf schemas
* Run: `cp kafka_configs/<file> compose.yml`
* Run:  ```docker-compose up```
* Logs should show controller and broker working, receiving messages from app/producer.py
* If `compose.multi-controller-single-broker.yml` is selected, make sure to update th file .env accordingly

## Next experiments
* streams
* schema registers
* multi controller config
* Pipelining with other data processing tools
