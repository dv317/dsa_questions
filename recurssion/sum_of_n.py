def sum_of_n(n):
    if n<= 0:
        return 0
    return n + sum_of_n(n-1)


number = int(input("Enter number to find its sum"))
sumatation = sum_of_n(number)
print('sumatation', sumatation)