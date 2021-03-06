from typing import Callable
from app.client.subscriber.subscriber import Subscriber
from ...common.broker_mode import BrokerMode
from .subscriber import Subscriber
from .integrated_subscriber import IntegratedSubscriber
from .direct_subscriber import DirectSubscriber


class SubscriberFactory:
    def __init__(self, broker_mode: BrokerMode, callback: Callable[[str, str], None]):
        self.__callback = callback
        self.__broker_mode = broker_mode

    def create(self, id: str) -> Subscriber:
        if self.__broker_mode == BrokerMode.INDIRECT:
            return IntegratedSubscriber(self.__callback, id)
        elif self.__broker_mode == BrokerMode.DIRECT:
            return DirectSubscriber(self.__callback)
        else:
            raise ValueError
