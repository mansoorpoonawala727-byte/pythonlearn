def count_letters(s):
    counts = {}
    for letter in s:          
        if letter not in counts:
            counts[letter] = 1  
        else:
            counts[letter] = counts[letter] + 1
    return counts


print(count_letters("banana"))