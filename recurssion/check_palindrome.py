def check_palindrome(i,n,check_string):
    if i>=n/2:
        return True
    if check_string[i] != check_string[n-i-1]:
        return False
    
    return check_palindrome(i+1, len(check_string), check_string=check_string)


check_string = input("Enter string to check palindrome")
print('aa', check_string)
check_palindrome(0,len(check_string), check_string)