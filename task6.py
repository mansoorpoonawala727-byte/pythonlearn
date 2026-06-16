def second_largest(nums):
    largest = float('-inf')  
    second = float('-inf')   
    
    for num in nums:        
        if num > largest:   
            second = largest 
            largest = num    
        elif num > second and num != largest: 
            second = num     
    
    if second == float('-inf'): 
        return None         
    return second            


print(second_largest([3, 7, 1, 9, 4]))
print(second_largest([100, 23, 45, 67])) 
print(second_largest([5, 5, 5]))         