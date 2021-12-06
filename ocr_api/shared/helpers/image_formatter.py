import cv2
import numpy as np
import io


def from_bytes_to_np_array(image_bytes: str) -> np.ndarray:
    try:
        image_buffer = np.fromstring(image_bytes, np.uint8)
        image_np = cv2.imdecode(image_buffer, cv2.IMREAD_COLOR)
        return image_np
    except:
        return np.ndarray([])


def from_np_array_to_bytes(image_np: np.ndarray) -> io.BytesIO:
    try:
        _, encoded_img = cv2.imencode('.jpg', image_np)
        encoded_img = io.BytesIO(encoded_img.tobytes())
        return encoded_img
    except:
        return io.BytesIO()
