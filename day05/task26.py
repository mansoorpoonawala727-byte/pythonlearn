def two_sum_fast(nums, target):
    seen={}
    for i,num in enumerate(nums):
        comp=target-num
        if comp in seen:
            return [seen[comp],i]
    
        seen[num]=i
    return []    
  
print(two_sum_fast([2, 7, 11, 15], 9))   
print(two_sum_fast([3, 2, 4], 6))        
print(two_sum_fast([3, 3], 6))           