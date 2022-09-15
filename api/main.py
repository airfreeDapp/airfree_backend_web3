from leanapi.server import ApiServer

from api.core.app_config import AppConfig
from api.modules import modules


def start():
    server = ApiServer.config(configs=AppConfig.load()).loads(modules).server()

    server.start(port=8000,host="127.0.0.1")


if __name__ == "_main_":
    start()

