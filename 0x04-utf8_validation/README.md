# 0x04. UTF-8 Validation
## Concepts Needed:
### 1. Bitwise Operations in Python:
- Understanding how to manipulate bits in Python, including operations like AND (``&``), OR (``|``), XOR (``^``), NOT (``~``), shifts (``<<``, ``>>``).
- [Python Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
### 2. UTF-8 Encoding Scheme:
<details>
<summary >Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.</summary>

#### UTF-8 encoding rules
UTF-8 (Unicode Transformation Format - 8-bit) is a variable-length character encoding that can represent every character in the Unicode character set. UTF-8 uses one to four bytes to encode characters, where each byte provides enough bits to represent specific ranges of code points.

##### 1. Encoding Rules
- UTF-8 uses 1 byte for ASCII characters (0-127).
- For characters above ASCII, UTF-8 uses between 2 and 4 bytes, depending on the Unicode code point.
- Each byte in a multi-byte sequence has a specific structure, where certain bits identify it as part of UTF-8 and indicate the byte position within the sequence.
##### 2. Byte Structures for Different Ranges
Each code point falls into one of the following categories, depending on the number of bytes needed:

| Code Point Range  | Byte Count | Byte Format in Binary                          |
|-------------------|------------|------------------------------------------------|
| U+0000 to U+007F  | 1 byte     | `0xxxxxxx`                                     |
| U+0080 to U+07FF  | 2 bytes    | `110xxxxx 10xxxxxx`                            |
| U+0800 to U+FFFF  | 3 bytes    | `1110xxxx 10xxxxxx 10xxxxxx`                   |
| U+10000 to U+10FFFF | 4 bytes | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`          |

##### 3. Explanation of Each Format
- **1 Byte (ASCII): `0xxxxxxx`**
    + Characters in the range ``U+0000`` to ``U+007F`` (standard ASCII) are encoded with a single byte.
    + Example: The character ``A`` (``U+0041``) is encoded in binary as ``01000001`` (1 byte).
- **2 Bytes: `110xxxxx 10xxxxxx`**
    + Characters from ``U+0080`` to ``U+07FF`` use two bytes.
    + The first byte starts with ``110``, followed by 5 bits of the code point.
    + The second byte starts with ``10``, followed by the remaining 6 bits.
    + Example: ``U+00A2`` (¢ symbol) in binary ``10100010`` is encoded as ``11000010 10100010``.
- **3 Bytes: `1110xxxx 10xxxxxx 10xxxxxx`**
    + Characters from ``U+0800`` to ``U+FFFF`` require three bytes.
    + The first byte starts with ``1110``, followed by 4 bits of the code point.
    + The second and third bytes start with ``10`` and hold the next 12 bits.
    + Example: ``U+20AC`` (Euro symbol €) in binary ``10000010101100`` is encoded as ``11100010 10000010 10101100``.
- **4 Bytes: ``11110xxx 10xxxxxx 10xxxxxx 10xxxxxx``**
    + Characters from ``U+10000`` to ``U+10FFFF`` (including emojis and less common symbols) use four bytes.
    + The first byte starts with ``11110``, followed by 3 bits of the code point.
    + The second, third, and fourth bytes start with ``10`` and cover the remaining 18 bits.
    + Example: ``U+1F600`` (Grinning Face emoji 😀) in binary ``11111011000000`` is encoded as ``11110000 10011111 10011000 10000000``.
##### 4. Rules for Decoding UTF-8
To decode UTF-8 bytes:
- Determine the number of bytes based on the leading bits:
    + ``0xxxxxxx``: 1 byte (ASCII)
    + ``110xxxxx``: 2 bytes
    + ``1110xxxx``: 3 bytes
    + ``11110xxx``: 4 bytes
- Strip the leading bits (e.g., ``110``, ``1110``) to extract the original bits for each byte.
- Concatenate the bits from all bytes and convert them back to the original Unicode code point.
##### 5. Example of UTF-8 Encoding Steps
Suppose we encode ``U+1F600`` (😀):
1. ``U+1F600`` in binary is ``11111011000000``.
2. Since it falls in the 4-byte range, we use the format: ``11110xxx 10xxxxxx 10xxxxxx 10xxxxxx``.
3. Mapping bits:
    - 11110 + 0001
    - 10 + 1111
    - 10 + 1001
    - 10 + 100000

4. Resulting byte sequence: 11110000 10011111 10011000 10000000.
This flexibility in byte length makes UTF-8 both space-efficient for ASCII text and capable of encoding the full range of Unicode characters.
</details>

<details>
<summary>Understanding the patterns that represent a valid UTF-8 encoded character.</summary>

#### UTF-8 Patterns
| Bytes | Bit Pattern                                     | Code Point Range | Description                                |
|-------|-------------------------------------------------|------------------|--------------------------------------------|
| 1     | `0xxxxxxx`                                      | U+0000 to U+007F | Standard ASCII (7-bit)                     |
| 2     | `110xxxxx 10xxxxxx`                             | U+0080 to U+07FF | Latin, Greek, Cyrillic, etc.               |
| 3     | `1110xxxx 10xxxxxx 10xxxxxx`                    | U+0800 to U+FFFF | Extended language characters               |
| 4     | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`           | U+10000 to U+10FFFF | Supplemental characters (e.g., emojis, historical scripts) |

##### Explanation of Each Pattern
- **1-Byte Sequence (ASCII):**
    + Pattern: ``0xxxxxxx``
    + The leading ``0`` indicates a single-byte character (ASCII).
    + This range (0x00 to 0x7F) is used for standard ASCII characters.
- **2-Byte Sequence:**
    + Pattern: ``110xxxxx 10xxxxxx``
    + The leading bits ``110`` indicate a two-byte character.
    + Valid for Unicode code points from U+0080 to U+07FF.
- **3-Byte Sequence:**
    + Pattern: ``1110xxxx 10xxxxxx 10xxxxxx``
    + The leading bits ``1110`` signal a three-byte character.
    + Used for Unicode code points from U+0800 to U+FFFF.
- **4-Byte Sequence:**
    + Pattern: ``11110xxx 10xxxxxx 10xxxxxx 10xxxxxx``
    + The leading bits ``11110`` indicate a four-byte character.
    + Used for higher code points, from U+10000 to U+10FFFF (e.g., emojis, rare language characters).
##### Rules for Valid UTF-8 Encoding
- Each multi-byte sequence must start with a unique lead byte (``110``, ``1110``, or ``11110``).
- Continuation bytes all have the format ``10xxxxxx``, which ensures they can only follow lead bytes, not start a character sequence.
- Overlong encodings (using more bytes than necessary) are invalid in UTF-8.
- Only code points up to U+10FFFF are allowed, matching the UTF-16 range.

These patterns help UTF-8 maintain compatibility with ASCII, efficiently encode most languages, and safely handle characters across diverse scripts.
</details>

- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4&ab_channel=Computerphile)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
### 3. Data Representation:
<details>
<summary>How to represent and work with data at the byte level.</summary>

