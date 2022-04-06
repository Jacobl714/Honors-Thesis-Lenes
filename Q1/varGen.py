import os
output_file2 = '.key.txt'
def generateVar():
    key = os.urandom(16)
    return key
