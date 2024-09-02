'''
Problem Statement 1
print name N times
'''

def print_name(i,n):
    if i >n:
        return
    print("name")
    print_name(i+1,n)

number = int(input("Enter number how many time you want to print"))
print('number', number, type(number))

print_name(1,number)
