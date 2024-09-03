def hashing():
    input_string = input("Enter Input String: ")

    hash_arr = [0]* 26
    print('hash arr', hash_arr)
    # for char in input_string:

    for char in input_string:
        hash_arr[ord(char)-ord('a')] +=1


    print('hash arr', hash_arr)

    # for i,val in enumerate(hash_arr):
    #     print(f'{chr(ord("a")+ i)} frequency {val}')

    for char in input_string:
        print(f"{char} frequency {hash_arr[ord(char)-ord('a')]}")


hashing()
