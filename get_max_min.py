
arr = [8, 3, 7, 2, 9]

n = len(arr)

def get_min(arr, n):
    if n == 1:
        return arr[0]
    else:
        return min(get_min(arr[1:], n-1), arr[0])
    
def get_max(arr, n):
    if n == 1:
        return arr[0]
    else:
        return max(get_max(arr[1:], n-1), arr[0])
    
print(get_min(arr, n))
print(get_max(arr, n))
# Time Complexity: O(n)
# Auxiliary Space: O(n), as implicit stack is used due to recursion
