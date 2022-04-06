#This is where you need to write your own python script in order to decrypt 
# the obfuscated ransomware program R2.py.  
# Feel free to use any resources from other questions. 

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes 
from varGen import generateVar
 