from abc import ABCMeta, abstractmethod
from ..IAdsComponent import IAdsComponent


class IAddOnDecorator(IAdsComponent, metaclass=ABCMeta):
    def __init__(self, ad_component: IAdsComponent):
        super().__init__()
        self.ad_component = ad_component
