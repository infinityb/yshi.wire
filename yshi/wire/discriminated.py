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


class DiscriminatedSerDes(object):
    def __init__(self, serdes_list):
        self._serdes_list = serdes_list

    def serialize(self, thing):
        for idx, serdes in enumerate(self._serdes_list):
            try:
                return varint.serialize(idx) + serdes.serialize(thing)
            except:
                pass
        raise Exception("Couldn't serialize %r" % (thing, ))

    def buf_parse(self, buf, idx):
        option, idx = varint.buf_parse(buf, idx)
	if not 0 <= option < len(self._serdes_list):
            raise ValueError('Invalid data')
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
