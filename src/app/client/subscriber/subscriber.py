from threading import Thread
from typing import Callable
import zmq
from abc import ABC, abstractmethod


class Subscriber(ABC):
    def __init__(self, callback: Callable[[str, str], None], id: str = None):
        self._callback = callback
        self.__id = id
        self.__context = zmq.Context.instance()
        self._new_sub_endpoint = 'subscribe'
        self.__send_new_sub_socket = self.__context.socket(zmq.PAIR)
        self.__send_new_sub_socket.bind(f'inproc://{self._new_sub_endpoint}')
        self._background_thread.start()

    def subscribe(self, topic: str) -> None:
        self.__send_new_sub_socket.send_string(topic)

    @property
    @abstractmethod
    def _background_thread(self) -> Thread:
        pass

    def __del__(self):
        self.__send_new_sub_socket.close()
        self.__context.term()
