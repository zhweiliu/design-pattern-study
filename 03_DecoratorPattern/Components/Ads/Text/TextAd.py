from ..IAdsComponent import IAdsComponent


class TextAd(IAdsComponent):

    def __init__(self, text: str):
        super().__init__()
        self.content = text

    def get_ad_channel(self) -> str:
        return 'Text ads'

    def set_content(self, content: str) -> None:
        self.content = content

    def get_content(self) -> str:
        return self.content

    def get_description(self) -> dict:
        return {
            'content': self.content
        }
