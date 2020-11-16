#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    start_day=i
    end_day=j
    divisor_by=k
    count_fav_day=0
    for i in range(start_day,end_day+1):
        print(i)
        fav_day=abs(i-reverse_digit(i))
        print(fav_day)
        if(fav_day%divisor_by==0):
            count_fav_day=count_fav_day+1
    return count_fav_day


def reverse_digit(day_number):
    rev_num=0
    while day_number>0:
        reminder=day_number%10
        rev_num=(rev_num*10)+reminder
        day_number/=10
    return rev_num



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
