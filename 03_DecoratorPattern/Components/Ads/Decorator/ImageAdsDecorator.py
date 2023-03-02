from ..IAdsComponent import IAdsComponent
from .IAddOnDecorator import IAddOnDecorator
import json


class ImageAdsDecorator(IAddOnDecorator):

    def __init__(self, ad_component: IAdsComponent):
        super().__init__(ad_component)
        self.ad_component = ad_component
        self._width = 320.0
        self._height = 480.0

    def get_ad_channel(self) -> str:
        return self.ad_component.get_ad_channel()

    def set_content(self, content: str) -> None:
        self.ad_component.set_content(content)

    def get_content(self) -> str:
        return self.ad_component.get_content()

    def get_description(self) -> dict:
        desc: dict = self.ad_component.get_description()
        desc.update({
            'width': self._width,
            'height': self._height
        })

        return desc

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, w: float) -> None:
        self._width = w

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, h: float) -> None:
        self._height = h


class GoogleImageAdDecorator(ImageAdsDecorator):

    @ImageAdsDecorator.width.setter
    def width(self, w: float) -> None:
        if w > 1920.0:
            self._width = 1920.0

        if w < 320.0:
            self._width = 320.0

    @ImageAdsDecorator.height.setter
    def height(self, h: float) -> None:
        if h > 1080.0:
            self._height = 1080.0

        if h < 480.0:
            self._height = 480.0


class MetaImageAdDecorator(ImageAdsDecorator):

    @ImageAdsDecorator.width.setter
    def width(self, w: float) -> None:
        if w > 1080.0:
            self._width = 1080.0

        if w < 320.0:
            self._width = 320.0

    @ImageAdsDecorator.height.setter
    def height(self, h: float) -> None:
        if h > 720.0:
            self._height = 720.0

        if h < 480.0:
            self._height = 480.0
