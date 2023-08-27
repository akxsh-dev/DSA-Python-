def duplicates(list,n):
    temp = [0]*n
    temp[0] = list[0]                         #First element will always be distinct
    res = 1

    for i in range(1,n):                    #running a loop from 1 to end of the list or array
        if temp[res-1] != list[i]:          #comparing the temporary list's last copied value with the original list index
            temp[res] = list[i]
            res += 1
    for i in range(0, res):                  #copies the unique elements back into the array or list
        list[i] = temp[i]

    return res

list = [10,20,20,30,30,30,40,40,40,40]
n = 10
new_length = duplicates(list, n)
print("New Length:", new_length)
print("Modified List:", list[:new_length])  #using slicing to print till the new length of the list

