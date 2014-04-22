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
import six

# Shims
if six.PY3:
    unicode = str


from .varint import varint
from .exc import WireValueError, WireTypeError


def dumps_unicode(str_):
    str_bytes = str_.encode('utf8')
    try:
        return varint.dumps(len(str_bytes)) + str_bytes
    except TypeError as e:
        raise WireTypeError(e)
    except ValueError as e:
        raise WireValueError(e)


def buf_loads_unicode(buf, idx):
    byte_count, idx = varint.buf_loads(buf, idx)
    str_ = unicode(buf[idx:idx + byte_count], 'utf8')
    return str_, idx + byte_count


def loads_unicode(buf):
    data, offset = buf_loads_unicode(buf, 0)
    assert len(buf) == offset
    return data


class UnicodeSerDes(object):
    def dumps(self, num):
        return dumps_unicode(num)

    def buf_loads(self, buf, idx):
        return buf_loads_unicode(buf, idx)

    def loads(self, buf):
        return loads_unicode(buf)


unicode_ = UnicodeSerDes()
