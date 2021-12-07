from abc import ABC, abstractmethod, ABCMeta
import io


class AbstractCharacterExtractorService(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_characters_info(self, image: str) -> str: raise NotImplementedError

    @abstractmethod
    def get_characters_bounding_boxes(self, image: str) -> io.BytesIO: raise NotImplementedError
