s = "A man, a plan, a canal: Panama"

def isPalindrome(s: str) -> bool:
    new_str = "".join([ch for ch in s if ch.isalnum()]).lower()
    return new_str == new_str[::-1]


print(isPalindrome(s))