Working with data at the byte level in Python involves understanding byte objects and binary data manipulation.

#### 1. Representing Byte Data
- **Bytes and Bytearray:**
    + ``bytes:`` An immutable sequence of bytes. It can be defined by either literal bytes (e.g., b"hello") or a sequence of integers (e.g., ``bytes([104, 101, 108, 108, 111])``).
    + bytearray: A mutable version of bytes, useful for modifying byte data in place.
```python
b1 = b"hello"  # bytes
b2 = bytearray(b"hello")  # bytearray
```
- **Hexadecimal Representation:**
    + A common way to work with raw byte data, where each byte is represented as two hexadecimal digits.
    + Use ``bytes.fromhex("68656c6c6f")`` to convert a hex string to bytes or ``b1.hex()`` to convert bytes to hex.
#### 2. Accessing Byte Data
Byte objects can be accessed like lists, where each element represents a single byte (an integer between 0 and 255).
```python
# Access individual bytes
print(b1[0])       # 104 (ASCII for 'h')
print(b2[1:3])     # bytearray(b'el')
```
#### 3. Byte Manipulation
- **Bitwise Operations:** You can perform bitwise operations (AND, OR, XOR, NOT) on each byte by iterating over the byte sequence.
```python
# Bitwise AND on each byte in b1 with 0b11110000
b3 = bytes([byte & 0b11110000 for byte in b1])
print(b3)  # modified bytes
```
- **Slicing:** Byte objects support slicing like strings and lists.
- **Concatenation:** Use ``+`` to concatenate byte sequences.
#### 4. Packing and Unpacking Bytes
- **``struct`` module:** Useful for converting between Python values and C structs in byte format.
```python
import struct
packed_data = struct.pack('I 2s f', 1025, b"ab", 3.14)
print(packed_data)  # byte representation of the data

# Unpack
unpacked_data = struct.unpack('I 2s f', packed_data)
print(unpacked_data)  # returns (1025, b'ab', 3.14)
```
#### 5. Binary I/O
Reading and writing bytes directly to files can be done in binary mode (``rb``, ``wb``).
```python
with open("data.bin", "wb") as f:
    f.write(b1)

with open("data.bin", "rb") as f:
    data = f.read()
    print(data)  # read as bytes
```
#### 6. Encoding and Decoding
- **Text to Bytes:** Encode text strings to bytes using encodings (UTF-8, ASCII).
```python
text = "Hello"
encoded_text = text.encode('utf-8')  # b'Hello'
```
- **Bytes to Text:** Decode bytes back to strings.
```python
decoded_text = encoded_text.decode('utf-8')  # 'Hello'
```
#### 7. Bit-Level Manipulation
To work at the bit level, first convert bytes to their binary form and apply bitwise operations as needed.
```python
# Convert to binary, operate, and return to bytes
binary_rep = ''.join(format(byte, '08b') for byte in b1)  # '0110100001100101011011000110110001101111'
```
Using these techniques, you can effectively handle and manipulate data at the byte level in Python, especially useful in applications like low-level protocol handling, binary file I/O, and encoding conversions.
</details>
<details>
<summary>Handling the least significant bits (LSB) of integers to simulate byte data.</summary>

