'''
#MAANG Question

You are given an array of integers nums and an integer target. 
Your task is to write a function that returns the indices 
of the two numbers such that they add up to the target.

'''


def two_sum (nums, target):
    seen = {}

    for i, num in enumerate (nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen [num]  = i

nums = [2,7,11,15]
target = 9 
indices = two_sum(nums, target)
print(f"Indices of the two numbers are:{indices}")
