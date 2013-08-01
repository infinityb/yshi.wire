

class TupleSerDes(object):
    def __init__(self, serdes):
        self._serdes = serdes

    def serialize(self, objs):
        buf = b''
        for obj, serdes_inst in zip(objs, self._serdes):
            buf += serdes_inst.serialize(obj)
        return buf

    def buf_parse(self, buf, idx):
        out = list()
        for serdes_inst in self._serdes:
            data, idx = serdes_inst.buf_parse(buf, idx)
            out.append(data)
        return tuple(out), idx

    def parse(self, buf):
        data, idx = self.buf_parse(buf, 0)
        assert len(buf) == idx
        return data


class TupleSerDesBuilder(object):
    def __init__(self):
        self._serdes = list()

    def append(self, serdes_inst):
        self._serdes.append(serdes_inst)

    def build(self):
        return TupleSerDes(self._serdes)
