from typing import List
from abc import ABC, abstractmethod, ABCMeta


class AbstractCharacterExtractorService(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_characters_info(self) -> List[List[str]]: raise NotImplementedError
