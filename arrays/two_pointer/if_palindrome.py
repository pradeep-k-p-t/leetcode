def is_pallindrom(s:str) -> bool:
    "time complexity O(n), space complexity O(1)"
    left = 0 
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
# Test the function
print(is_pallindrom("racecar"))  # True
print(is_pallindrom("hello"))    # False