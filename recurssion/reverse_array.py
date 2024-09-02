'''
Approach 1 to reverse array
[1,2,3,4,5,6]

using 2 pointers left and right
left will move forward 
right will move backwards

untill they overlap each other

till then they will swap at each location

'''

def rev_arr(left,right, arr):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    rev_arr(left+1, right-1, arr)


my_list = [2,3,4,5,6,7,8,8,9,20]

# rev_arr(0,len(my_list)-1, my_list)
# print('my list', my_list)


''''

Second approch is to 
in an array when to reverse there is a logic that 
ith element has to be saved with n-i-1
i.e 0 the element should be swapped with n-i-1

'''

def rev_arr_v2(i,n,arr):
    if i >= n/2:
           return
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    rev_arr_v2(i+1, len(arr), arr=arr)

rev_arr_v2(0,len(my_list), my_list)
print('new list', my_list)