from typing import List

from domain.services.contracts.abstract_character_extractor_service import AbstractCharacterExtractorService


class CharacterExtractorService(AbstractCharacterExtractorService):

    def get_characters_info(self) -> List[List[str]]:
        return [['test']]