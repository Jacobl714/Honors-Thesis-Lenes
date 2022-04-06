import random

def genPT():
    output_file = 'p2.txt'
    i = 0
    string = ''
    while i < 50:
        string += random.choice(open('wordlist2.txt').read().split()).strip() + ' '
        i+=1
    string = string.encode('utf-8')
    file_out = open(output_file, "wb") 
    #file_out.write(cipher.iv) # Write the iv to the output file (will be required for decryption)
    file_out.write(string) # Write the varying length ciphertext to the file (this is the encrypted data)
    file_out.close()