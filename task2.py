def is_palindrome(s):
    reversed_s = ""
    for i in range(len(s)-1, -1, -1):
        reversed_s = reversed_s + s[i]
    
    if reversed_s == s:
        return True
    else:
        return False

print(is_palindrome("racecar"))  
print(is_palindrome("mansoor"))  
print(is_palindrome("madam"))    