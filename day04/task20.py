def nested_sum(lst):
    total=0
    for i in lst:
        if type(i) == list:
            total+=nested_sum(i)
        else :
            total+=i
    return total        
print(nested_sum([1, [2, 3], [4, [5, 6]]]))  
print(nested_sum([1, 2, 3]))                  
print(nested_sum([[1, [2]], [3, [4, [5]]]]))  