from src.interface import QueryHandler


class CountHandler(QueryHandler):

    def __init__(self, name='count'):
        self._name = name
        self.counter = 0

    def process(self, query):
        if query:
            self.counter += 1

    @property
    def json(self):
        return self.counter


class TypeCountHandler(QueryHandler):

    def __init__(self, name='count_by_type'):
        self._name = name
        self.counter = {}

    def process(self, query):
        key = query['method']
        if key in self.counter:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

    @property
    def json(self):
        return self.counter


class TopFreqIpHandler(QueryHandler):

    def __init__(self, name='top_ip_by_freq', length: int = 3):
        self._name = name
        self.counter = {}
        self.length = length

    def process(self, query):
        key = query['ip']
        if key in self.counter:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

    @property
    def json(self):
        res = [(key, self.counter[key]) for key in sorted(self.counter, key=lambda x: self.counter[x], reverse=True)]
        return res[:self.length]


class TopSlowReqHandler(QueryHandler):

    def __init__(self, name='top_req_by_time', length: int = 3):
        self._name = name
        self.top = []
        self.length = length

    def process(self, query):
        self.top.append(query)
        self.top = [row for row in sorted(self.top, key=lambda x: x['time'], reverse=True)][:self.length]

    @property
    def json(self):
        return self.top
