# The MIT License (MIT)
#
# Copyright (c) 2013 Yasashii Syndicate
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


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
