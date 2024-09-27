#!/usr/bin/python3
"""UTF-8 Validation"""

from typing import List


def count_leading_set_bits(byte: int) -> int:
    """Count the number of leading 1 bits in the byte.

    Args:
        byte: An integer representing a byte (0-255).

    Returns:
        The count of leading 1 bits.
    """
    count = 0
    mask = 1 << 7

    while mask & byte:
        count += 1
        mask >>= 1

    return count


def validUTF8(data: List[int]) -> bool:
    """Check if a list of integers represents valid UTF-8 encoding.

    Args:
        data: A list of integers (0-255) representing bytes.

    Returns:
        True if the data is valid UTF-8, False otherwise.
    """
    bytes_to_process = 0
    for byte in data:
        if bytes_to_process == 0:
            bytes_to_process = count_leading_set_bits(byte)

            # 1-byte character (0xxxxxxx)
            if bytes_to_process == 0:
                continue

            # Check for valid leading bits (1-4 bytes)
            if bytes_to_process == 1 or bytes_to_process > 4:
                return False
        else:
            # Check if the current byte is of the form 10xxxxxx
            if not (byte & (1 << 7)) or (byte & (1 << 6)):
                return False

        bytes_to_process -= 1

    # All bytes processed should be accounted for
    return bytes_to_process == 0
