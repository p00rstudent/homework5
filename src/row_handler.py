from src.interface import RowHandler


class TypeCountHandler(RowHandler):

    def __init__(self, name='count_by_type'):
        self._name = name
        self.counter = {}

    def process(self, row):
        key = row.split()[5][1:]
        if key in self.counter:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

    @property
    def json(self):
        return self.counter


class TopFreqIpHandler(RowHandler):

    def __init__(self, name='top_ip_by_freq', length: int = 3):
        self._name = name
        self.counter = {}
        self.length = length

    def process(self, row):
        key = row.split()[0]
        if key in self.counter:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

    @property
    def json(self):
        res = [(key, self.counter[key]) for key in sorted(self.counter, key=lambda x: self.counter[x], reverse=True)]
        return res[:self.length]


def parse_row(row):
    r_list = row.split()
    return {
        'method': r_list[5][1:],
        'url': r_list[6],
        'ip': r_list[0],
        'datetime': r_list[3] + r_list[4],
        'time': r_list[-1]
    }


class TopSlowReqHandler(RowHandler):

    def __init__(self, name='top_req_by_time', length: int = 3):
        self._name = name
        self.top = []
        self.length = length

    def process(self, row):
        self.top.append(parse_row(row))
        self.top = [row for row in sorted(self.top, key=lambda x: x['time'], reverse=True)][:self.length]

    @property
    def json(self):
        return self.top
