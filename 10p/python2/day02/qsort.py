#!/usr/bin/env python3
"quick sort"
from random import randint

def qsort(nums):
    if len(nums) <2:
        return nums
    middle=nums[0]
    smaller=[]
    larger=[]
    for i in nums[1:]:
        if i >= middle:
            larger.append(i)
        else:
            smaller.append(i)
    return qsort(smaller)+[middle]+qsort(larger)


if __name__ == '__main__':
    nums=[randint(0,100) for i in range(10)]
    print(nums)
    print(qsort(nums))
