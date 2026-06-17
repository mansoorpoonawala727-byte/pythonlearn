def is_anagram(s1, s2):
    counts1 = {}
    counts2 = {}
    
    for letter in s1:    
        if letter not in counts1:
            counts1[letter] = 1
        else:
            counts1[letter] = counts1[letter] + 1
    
    for letter in s2:
        if letter not in counts2:
            counts2[letter] = 1
        else:
            counts2[letter] = counts2[letter] + 1
    
    if counts1 == counts2:
        return True
    else:
        return False
print(is_anagram("listen", "silent"))    
print(is_anagram("hello", "world"))      
print(is_anagram("triangle", "integral"))     