def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    
    return -1
print(binary_search([1, 3, 5, 7, 9, 11, 13], 7))   
print(binary_search([1, 3, 5, 7, 9, 11, 13], 11))  
print(binary_search([1, 3, 5, 7, 9, 11, 13], 4))   