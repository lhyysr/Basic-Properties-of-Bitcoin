import numpy as np
import matplotlib.pyplot as plt
from math import factorial as f
from math import e
from decimal import Decimal
import pandas as pd
import hashlib, binascii
import random

# 1
'''
Assume that block Bj-1 has value 'wubba lubba' and block Bj has 'value dubdub'.
Find the nonce s with num_zeros leading 0's.
'''
def hash_exp(num_zeros):
    # first check_digit digits of hex representation of num_zeros zeros 
    checklist = []
    check_digit = 0
    if (num_zeros == 0):
        checklist = ['8','9','a','b','c','d','e','f']
        check_digit = 1
    else:
        quotient = num_zeros / 4
        remainder = num_zeros % 4
        base = '0' * quotient
        check_digit = quotient
        if (remainder == 0):
            checklist = [base]
        else:
            check_digit += 1
            if (remainder == 1):
                checklist = [base+'4', base+'5', base+'6', base+'7']
            elif (remainder == 2):
                checklist = [base+'2', base+'3']
            else:
                checklist = [base+'1']
    # start checking            
    genesis = 'wubba lubba dub dub'
    found = False
    while (found == False):
        s = str(np.random.random())
        x = genesis + s
        y = hashlib.sha256(x).hexdigest()
        if (y[0:check_digit] in checklist):
            found = True
    return s
        
# 2
'''
Simulates the effort exerted in confirming a new Bitcion block by randomly generating
an integerin [0 ,2^256-1] and checking if there are at least num_zeros leading 0's.
Run the program 500000 times, sequentially, and generate an vector v1 that records each 
time you succeed of failed in 'mining' bitcoin.
'''
def fake_hash_exp(num_zeros):          
    n = random.randint(0, 2**256 - 1)
    if (n <= 2**(256-num_zeros) - 1):
        return n
    else:
        return None

def vector1():
    v = ''
    for i in range(500000):
        if (fake_hash_exp(6) != None):
            v += '1'
        else:
            v += '0'
    return v

# 3
'''
create an vector v2 of inter-arrival success times
'''
def vector2(v1):
    v2 = []
    while (v1 != ''):
        count = 0
        while (v1[0] != '1'):
            count += 1
            v1 = v1[1:]
            if (v1 == ''):
                return v2
        v2.append(count)
        v1 = v1[1:]
    return v2

# 4
'''
use v2 to plot a histogram of inter-arrival times with 20 bins
'''
def plot_v2(v2):
    plt.figure(1)
    plt.hist(v2, bins=20, weights=[1./len(v2) for i in range(len(v2))])
    plt.title("Unknow Distribution")
    plt.xlabel("Interarrival Time")
    plt.ylabel("Probability")
    plt.show()

# 5
'''
use v1 to generate a vector v3 the counts the number of times you successfully mined bitcoin
every 1000 trials. Plot a scaled histogram of the values in v3.
'''
def vector3(v1):
    v3 = []
    while (v1 != ''):
        count = 0
        for i in range(1000):
            if (v1 == ''):
                return v3
            elif (v1[0] == '1'):
                count += 1
            v1 = v1[1:]
        v3.append(count)
    return v3

def plot_v3(v3):
    plt.figure(1)
    plt.hist(v3, bins=20,weights=[1./len(v3) for i in range(len(v3))])
    plt.title("Bitcoin Mined Every 10 Minutes")
    plt.xlabel("Number of Bitcoin")
    plt.ylabel("Probability")
    plt.show()

# 6
'''
Plot a Poison distribution on top of your histogram from the previous question.
'''
def plot_Poisson(v3):
    plot_v3(v3)
    lam = np.average(v3)
    x = [i for i in range(30)]
    y = [e**(-lam) * lam**i / f(i) for i in range(30)]
    plt.figure(1)
    plt.plot(x, y)
    plt.show() 