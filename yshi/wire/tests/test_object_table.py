import unittest

import yshi.wire as wire
from yshi.wire import WireValueError


class TestWireObjecTable(unittest.TestCase):
    def test_basic(self):
        object_table = [
            None,
            list,
            object,
            'three'
        ]
        serdes = wire.ObjectTableSerDes(object_table)
        self.assertIs(serdes.loads(serdes.dumps(None)), None)
        self.assertIs(serdes.loads(serdes.dumps(list)), list)
        self.assertIs(serdes.loads(serdes.dumps(object)), object)
        self.assertEqual(serdes.loads(serdes.dumps('three')), 'three')
        self.assertRaises(WireValueError, serdes.dumps, 4)

if __name__ == '__main__':
    unittest.main()
