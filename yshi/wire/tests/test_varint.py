import unittest

import yshi.wire as wire


class TestWireVarInt(unittest.TestCase):
    def test_field_existing(self):
        self.assertEqual(wire.varint.loads(wire.varint.dumps(4)), 4)
        self.assertRaises(wire.WireTypeError, wire.varint.dumps, "4")

if __name__ == '__main__':
    unittest.main()
