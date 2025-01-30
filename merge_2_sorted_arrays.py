# Solution to merge 2 sorted arrays with O(m+n-1) complexity
class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >=0:
            if num1[i] > num2[j]:
                num1[k] = num1[i]
                i -= 1
            else:
                num1[k] = num2[j]
                j -=  1
            k -= 1

        while j >= 0:
            num1[k] = num2[j]
            j -= 1
            k -= 1
        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
