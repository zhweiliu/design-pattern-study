from ..IAdsComponent import IAdsComponent
from .IAddOnDecorator import IAddOnDecorator
import json


class ImageAdsDecorator(IAddOnDecorator):

    def __init__(self, ad_component: IAdsComponent):
        super().__init__(ad_component)
        self.ad_component = ad_component
        self.ad_component.width = 320.0
        self.ad_component.height = 480.0

    def get_ad_channel(self) -> str:
        return self.ad_component.get_ad_channel()

    def set_content(self, content: str) -> None:
        self.ad_component.set_content(content)

    def get_content(self) -> str:
        channel = self.ad_component.get_ad_channel()
        image_desc = self.ad_component.get_content()
        return json.dumps({
            'channel': channel,
            'description': image_desc,
            'width': self.ad_component.width,
            'height': self.ad_component.height
        })


class GoogleImageAdDecorator(ImageAdsDecorator):

    @property
    def width(self) -> float:
        return self.ad_component.width

    @width.setter
    def width(self, w: float) -> None:
        if w > 1920.0:
            self.ad_component.width = 1920.0

        if w < 320.0:
            self.ad_component.width = 320.0

    @property
    def height(self) -> float:
        return self.ad_component.height

    @height.setter
    def height(self, h: float) -> None:
        if h > 1080.0:
            self.ad_component.height = 1080.0

        if h < 480.0:
            self.ad_component.height = 480.0


class MetaImageAdDecorator(ImageAdsDecorator):

    @property
    def width(self) -> float:
        return self.ad_component.width

    @width.setter
    def width(self, w: float) -> None:
        if w > 1080.0:
            self.ad_component.width = 1080.0

        if w < 320.0:
            self.ad_component.width = 320.0

    @property
    def height(self) -> float:
        return self.ad_component.height

    @height.setter
    def height(self, h: float) -> None:
        if h > 720.0:
            self.ad_component.height = 720.0

        if h < 480.0:
            self.ad_component.height = 480.0
