#using Library direct methods

# l=[1,2,3,4,5]
# l.reverse()
# print(l)

# l=[1,2,3,4,5]
# new_l=list(reversed(l))
# print("the new list", new_l)

# l=[1,2,3,4,6]
# print(l[::-1])


#lets write our own functions
#logic: we will swap the positions of the first element l[0] with the last l[n-1] and so on
#then we will increment S value and decrement e value

def reverse(l):
    s=0
    e=len(l)-1
    while s<e:
        l[s],l[e]=l[e],l[s]
        s+=1
        e-=1

l=[1,2,3,4,5]
reverse(l)
print(l)
