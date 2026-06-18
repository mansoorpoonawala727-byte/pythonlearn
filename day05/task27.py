def first_non_repeating(s):
     letters = {}
     for letter in s:          
        if letter not in letters:
            letters[letter] = 1  
        else:
            letters[letter] = letters[letter] + 1
     for i in letters:
         if letters[i]==1:
             return i
         
     return None 
             



print(first_non_repeating("leetcode"))   
print(first_non_repeating("aabb"))       
print(first_non_repeating("aabbc"))      