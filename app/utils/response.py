class Response:
    success = False
    data = None
    errorMessage = ""

    def __init__(self, success, data, errorMessage):
        self.success = success
        self.data = data
        self.errorMessage = errorMessage
