#slicing method

# l=[1,2,3,4]
# l=l[1:]+l[0:1]
# print(l)

#using append and pop method
# l=[1,2,3,5]
# l.append(l.pop(0))
# print(l)

#lets write a function for it

def rotatebyone(list):
    n=len(list)
    x=list[0]
    for i in range(1,n):
        list[i-1]=list[i]

    list[n-1]=x
list=[1,2,3,15]
rotatebyone(list)
print(list)
