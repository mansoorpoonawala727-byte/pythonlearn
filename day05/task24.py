def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):  
            if nums[j] > nums[j+1]:         
                nums[j], nums[j+1] = nums[j+1], nums[j]  
    return nums   

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
