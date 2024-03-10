#!/bin/python3

import math
import os
import random
import re
import sys
import string
from itertools import combinations


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

s = input()
t = input()

result = ""
for i in range(len(s)):
    result += str(int(s[i]) + int(t[i]))
print(result)