from dependency_injector import containers, providers
from domain.services.contracts.abstract_character_extractor_service import AbstractCharacterExtractorService
from application.extractor.services.character_extractor_service import CharacterExtractorService


class Services(containers.DeclarativeContainer):

    # extractor
    character_extractor_service = providers.Factory(
        AbstractCharacterExtractorService.register(CharacterExtractorService))
