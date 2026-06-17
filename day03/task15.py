
def find_all_pairs(nums, target):
    result = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append([nums[i],nums[j]])
    
    return result
    

print(find_all_pairs([1, 2, 3, 4, 5, 6], 7))
print(find_all_pairs([1, 1, 2, 3], 4))         
print(find_all_pairs([1, 2, 3], 10))            
