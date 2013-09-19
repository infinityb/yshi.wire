import unittest

import yshi.wire as wire
from yshi.wire import WireTypeError


class TestWireString(unittest.TestCase):
    def test_field_existing(self):
        self.assertEqual(wire.string.loads(wire.string.dumps("")), "")
        self.assertEqual(wire.string.loads(wire.string.dumps("4")), "4")
        self.assertRaises(WireTypeError, wire.string.dumps, None)
        self.assertRaises(WireTypeError, wire.string.dumps, 4)
        self.assertRaises(WireTypeError, wire.string.dumps, object())


if __name__ == '__main__':
    unittest.main()
