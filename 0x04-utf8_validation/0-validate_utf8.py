#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # For each integer in the data
    for num in data:
        # Get the binary representation of the current integer
        bin_rep = format(num, '#010b')[-8:]

        # If this is the case then we have an incomplete character
        if n_bytes == 0:
            # Get number of 1s in the beginning of the binary representation
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            # 1 <= n_bytes <= 4, otherwise it's an invalid UTF-8 character
            if n_bytes == 0 or n_bytes > 4 or n_bytes == 1:
                continue

        # Else, we are in the middle of a UTF-8 character
        else:
            # Else, the current byte should be 10xxxxxx
            if not (bin_rep.startswith('10')):
                return False

        # Decrement the number of bytes we have left to read
        n_bytes -= 1

    # If we didn't finish reading a character, it's an invalid UTF-8
    return n_bytes == 0
