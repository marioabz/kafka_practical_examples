
import os
from dotenv import load_dotenv
load_dotenv()


class Config:

    def __init__(self, ):

        self.TOPIC = os.getenv("TOPIC")
        self.GROUP_ID = os.getenv("GROUP_ID", None)
        self.SERVER = os.getenv("SERVER", None)
        self.PORT = os.getenv("BROKER_PORT", None)
        self.BOOTSTRAP_SERVER = f"{self.SERVER}:{self.PORT}"

config = Config()
