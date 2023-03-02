from ..IAdsComponent import IAdsComponent
from .IAddOnDecorator import IAddOnDecorator


class AdsChannelDecorator(IAddOnDecorator):

    def __init__(self, ad_component: IAdsComponent, channel: str):
        super().__init__(ad_component)
        self.ad_channel: str = channel

    def get_ad_channel(self) -> str:
        return self.ad_channel

    def set_content(self, content: str) -> None:
        self.ad_component.set_content(content)

    def get_content(self) -> str:
        return self.ad_component.get_content()

    def get_description(self) -> dict:
        desc: dict = self.ad_component.get_description()
        # update channel information
        desc.update({
            'channel': self.ad_channel
        })
        return desc

