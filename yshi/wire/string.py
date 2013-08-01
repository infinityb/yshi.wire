from .varint import varint


def serialize_string(str_):
    return varint.serialize(len(str_)) + str_


def buf_parse_string(buf, idx):
    byte_count, idx = varint.buf_parse(buf, idx)
    return buf[idx:idx + byte_count], idx + byte_count


def parse_string(buf):
    data, offset = buf_parse_string(buf, 0)
    assert len(buf) == offset
    return data


class StringSerDes(object):
    def serialize(self, num):
        return serialize_string(num)

    def buf_parse(self, buf, idx):
        return buf_parse_string(buf, idx)

    def parse(self, buf):
        return parse_string(buf)


string = StringSerDes()
