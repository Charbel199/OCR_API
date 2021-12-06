from fastapi import APIRouter, HTTPException
from typing import List
from domain.exceptions.application_error import ApplicationError
from containers import Services

router = APIRouter()
character_extractor_service = Services.character_extractor_service()


@router.post('/content')
async def get_image_content() -> List[List[str]]:
    try:
        return character_extractor_service.get_characters_info()
    except ApplicationError as e:
        raise HTTPException(status_code=400, detail=e.__str__())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())

