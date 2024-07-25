
import sys
import time
import pickle
import logging

from msg_intfcs.protos import msg_pb2
from load_config import config
from kafka import KafkaProducer

results = list()
state = set()

TOPIC = config.TOPIC

logging.root.setLevel(logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))


def run_producer():
    logging.info("LETS PRODUCE ------------")
    producer = KafkaProducer(bootstrap_servers=config.BOOTSTRAP_SERVER,)
    return producer


producer = run_producer()


def permutation(array: list[int], results):

    """
        P(n, r) = n!/(n - r)! ;;;
        C(n, r) = P(n,r) / r! = n!/[(n-r)!*r!]
    """

    if len(array) == 1:
        return array

    for i, w in enumerate(array):
        compl = permutation(array[0:i] + array[i + 1:], results)
        if compl is None:
            continue
        perm = tuple([w] + compl)
        if len(perm) == 2 and perm not in state:
            results.append(perm)
            state.add(perm)
            msg = msg_pb2.Permutation(
                id=i, permutation=bytes(perm)
            )
            logger.info(f"Perm: {perm}")
            logger.handlers[0].flush()
            producer.send(TOPIC, msg.SerializeToString())
            time.sleep(0.5)


if __name__ == "__main__":
    results = list()
    permutation([1,2,3,4,5], results)
