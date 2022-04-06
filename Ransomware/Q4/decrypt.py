from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

input_file = 'encrypted4.txt' # Input file
# The key used for encryption (do not store/read this from the file)
with open('.key.txt', mode='rb') as file: # b is important -> binary
	key = file.read()
print('key', key)
print('key', len(key))

print(key)
print(len(key))
# Read the data from the file

file_in = open(input_file, 'rb') # Open the file to read bytes
iv = file_in.read(16) # Read the iv out - this is 16 bytes long
print(iv)
ciphered_data = file_in.read() # Read the rest of the data
print(ciphered_data)
file_in.close()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher
original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) # Decrypt and then up-pad the result
print(original_data)