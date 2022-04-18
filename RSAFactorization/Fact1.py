from ctypes import sizeof
from gettext import find
import random
import math
from typing import List
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey.RSA import construct
from generatePT import genPT
import binascii
import sys
import os 
import csv
from Crypto.Util import number
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend 
'''
x = number.getPrime(512)
y = number.getPrime(512)
print(x)
print('\n')
print(y)

Nfact = x*y
print('\n')
print(Nfact)
'''


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


'''
Tests to see if a number is prime.
'''


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_key_pair(p, q):
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private key_pair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    # Return the array of bytes
    return cipher


x = input("How many students, professor?\n")

for i in range(int(x)):
    if __name__ == '__main__':
        while True:
            keySize = 512
            p = number.getPrime(keySize)
            q = number.getPrime(keySize)
            nFact = p*q 
            phi = (p-1)*(q-1)
            genPT() #generate your random plaintext
            variable = genPT()
            plaintext1 = str(variable)
            public, private = generate_key_pair(p, q)
            encrypt_msg = encrypt(public, plaintext1)
            #Professor Cipher, PT
            professor_file = open('/Users/jacoblenes/Desktop/Fall 2021/HonorsThesis/FactFinal/ProfFact/forProf' + str(i)+'.csv', 'w')
            professor_file.write("***Student " + str(i) + '***')
            for word in encrypt_msg:
                professor_file.write(str(word) + ' ')
            professor_file.write('\n\n')
            for word in plaintext1:
                professor_file.write(str(word) + ' ')
            professor_file.write("\n\nP is: " + str(p) +"\nQ is: " + str(q))
            professor_file.close()
            #Student P, Q, N, and Phi Files
            student_file = open('/Users/jacoblenes/Desktop/Fall 2021/HonorsThesis/FactFinal/StudentFact/forStudent' + str(i)+'.csv', 'w')
            student_file.write("P is: " + str(p) +"\nQ is: " + str(q) + '\n\n\n')
            student_file.close()
            break
