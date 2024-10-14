#naive approach
# def countFreq(arr,n):
#     #checking whether the element has been seen before or not
#     for i in range (n):
#         flag= False
#         for j in range (i):
#             if arr[i]==arr[j]:
#                 flag= True
#                 break
#     #if the element is seen we choose to ignore
#         if flag == True:
#             continue
#     #if not seen before we count its frequency
#         freq=1
#         for j in range(i+1,n):
#             if arr[i]==arr[j]:
#                 freq+=1
#         print(arr[i],freq)
#
# list=[1,1,1,1,5]
# res= countFreq(list, n= len(list))
# print(res)


#efficient solution
def countFreq(arr,n):
    hmp=dict()
    for i in range(n):
        if arr[i] in hmp.keys():
            hmp[arr[i]]+=1
        else:
            hmp[arr[i]]=1
    for x in hmp:
        print(x," ",hmp[x])
list=[50,50,10,40,10]
res= countFreq(list, n= len(list))
print(res)