
# Find min and max sum of n-1 elements
arr = [8, 3, 7, 2, 9]

n = len(arr)

def get_max_min_sum(arr, n):
    min_num = max_num = arr[0]
    arr_sum = arr[0]
    
    for i in range(1, n):
        if arr[i] < min_num:
            min_num = arr[i]
        
        if arr[i] > max_num:
            max_num = arr[i]
        
        arr_sum+= arr[i]
    print(arr_sum)
    min_sum = arr_sum - max_num
    max_sum = arr_sum - min_num
    return min_sum, max_sum

print(get_max_min_sum(arr, n))
