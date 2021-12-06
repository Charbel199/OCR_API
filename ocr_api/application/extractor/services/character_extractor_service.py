import cv2
import numpy as np
import io
from domain.services.contracts.abstract_character_extractor_service import AbstractCharacterExtractorService
import pytesseract
from sys import platform
from shared.helpers.image_formatter import from_bytes_to_np_array, from_np_array_to_bytes
from typing import List
from domain.models.character_info import CharacterInfo

# Windows testing only
if platform == 'win32':
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


class CharacterExtractorService(AbstractCharacterExtractorService):

    def _get_character_coordinates(self, image_np: np.ndarray) -> List[CharacterInfo]:
        boxes = pytesseract.image_to_boxes(image_np)
        characters_info = []
        for box in boxes.splitlines():
            character_info = box.split(' ')
            character, x, y, w, h, _ = character_info
            characters_info.append(CharacterInfo(character=character, x=int(x), y=int(y), h=int(h), w=int(w)))

        return characters_info

    def get_characters_info(self, image: str) -> str:
        # Get image from endpoint
        image_np = from_bytes_to_np_array(image)

        # Get content from image
        content = pytesseract.image_to_string(image_np)
        # Format content if necessary

        return content

    def get_characters_bounding_boxes(self, image: str) -> io.BytesIO:
        # Get image from endpoint
        image_np = from_bytes_to_np_array(image)
        height, width, _ = image_np.shape

        # Get necessary coordinates
        characters_info = self._get_character_coordinates(image_np)

        # Draw bounding boxes
        for character_info in characters_info:
            cv2.rectangle(image_np, (character_info.x, height - character_info.y),
                          (character_info.w, height - character_info.h), (255, 0, 255), 1)
            cv2.putText(image_np, character_info.character,
                        (character_info.x, height - character_info.y + 30),
                        cv2.FONT_HERSHEY_PLAIN,
                        2,
                        (255, 0, 255),
                        1,
                        cv2.LINE_AA)
        image_bytes = from_np_array_to_bytes(image_np)

        return image_bytes
