#insertion Sort 

def insertionsort(arr):
    
    for i in range(0,len(arr)):
        key=arr[i]
        print("Key:", key)
        j=i-1
        print("Array Entering loop: ",arr)
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            print("     inside loop {}",arr)
        arr[j+1]=key
        print("After Loop Ends", arr)        
arr=[12,11,13,5,6,1]
insertionsort(arr)
