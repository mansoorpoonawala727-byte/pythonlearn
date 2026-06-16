def group_by_letter(words):
     result = {}
    
     for word in words:
        letter = word[0]              
        if letter not in result:
            result[letter] = [word]    
        else:
            result[letter].append(word)  
    
     return result

print(group_by_letter(["apple", "banana", "avocado", "blueberry", "cherry"]))
