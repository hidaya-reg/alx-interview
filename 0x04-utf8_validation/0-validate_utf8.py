#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0
    for byte in data:
        # Get the 8 least significant bits of the integer (byte)
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the character
            if (byte >> 7) == 0b0:
                num_bytes = 0  # 1-byte character
            elif (byte >> 5) == 0b110:
                num_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid starting byte
        else:
            # Check if it is a valid continuation byte
            if (byte >> 6) != 0b10:
                return False  # Not a valid continuation byte
            num_bytes -= 1

    return num_bytes == 0  # All bytes must be consumed
