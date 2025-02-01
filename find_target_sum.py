""" Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target.
You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.
"""

class Solution:
    def subarraySum(self, arr, target):
        """ 
         Input arr = []
         Can use two pointers approach
        """
        start = 0
        arr_sum = 0
        for end in range(len(arr)):
            arr_sum+= arr[end]
            
            while arr_sum > target and start <= end:
                arr_sum -= arr[start]
                start+= 1
            
            if arr_sum == target:
                return [start+1, end+1]
        return [-1]
