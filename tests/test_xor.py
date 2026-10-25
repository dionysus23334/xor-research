import unittest
from functools import reduce
from operator import xor

from experiments.xor_lab import prefix_xor, range_xor, xor_bytes


class XorTests(unittest.TestCase):
    def test_bit_truth_table(self):
        self.assertEqual([a ^ b for a in (0, 1) for b in (0, 1)], [0, 1, 1, 0])

    def test_identities_exhaustive(self):
        for a in range(256):
            self.assertEqual(a ^ a, 0)
            self.assertEqual(a ^ 0, a)
            for b in range(256):
                self.assertEqual(a ^ b, b ^ a)
                self.assertEqual((a ^ b) ^ b, a)
                self.assertEqual(a + b, (a ^ b) + 2 * (a & b))
        for a in range(16):
            for b in range(16):
                for c in range(16):
                    self.assertEqual((a ^ b) ^ c, a ^ (b ^ c))

    def test_ranges_against_direct_reduction(self):
        for values in ([], [0], [5, 3, 7, 3], [9, 9], [2**100, 3, 2**100]):
            prefix = prefix_xor(values)
            for left in range(len(values) + 1):
                for right in range(left, len(values) + 1):
                    self.assertEqual(range_xor(prefix, left, right), reduce(xor, values[left:right], 0))

    def test_invalid_inputs(self):
        for values in ([-1], [1.5], [True]):
            with self.assertRaises(ValueError):
                prefix_xor(values)
        for left, right in ((-1, 0), (1, 0), (0, 2)):
            with self.assertRaises(ValueError):
                range_xor(prefix_xor([5]), left, right)
        with self.assertRaises(ValueError):
            xor_bytes(b"a", b"ab")

    def test_bytes_and_reused_key(self):
        first, second, key = b"HELLO", b"WORLD", bytes([19, 42, 67, 91, 123])
        self.assertEqual(xor_bytes(xor_bytes(first, key), key), first)
        self.assertEqual(xor_bytes(xor_bytes(first, key), xor_bytes(second, key)), xor_bytes(first, second))
        self.assertEqual(xor_bytes(b"", b""), b"")


if __name__ == "__main__":
    unittest.main()
