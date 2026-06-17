def reverse_str(s) :
    result = " "
    for i in range(len(s)-1 , -1 ,-1):
      result = result + s[i]
    return result
print(reverse_str("mansoor"))