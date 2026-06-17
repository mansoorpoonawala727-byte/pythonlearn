def find_largest(nums):
    largest = nums[0]
    for i in range(0,len(nums)-1,+1):
        if nums[i]>=largest:
            largest =nums[i]
         
    return largest               

print(find_largest([3, 7, 1, 9, 4]))   
print(find_largest([100, 23, 45, 67])) 
print(find_largest([5]))