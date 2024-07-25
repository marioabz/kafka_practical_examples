
import pickle, time, sys
from msg_intfcs.protos import msg_pb2
import logging
from load_config import config
from kafka import KafkaConsumer, TopicPartition

logging.root.setLevel(logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))

def run_consumer():
    try:
        logger.info("STARTING TO CONSUME ----------------")
        topic = config.TOPIC
        consumer = KafkaConsumer(
            enable_auto_commit=True,
            bootstrap_servers=config.BOOTSTRAP_SERVER,
        )

        """
        topic_partition = TopicPartition(topic, 0)
        consumer.assign([topic_partition])
        print(topic_partition)
        consumer.seek_to_beginning(topic_partition)
        """

        consumer.subscribe( topics=[topic,] )

        for i, msg in enumerate(consumer):
            serialized_msg = msg_pb2.Permutation()
            perm = serialized_msg.FromString(msg.value)
            logger.info(f"Offset: {msg.offset}, Perm: {tuple(perm.permutation)}")
            logger.handlers[0].flush()
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("Bye")


if __name__ == "__main__":
    run_consumer()
