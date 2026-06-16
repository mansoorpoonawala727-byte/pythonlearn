def most_frequent(nums):
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] = counts[num] + 1
    
    most_freq = None
    highest_count = 0
    
    for num in counts:           
        if counts[num] > highest_count:
            highest_count = counts[num]
            most_freq = num
    
    return most_freq
 

print(most_frequent([1, 2, 2, 3, 3, 3, 4]))  
print(most_frequent([5, 5, 1, 1, 5]))         
print(most_frequent([7]))  
print(most_frequent([3, 3, 1, 1, 1, 2, 2, 2, 2]))                      