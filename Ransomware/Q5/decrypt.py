from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import math
import binascii
import time 
from Crypto.Random import get_random_bytes 
import socket
import sys
from Crypto.Hash import MD5

BLOCKSIZE = 256
h = MD5.new()
with open( 'R5.py' , 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        h.update(buf)
        buf = afile.read(BLOCKSIZE)
key = h.digest()
print(key)



with open( '.key.txt' , 'rb') as afile:
    buf = afile.read()
print(buf)

input_file = 'e2e2.txt' # Input file
print(len(key))
# Read the data from the file
file_in = open(input_file, 'rb') # Open the file to read bytes
iv = file_in.read(16) # Read the iv out - this is 16 bytes long
print(len(iv))
ciphered_data = file_in.read() # Read the rest of the data
print(len(ciphered_data))
file_in.close()

cipher = AES.new(buf, AES.MODE_CBC, iv=iv)  # Setup cipher
original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) # Decrypt and then up-pad the result
print(original_data)