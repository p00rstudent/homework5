class LogHandler:

    def __init__(self, handlers: list = None):
        self.handlers = handlers or list()

    def process(self, row):
        if row and len(row.split()) == 19:
            for handler in self.handlers:
                handler.process(row)

    @property
    def json(self):
        return [{handler.name: handler.json} for handler in self.handlers]



