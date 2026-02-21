from fastapi import status

class DomainException(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(message)
        
class UserExistsError(DomainException):
    def __init__(self, message: str):
        super().__init__(
            message=message, 
            status_code=status.HTTP_409_CONFLICT
        )
        
class UserDoesNotExistsError(DomainException):
    def __init__(self, message):
        super().__init__(
            message=message,
            status_code=status.HTTP_404_NOT_FOUND
        )
        