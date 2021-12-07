from domain.exceptions.application_error import ApplicationError


class ImageNotValid(ApplicationError):
    """Raised when the input image is not valid """

    def __init__(self, additional_message: str = ''):
        super().__init__(f'Image Not Valid {additional_message}')
