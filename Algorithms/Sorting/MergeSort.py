def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftarr = arr[:mid]
        rightarr = arr[mid:]

        merge_sort(leftarr)
        merge_sort(rightarr)

        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merge array index

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
                k += 1
            else:
                arr[k] = rightarr[j]
                j += 1
                k += 1
        
        # copy any left of elements
        while i < len(leftarr):
            arr[k] = leftarr[i]
            i += 1
            k += 1
        
        while j < len(rightarr):
            arr[k] = rightarr[j]
            j += 1
            k += 1

arr = [2,3,5,1,7,4,4,4,2,6,0]
print(arr)
merge_sort(arr)
print(arr)