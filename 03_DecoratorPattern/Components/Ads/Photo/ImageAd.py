from ..IAdsComponent import IAdsComponent


class ImageAd(IAdsComponent):

    def __init__(self, image_uri: str):
        super().__init__()
        self.content = image_uri

    def get_ad_channel(self) -> str:
        return 'Image ads'

    def set_content(self, image_uri: str) -> None:
        self.content = image_uri

    def get_content(self) -> str:
        return self.content
