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
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import struct
import numbers
from .exc import WireTypeError


_int128_fmt = '!QQ'


def dumps_int128(num):
    if not isinstance(num, numbers.Integral):
        raise WireTypeError("num must be integral")
    if not 0 <= num < 2 ** 128:
        raise ValueError(
            'Out of bounds; {} not in 0 <= x < 2 ** 128'.format(num))
    high = (num >> 64) & (2 ** 64 - 1)
    low = num & (2 ** 64 - 1)
    return struct.pack(_int128_fmt, high, low)


def buf_loads_int128(buf, pos):
    struct_size = struct.calcsize(_int128_fmt)
    high, low = struct.unpack('!QQ', buf[pos:pos + struct_size])
    return (high << 64) + low, pos + struct_size


def loads_int128(buf):
    data, offset = buf_loads_int128(buf, 0)
    assert len(buf) == offset
    return data


class Int128SerDes(object):
    def dumps(self, num):
        return dumps_int128(num)

    def buf_loads(self, buf, idx):
        return buf_loads_int128(buf, idx)

    def loads(self, buf):
        return loads_int128(buf)


int128 = Int128SerDes()
