from abc import ABC, abstractmethod


class IAdsComponent(ABC):

    def __init__(self):
        self.content: str = ''

    @abstractmethod
    def get_ad_channel(self) -> str:
        """
        Get ad channel, for example: google, meta, youtube, etc.
        :return: (string) ad channel
        """
        pass

    @abstractmethod
    def set_content(self, content: str) -> None:
        """
        Set the content
        :param content: (string)
        :return: None
        """
        pass

    @abstractmethod
    def get_content(self) -> str:
        """
        Get Content
        :return: (string)
        """
        pass
