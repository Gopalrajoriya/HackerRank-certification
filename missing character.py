import math
import os
import random
import re
import sys

def missingCharacters(s):
    g=[0]*123
    result=""
    for i in range(len(s)):
        x=ord(s[i])
        g[x]+=1
    for i in range(48,58):
        if(g[i]==0):
            result+=chr(i)
    for i in range(97,123):
        if(g[i]==0):
            result+=chr(i)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
    
