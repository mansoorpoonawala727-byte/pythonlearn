def merge_sort(nums):
    if len(nums) <= 1:        
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid]) 
    right = merge_sort(nums[mid:])  
    
    return merge(left, right)       

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


print(merge_sort([64, 34, 25, 12, 22, 11, 90]))