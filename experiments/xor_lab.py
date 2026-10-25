"""Small reproducible XOR experiments; standard library only."""


def prefix_xor(values):
    """Return prefix XORs for non-negative Python integers."""
    result = [0]
    for value in values:
        if type(value) is not int or value < 0:
            raise ValueError("values must be non-negative integers")
        result.append(result[-1] ^ value)
    return result


def range_xor(prefix, left, right):
    """Query [left, right); prefix must come from prefix_xor."""
    if not 0 <= left <= right < len(prefix):
        raise ValueError("require 0 <= left <= right <= array length")
    return prefix[right] ^ prefix[left]


def xor_bytes(left, right):
    """XOR equal-length bytes, rejecting accidental truncation."""
    if len(left) != len(right):
        raise ValueError("inputs must have equal length")
    return bytes(a ^ b for a, b in zip(left, right))


def main():
    print(f"5 XOR 3 = {5 ^ 3}; (5 XOR 3) XOR 3 = {(5 ^ 3) ^ 3}")
    values = [5, 3, 7, 3]
    print(f"Array: {values}; XOR of [1:4] = {range_xor(prefix_xor(values), 1, 4)}")
    first, second = b"HELLO", b"WORLD"
    key = bytes([19, 42, 67, 91, 123])  # Fixed teaching example, not a secure key.
    c1, c2 = xor_bytes(first, key), xor_bytes(second, key)
    print("Reused-key relation:", xor_bytes(c1, c2).hex(), "=", xor_bytes(first, second).hex())


if __name__ == "__main__":
    main()
