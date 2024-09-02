def print_n_to_1(n):
    if n<=0:
        return 1
    print(n)
    print_n_to_1(n-1)

number = int(input("Enter N number"))
print_n_to_1(number)