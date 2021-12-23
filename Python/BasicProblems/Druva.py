#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY processorTime
#  2. INTEGER_ARRAY taskTime
#

def minTime(processorTime, taskTime):
    # Write your code here
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    processorTime_count = int(input().strip())

    processorTime = []

    for _ in range(processorTime_count):
        processorTime_item = int(input().strip())
        processorTime.append(processorTime_item)

    taskTime_count = int(input().strip())

    taskTime = []

    for _ in range(taskTime_count):
        taskTime_item = int(input().strip())
        taskTime.append(taskTime_item)

    result = minTime(processorTime, taskTime)

    fptr.write(str(result) + '\n')

    fptr.close()
