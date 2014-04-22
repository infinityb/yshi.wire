from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)
import unittest

import yshi.wire as wire
from yshi.wire import WireTypeError


class TestWireList(unittest.TestCase):
    def test_varint_list(self):
        serdes = wire.ListSerDes(wire.varint)
        self.assertEqual(serdes.loads(serdes.dumps([])), [])
        self.assertEqual(serdes.loads(serdes.dumps([1, 2, 3])), [1, 2, 3])
        self.assertRaises(WireTypeError, serdes.dumps, 4)
        self.assertRaises(WireTypeError, serdes.dumps, "asdf")
        self.assertRaises(WireTypeError, serdes.dumps, None)

if __name__ == '__main__':
    unittest.main()
