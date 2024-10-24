class InvalidInputException(Exception):
    def __init__(self, f: callable, *args):
        super().__init__()
        self.f = f
        self.args = args

    def __str__(self):
        return f"Values {self.args} violate {self.f.__name__}'s function domain"
