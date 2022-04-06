import random
import os

def genPT():
    output_file = 'p2.txt'
    lines = open('wordlist.txt').read().splitlines()
    string1 = random.choice(lines).strip()
    string2 = random.choice(lines).strip()
    string1 = string1.encode('utf-8')
    string2 = string2.encode('utf-8')
    file_out = open(output_file, "wb") 
    file_out.write(string1) # Write the varying length ciphertext to the file (this is the encrypted data)
    file_out.write(b'\n') # Write the varying length ciphertext to the file (this is the encrypted data)
    file_out.write(string2) # Write the varying length ciphertext to the file (this is the encrypted data)
    file_out.close()
    print('Q4: index of the text are:' + str(string1[0:3]) + " & " + str(string2[0:3]))

output_file2 = '.key.txt'
def generateVar():
    key = os.urandom(16)
    return key

size = [64,128,256,512,1024,2048,4096]

genPT()
#key = generateVar()
#print(key)
search_text = b'haitham'
replace_text = random.choice(size)
print(replace_text)
with open(r'R0.py', 'r') as file:
    data = file.read()
    data = data.replace(str(search_text), str(replace_text))
with open(r'R5.py', 'w') as file:
    file.write(data)
