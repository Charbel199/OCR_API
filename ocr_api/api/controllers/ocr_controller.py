from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from domain.exceptions.application_error import ApplicationError
from containers import Services

router = APIRouter()
character_extractor_service = Services.character_extractor_service()


@router.post('/content')
async def get_image_content(image: UploadFile = File(...)) -> str:
    try:
        return character_extractor_service.get_characters_info(await image.read())
    except ApplicationError as e:
        raise HTTPException(status_code=400, detail=e.__str__())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())


@router.post('/characters')
async def get_characters_bounding_box(image: UploadFile = File(...)) -> StreamingResponse:
    try:
        image_bytes = character_extractor_service.get_characters_bounding_boxes(await image.read())
        return StreamingResponse(content=image_bytes, media_type="image/png")
    except ApplicationError as e:
        raise HTTPException(status_code=400, detail=e.__str__())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())