To simulate byte data by manipulating the least significant bits (LSB) of integers, you can use bitwise operations to mask, set, clear, and shift bits. This approach allows fine control over individual bits, making it useful for scenarios like encoding, decoding, and embedded systems programming. 

#### 1. Extracting the LSBs of an Integer
To get the least significant ``n`` bits of an integer, use a mask with ``n`` bits set to 1:
```python
def get_lsb(integer, n):
    mask = (1 << n) - 1  # Creates a mask with `n` LSBs as 1
    return integer & mask
```
- ``1 << 3`` gives`` 0b1000`` (binary for 8).
- ``(1 << 3) - 1`` gives ``0b0111`` (binary for 7).
For example, to get the 3 least significant bits of the integer 5:
```python
get_lsb(5, 3)  # Output: 5 (binary: 101)
```
#### 2. Setting the LSBs of an Integer
You can set (turn on) the LSBs of an integer by OR-ing the integer with a mask.
```python
def set_lsb(integer, n):
    mask = (1 << n) - 1
    return integer | mask
```
For example, setting the 4 least significant bits of ``5``:
```python
set_lsb(5, 4)  # Output: 15 (binary: 1111)
```
#### 3. Clearing the LSBs of an Integer
To clear (turn off) the LSBs, use a mask with n bits set to 0 at the end and 1s elsewhere.
```python
def clear_lsb(integer, n):
    mask = ~((1 << n) - 1)
    return integer & mask
```
Clearing the 3 least significant bits of ``13``:
```python
clear_lsb(13, 3)  # Output: 8 (binary: 1000)
```
#### . Toggling the LSBs of an Integer
To flip or toggle the LSBs, XOR the integer with a mask.
```python
def toggle_lsb(integer, n):
    mask = (1 << n) - 1
    return integer ^ mask
```
For example, toggling the 3 least significant bits of ``7``:
```python
toggle_lsb(7, 3)  # Output: 0 (binary: 000)
```
#### 5. Shifting LSBs
- **Right Shifting:** Move bits to the right, effectively discarding the LSBs.
```python
shifted_right = integer >> n
```
- **Left Shifting:** Move bits to the left, filling the LSBs with zeros.
```python
shifted_left = integer << n
```

By manipulating the LSBs, you gain fine control over how data is represented, which is especially helpful in binary encoding, cryptography, and data compression.
</details>

### 4. List Manipulation in Python:
- Iterating through lists, accessing list elements, and understanding list comprehensions.
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
### 5. Boolean Logic:
- Applying logical operations to make decisions within the program.

## Additional Resource
[Mock Technical Interview](https://www.youtube.com/watch?v=QvqvMxg24gY&ab_channel=InterviewPen)

## Tasks
### 0. UTF-8 Validation
Write a method that determines if a given data set represents a valid UTF-8 encoding.
- Prototype: ``def validUTF8(data)``
- Return: ``True`` if data is a valid UTF-8 encoding, else return ``False``
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
```bash
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
```
