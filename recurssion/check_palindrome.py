# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
def palindrome(i,n,input):
    if i >= n/2:
        return True
    if input[i] != input[n-i-1]:
        return False
    return palindrome(i+1, n, input)


input_string = input("Enter string to check: ")
result = palindrome(0, len(input_string), input_string)

print('result', result)