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


_SELF_CHECKS = [True]


def disable_self_checks():
    _SELF_CHECKS[0] = False


def _assertEquals(left, right, message=None):
    if message:
        assert (left == right), "%r != %r: %s" % (left, right, message)
    else:
        assert (left == right), "%r != %r" % (left, right)


def _do_check(func, *a, **kw):
    assert(_SELF_CHECKS[0])
    _SELF_CHECKS[0] = False
    try:
        return func(*a, **kw)
    finally:
        _SELF_CHECKS[0] = True


def _varint_read_byte(byte):
    """returns (value, is_terminal)"""
    return (ord(byte) >> 1), bool(ord(byte) & 1)


def serialize_varint(num):
    num_tmp = int(num)
    things = list()
    while True:
        things.append((num_tmp & 0x7F) << 1)
        num_tmp >>= 7
        if not num_tmp:
            break
    things[0] = things[0] | 1
    obuf = b''.join(map(chr, reversed(things)))
    if _SELF_CHECKS[0]:
        _assertEquals(_do_check(parse_varint, obuf), num, "serialize_varint")
    return obuf


def buf_parse_varint(buf, idx):
    acc = 0
    sidx = idx
    while True:
        value, is_terminal = _varint_read_byte(buf[idx])
        acc = (acc << 7) | value
        assert(((acc << 7) & value) == 0)
        idx += 1
        if is_terminal:
            break
    if _SELF_CHECKS[0]:
        _assertEquals(
            _do_check(serialize_varint, acc), buf[sidx:idx],
            "buf_parse_varint"
        )
    return acc, idx


def parse_varint(buf):
    data, offset = buf_parse_varint(buf, 0)
    assert len(buf) == offset
    return data


class VarIntSerDes(object):
    def serialize(self, num):
        return serialize_varint(num)

    def buf_parse(self, buf, idx):
        return buf_parse_varint(buf, idx)

    def parse(self, buf):
        return parse_varint(buf)


varint = VarIntSerDes()
