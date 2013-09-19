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

from .exc import WireTypeError


class TupleSerDes(object):
    def __init__(self, serdes):
        self._serdes = serdes

    def dumps(self, objs):
        buf = b''
        try:
            iterable = zip(objs, self._serdes)
        except TypeError:
            raise WireTypeError("Bad type")
        for obj, serdes_inst in iterable:
            buf += serdes_inst.dumps(obj)
        return buf

    def buf_loads(self, buf, idx):
        out = list()
        for serdes_inst in self._serdes:
            data, idx = serdes_inst.buf_loads(buf, idx)
            out.append(data)
        return tuple(out), idx

    def loads(self, buf):
        data, idx = self.buf_loads(buf, 0)
        assert len(buf) == idx
        return data


class TupleSerDesBuilder(object):
    def __init__(self):
        self._serdes = list()

    def append(self, serdes_inst):
        self._serdes.append(serdes_inst)

    def build(self):
        return TupleSerDes(self._serdes)
