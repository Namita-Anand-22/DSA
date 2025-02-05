# 27. Remove Element: https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums, val):
        i = 0 # slow pointer
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i

def removeElement(nums, val):
    nums = [x for x in nums if x != val]
    return nums
