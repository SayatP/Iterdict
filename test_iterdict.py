import unittest
from iterdict import IterDict


class TestIdict(unittest.TestCase):
    def setUp(self):
        _dict = {"key": "val", "otherkey": "therval"}
        self.idict = IterDict(_dict)
        self.keylist = ["key", "otherkey"]

    def testiter(self):
        res = []
        while True:
            try:
                n = next(self.idict)
                res.append(n)
            except StopIteration:
                break

        self.assertEqual(len(res), len(self.keylist))
        self.assertTrue(all(i in self.keylist for i in res))


if __name__ == "__main__":
    unittest.main()
