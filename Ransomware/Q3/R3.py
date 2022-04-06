# This is another obfuscated ransomware program (a bit moree challenging then R2.py!) 
# Your goal is to understand how the program works by breaking apart the obfuscation methods used.
# Once you understand how it works, please write a decryption program to decrypt encrypted3.txt

#Use the following link to read documentation on this imported library:
        #https://pycryptodome.readthedocs.io/en/latest/

# This is an AES block mode encryption, with data padded to make it a multiple pof 128-bits

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import Poly1305 
from lol import haha
from genPT import genPT
genPT()
input_file = 'plaintext3.txt' 
output_file = 'encrypted3.txt'
file_in = open(input_file, 'rb') 
iv = file_in.read(16) 
ciphered_data = file_in.read() 
file_in.close() 
def gm1305(data, key):
    mac1 = Poly1305.new(key=key, cipher=AES, data=data)
    return (mac1.hexdigest(), mac1.nonce)
def checksum(string): 
	csum = 0
	countTo = (len(string) // 2) * 2  
	count = 0
	while count < countTo:
		thisVal = ord(string[count+1]) * 256 + ord(string[count]) 
		csum = csum + thisVal 
		csum = csum & 0xffffffff  
		count = count + 2
	if countTo < len(string):
		csum = csum + ord(string[len(string) - 1])
		csum = csum & 0xffffffff 
	csum = (csum >> 16) + (csum & 0xffff)
	csum = csum + (csum >> 16)
	answer = ~csum 
	answer = answer & 0xffff 
	answer = answer >> 8 | (answer << 8 & 0xff00)
oof1 = haha()  
oof2 = haha() 
oof3 = haha() 
oof6 = str(oof1)
oof7 = str(oof2)
oof8 = str(oof3)
oof9 = oof6 + ' ' + oof7 + ' ' + oof8
of2 = '.key.txt'
file_out = open(of2, "w") 
file_out.write(oof9) # Write the varying length ciphertext to the file (this is the encrypted data)
file_out.close()
possKey = [b'\x8e\xb6\x934* f\xbd\xddr\xe2o\xb9\xb3<rjh\xe8iT\x80\xca\x17\xaaq\xe6\x93\x90\xec=\x86', b"\xa3.'A\xa9J\xea\n\r\xf2\xa5A\x8d\xd3\x88\xb7J\x9e\x903!\xcd\xba5&1\x97\xec\x16\n\xed\xf3", b'_\x8d\xa9>\xb9g\xddi!\xdbfG\x85a\xe6\xcd\xe0\xcf\x1aq\x03\xfay\x8axk\x89\xc9=$\x83\xc7']
keyList = []
for key in possKey:
    if key in keyList:
        keyList.append(key)
print(oof1)
print(oof2)
print(oof3)
a1 = AES.new(oof1, AES.MODE_CBC)
a2 = AES.new(oof2, AES.MODE_ECB)
a3  =AES.new(oof3, AES.MODE_CBC)
data = ciphered_data
cipher_text = a1.encrypt(pad(data, AES.block_size))
cipher_text2 = a2.encrypt(pad(cipher_text, AES.block_size))
cipher_text3 = a3.encrypt(pad(cipher_text2, AES.block_size))
iv = a1.iv
digestHex, noncePoly1305 = gm1305(data=data, key=oof1)
file_out = open(output_file, "wb") 
file_out.write(cipher_text3) 
file_out.close()
