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

#Plaintext created
#let prof inoit size of key


#####THIS#####
#LARGE PRIME GEN FOR RSA
# Pre generated primes
first_primes_list = [104179, 104183, 104207, 104231, 104233, 104239, 104243, 104281, 104287, 104297, 
                    104309, 104311, 104323, 104327, 104347, 104369, 104381, 104383, 104393, 104399, 
                    104417, 104459, 104471, 104473, 104479, 104491, 104513, 104527, 104537, 104543, 
                    104549, 104551, 104561, 104579, 104593, 104597, 104623, 104639, 104651, 104659, 
                    104677, 104681, 104683, 104693, 104701, 104707, 104711, 104717, 104723, 104729]
                    
'''
                    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]
                '''
 #gen random number
def nBitRandom(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)
 #basic division test 
def getLowLevelPrime(n):
    '''Generate a prime candidate divisible
    by first primes'''

    '''The prime candidate is divided by the pre-generated primes to check for divisibility. 
    If the prime candidate is perfectly divisible by any of these pre-generated primes, 
    the test fails and a new prime candidate must be picked and tested. 
    This is repeated as long as a value which is coprime to all the primes in our generated primes list is found '''
    while True:
        # Obtain a random number
        pc = nBitRandom(n)
 
         # Test divisibility by pre-generated
         # primes
        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else: return pc
 
def isMillerRabinPassed(mrc):
    '''A prime candidate passing the low-level test is then tested again using the Rabin Miller Primality Test.
For extremely large numbers, such as ones used in RSA, deterministic testing of whether the chosen value is prime or not 
is highly impractical as it requires an unreasonable amount of computing resources.
A probabilistic approach is preferred as such. If an inputted value passes a single iteration of the Rabin Miller test, 
the probability of the number being prime is 75%.
Thus, a candidate passing the test, an adequate number of times, can be considered to be a prime with a 
satisfactory level of probability.Usually, in commercial applications, we require error probabilities to be less than 1/2^128'''
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)
 

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True
 
    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True
 

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def generate_keypair(phi): #remove p and q
    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = math.gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

x = input("How many students, professor?\n")

#also ask size of n/p/q
#compile for speed
#py pi 
#add pt and ct to student files
#make it csv not txt - one for student one for prof
    #one w all p/q/etc
    #one for prof that checks

for i in range(int(x)):
    if __name__ == '__main__':
        while True:
            n = 8       #8 bit prime
            eSize = 8
            p = getLowLevelPrime(n)
            q = getLowLevelPrime(n)
            e1 = getLowLevelPrime(eSize) 
            nFact = p*q
            phi = (p-1)*(q-1)

            if not isMillerRabinPassed(p): #check q too     #check earlier
                continue
            elif not isMillerRabinPassed(q):
                continue
            else:
                print(n, "bit prime is: \n", p)
                #print("P is: " + str(p))
                #print("Q is: " + str(q))
                #print("N is: " + str(nFact))
                #print("Phi is: " + str(phi))
                #print("E is: " + str(e1))
            
                #print("P and Q are: " + str(sys.getsizeof(p)))
                

            #output values encrypted with key from professor
            #program to give professor key for thids
            #provide program to students 
                genPT() #generate your random plaintext
                variable = genPT()
                plaintext1 = str(variable)
                public, private = generate_keypair(phi)
                print ("Your public key is " + str(public))
                encrypt_msg = encrypt(public, plaintext1)
                #Professor Cipher, PT
                professor_file = open('/Users/jacoblenes/Desktop/Fall 2021/HonorsThesis/FactFinal/ProfFact/forProf' + str(i)+'.csv', 'w')
                for word in encrypt_msg:
                    professor_file.write(str(word) + ' ')
                professor_file.write('\n\n')
                for word in plaintext1:
                    professor_file.write(str(word) + ' ')
                professor_file.close()
                #Student P, Q, N, and Phi Files
                student_file = open('/Users/jacoblenes/Desktop/Fall 2021/HonorsThesis/FactFinal/StudentFact/forStudent' + str(i)+'.csv', 'w')
                student_file.write("P is: " + str(p) +"\nQ is: " + str(q)+ "\nN is: " + str(nFact) + "\nPhi is: " + str(phi) + '\n\n*****\n\n')
                for word in encrypt_msg:
                    student_file.write(str(word) + ' ')
                student_file.write('\n\n')
                student_file.close()
                break
#1 folder per student --> csv w p and q, 1 for professor 

#This creates a sperate file per student, all within the PROF folder
# number of files asked
# 
# put on github 
