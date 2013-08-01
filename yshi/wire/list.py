from .varint import varint


class ListSerDes(object):
    def __init__(self, item_serdes):
        self._item_serdes = item_serdes

    def serialize(self, list_):
        buf = b''
        buf += varint.serialize(len(list_))
        for obj in list_:
            buf += self._item_serdes.serialize(obj)
        return buf

    def buf_parse(self, buf, idx):
        array_len, idx = varint.buf_parse(buf, idx)
        out = list()
        for _ in xrange(array_len):
            item, idx = self._item_serdes.buf_parse(buf, idx)
            out.append(item)
        return out, idx

    def parse(self, buf):
        data, idx = self.buf_parse(buf, 0)
        assert len(buf) == idx
        return data
