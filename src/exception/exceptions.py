class UnauthorizedError(Exception):
    def __init__(self, message="Unauthorized!"):
        self.message = message
        self.code = -1
        self.http_status = 401

class ValidationErrorResponse(Exception):
    def __init__(self, errors):
        self.errors = errors
        self.code = -2
        self.http_status = 400

class UnexpectedError(Exception):
    def __init__(self, message="An unexpected error occurred"):
        self.message = message
        self.code = -3
        self.http_status = 500
