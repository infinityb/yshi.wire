from .varint import varint


class DiscriminatedSerDes(object):
    def __init__(self, serdes_list):
        self._serdes_list = serdes_list

    def serialize(self, thing):
        for idx, serdes in enumerate(self._serdes_list):
            try:
                return varint.serialize(idx) + serdes.serialize(thing)
            except:
                pass
        raise Exception("Couldn't serialize %r" % thing)

    def buf_parse(self, buf, idx):
        option, idx = varint.buf_parse(buf, idx)
        assert 0 <= option < len(self._serdes_list)
        return self._serdes_list[option].buf_parse(buf, idx)

    def parse(self, buf):
        data, idx = self.buf_parse(buf, 0)
        assert len(buf) == idx
        return data


class DiscriminatedSerDesBuilder(object):
    def __init__(self):
        self._serdes_list = list()

    def append(self, serdes):
        self._serdes_list.append(serdes)

    def build(self):
        return DiscriminatedSerDes(self._serdes_list)
