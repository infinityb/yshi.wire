from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)
import unittest

import yshi.wire as wire
from yshi.wire import WireTypeError


class TestWireDiscriminated(unittest.TestCase):
    def test_discriminated(self):
        serdes = wire.DiscriminatedSerDes([
            wire.TupleSerDes([wire.varint, wire.string]),
            wire.TupleSerDes([wire.varint, wire.varint]),
        ])
        self.assertEqual(
            serdes.loads(serdes.dumps((1, "one"))),
            (1, "one")
        )
        self.assertEqual(
            serdes.loads(serdes.dumps((2, 2))),
            (2, 2)
        )
        self.assertRaises(WireTypeError, serdes.dumps, ("asdf", "asdf"))


if __name__ == '__main__':
    unittest.main()
