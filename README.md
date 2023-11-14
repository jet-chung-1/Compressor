# Compressor Package


This Compressor package is a Python library for data compression using Huffman and Shannon coding. It allows you to efficiently compress and decompress data, making it useful for various applications. For example, we simulated some sensor data and showed that we can compress the data from needing 8 bits to an average of around 5.4 bits.

## Features

- Data compression using Huffman and Shannon coding.
- Calculations of average code length, entropy.
- Efficient handling of CSV data.
- Simple and easy-to-use interface.

## Usage




   ```python
   from encoder.encoder import Encoder

   # assume we have access to a pmf of words to encode
   
   # returns a dictionary codebook
   huffman_code = encoder.get_huffman_code(pmf)
   shannon_code = encoder.get_shannon_code(pmf)
   