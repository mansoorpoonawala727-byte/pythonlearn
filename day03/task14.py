def is_valid(s):
    stack = []                           
    matches = {')':'(', ']':'[', '}':'{'} 
    
    for char in s:                     
        if char in '([{':              
            stack.append(char)         
        else:                          
            if len(stack) == 0:        
                return False
            top = stack.pop()          
            if top != matches[char]:   
                return False           
    
    return len(stack) == 0 
print(is_valid("(())"))    
print(is_valid("()[]{}"))  
print(is_valid("(]"))      
print(is_valid("([)]"))    
print(is_valid("{[]}"))            