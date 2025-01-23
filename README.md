# Vietnamese Number Converter

A Python utility that converts Vietnamese number words into numerical values. This tool can handle complex Vietnamese number expressions including large numbers up to the billions (tỷ tỷ).

## Features

- Converts Vietnamese number words to integers
- Supports numbers from 0 to billions of billions
- Handles special Vietnamese number cases like "mươi", "lăm", "linh/lẻ"
- Supports formal and colloquial number expressions

## Usage
```python
from num import vietnamese_to_number

## Basic Usage
print(vietnamese_to_number("một trăm hai mươi ba")) # Output: 123
print(vietnamese_to_number("một tỷ")) # Output: 1000000000
```

### Running from Command Line

You can also run the script directly:
```bash
python num.py 
```


Then enter your Vietnamese number when prompted.

## Examples

Here are some example conversions:

- "một trăm hai mươi ba" → 123
- "hai mươi tư" → 24
- "không trăm linh năm" → 5
- "một tỷ hai trăm triệu" → 1200000000
- "một tỷ tỷ" → 1000000000000000000

## Supported Number Words

### Basic Numbers
- không (0)
- một (1)
- hai (2)
- ba (3)
- bốn/tư (4)
- năm/lăm (5)
- sáu (6)
- bảy (7)
- tám (8)
- chín (9)
- mười (10)

### Multipliers
- trăm (hundred - 100)
- nghìn (thousand - 1,000)
- vạn (ten thousand - 10,000)
- triệu (million - 1,000,000)
- tỷ (billion - 1,000,000,000)

### Special Cases
- mươi/mười (tens)
- linh/lẻ (zero in tens place)
- lăm (five, used in special cases)
