""""
Time Complexity : O(4n) where n is the length of the nums
                  First iteration for the checking all the input elements
                  Second n is for the while loop for the first iteration
                  Third iteration for the second for loop and 
                  Fourth n is for the while loop of the 2nd for loop
Space Complexity : O(n) where n is the length of the temperatures and the space is used for stack

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

Approach:
The brute force way is to find the next greater element with nested iteration and it will require O(n^2) where n is the length of nums.

The improvisation is to use the monotonic increasing stack
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        result = [-1 for _ in range(len(nums))]
        stack = []
        n = len(nums)
        for i in range(2*n):
            while len(stack) > 0 and nums[i % n] > nums[stack[-1]]:
                popIndex = stack.pop()
                result[popIndex] = nums[i % n]
            if i < n:
                stack.append(i)
        return result


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        result = [-1 for _ in range(len(nums))]
        stack = []
        n = len(nums)
        for i in range(n):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                popIndex = stack.pop()
                result[popIndex] = nums[i]
            stack.append(i)

        for i in range(n):
            while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                popIndex = stack.pop()
                result[popIndex] = nums[i]

        return result
