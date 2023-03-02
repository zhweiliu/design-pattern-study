from ..IAdsComponent import IAdsComponent
from .IAddOnDecorator import IAddOnDecorator


class TextAdsDecorator(IAddOnDecorator):

    def __init__(self, ad_component: IAdsComponent):
        super().__init__(ad_component)
        self.ad_component = ad_component

    def get_ad_channel(self) -> str:
        return self.ad_component.get_ad_channel()

    def set_content(self, content: str) -> None:
        self.ad_component.set_content(content)

    def get_content(self) -> str:
        return self.ad_component.get_content()

    def get_description(self) -> dict:
        return self.ad_component.get_description()
