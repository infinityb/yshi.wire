import unittest

import yshi.wire as wire


class TestWireTuple(unittest.TestCase):
    def test_wire_tuple(self):
        serdes = wire.TupleSerDes([
            wire.varint, wire.string
        ])
        self.assertEqual(serdes.loads(serdes.dumps((1, "one"))), (1, "one"))
        self.assertRaises(wire.WireTypeError, serdes.dumps, (1, 2))
        self.assertRaises(wire.WireTypeError, serdes.dumps, 1)
        self.assertRaises(wire.WireTypeError, serdes.dumps, "one")
        self.assertRaises(wire.WireTypeError, serdes.dumps, object())


if __name__ == '__main__':
    unittest.main()
