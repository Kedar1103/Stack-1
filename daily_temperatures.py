""""
Time Complexity : O(n) where n is the length of the temperatures
Space Complexity : O(n) where n is the length of the temperatures and the space is used for stack

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

Approach:
The brute force way is to find the next greater/warmer temperature through the nested iteration which will have time complexity of o(n) where n is the total number of elements in the temeperatures array.

The improvisation is using the monotonically increasing stack.
For each input temperature, loop on the stack and check if the current temperature can resolve the elements in the stack, if yes pop the index and populate the result with currentIndex - popIndex. 
Else append the current index to the stack.
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return []
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)

        return result
