def heapify(list,n,i):
    largest=i           # initializes largest as the current root index.
    left=2*i+1          # calculates the index of the left child of the current node.
    right=2*i+2         # calculates the index of the right child of the current node.

    if left<n and list[left]>list[largest]:         #checks if the left child exists and is greater than the current node. If so, it updates largest to l.
        largest=left

    if right<n and list[right]>list[largest]:       #checks if the right child exists and is greater than the current largest. If so, it updates largest to r.
        largest=right

    if largest!=i:                                  #it means that one of the children is larger than the current node. In this case, a swap is performed between arr[i] and arr[largest] to maintain the heap property.
        list[i],list[largest]=list[largest],list[i]
        heapify(list,n,largest)

def heapSort(list):
    n = len(list)


    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)


    for i in range(n - 1, 0, -1):
        (list[i], list[0]) = (list[0], list[i]) # swap
        heapify(list, i, 0)

