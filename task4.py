def remove_duplicates(nums):
    og = []
    
    for i in range(len(nums)):
        if nums[i] not in og:
            og.append(nums[i])
    
    return og

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  
print(remove_duplicates([7, 7, 7, 7]))             
print(remove_duplicates([1, 2, 3]))