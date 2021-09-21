class LogHandler:

    def __init__(self, handlers: list = None):
        self.handlers = handlers or list()

    def process(self, row):
        if row:
            query = self.split_row(row)
            if query:
                for handler in self.handlers:
                    handler.process(query)
            else:
                pass

    @staticmethod
    def split_row(row: str):
        try:
            return {'ip': row.split()[0],
                    'datetime': row.split('[')[1].split(']')[0],
                    'method': row.split('"')[1].split()[0],
                    'url': row.split('"')[1].split()[1],
                    'time': int(row.split()[-1])}
        except IndexError:
            return None

    @property
    def json(self):
        return [{handler.name: handler.json} for handler in self.handlers]
