from typing import List
from itertools import combinations


def create_combinations(nums):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            num_1 = nums[i]
            num_2 = nums[j]
            yield [num_1, num_2]

def twoSum(nums: List[int], target: int) -> List[int]:
    number_combinations = combinations(nums, 2)
    for x1, x2 in number_combinations:
        sum = x1 + x2
        if sum == target:
            index_1 = nums.index(x1)
            del nums[index_1]
            index_2 = nums.index(x2) + 1
            return [index_1, index_2]

def twoSum_generator(nums: List[int], target: int) -> List[int]:
    number_combinations = create_combinations(nums)
    for x1, x2 in number_combinations:
        sum = x1 + x2
        if sum == target:
            index_1 = nums.index(x1)
            del nums[index_1]
            index_2 = nums.index(x2) + 1
            return [index_1, index_2]

print(twoSum_generator([3,2,4], 6))