def group_anagrams(words):
   
    groups = {}
    
    for word in words:
        key = "".join(sorted(word))  
        if key not in groups:
            groups[key] = [word]      
        else:
            groups[key].append(word) 
    
    return  list(groups.values())    

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
