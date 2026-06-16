def flatten(nums):
    result = []
    
    for item in nums:
        if type(item) == list:    
            for num in item:      
                result.append(num)
        else:                    
            result.append(item)
    
    return result

print(flatten([1, [2, 3], [4, 5], 6]))      
print(flatten([[1, 2], [3, 4], [5, 6]]))     
print(flatten([1, 2, 3]))