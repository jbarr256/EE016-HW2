# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
from random import Random, randint
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")




# must be in-place sort
def merge_sort(arr,cmp):
    pass

# must be in-place sort
#Member B wil solve in place quicksort
#Using a similar code that was found in the book but modified to use cmp
#cmp will be used to compare the first and last element of the array and this will allow the algorithm 
# to know if it 
def quick_sort(arr,cmp):
    def inplacequicksort(arr,cmp,left,right):
        if cmp >= 0: return
        pivot = randint(0,len(arr)-1)
        currLeft = left
        currRight = right -1
        while currLeft <= currRight:
            while currLeft <= currRight and arr[currLeft] < pivot:
                currLeft += 1
            while currLeft <= currRight and pivot < arr[currRight]:
                currRight -= 1
            if currLeft <= currRight:
                arr[currLeft],arr[currRight] = arr[currRight],arr[currLeft]
                left,right = left + 1, right - 1
        arr[currLeft],arr[right] = arr[right], arr[left]
        inplacequicksort(arr,left,currLeft-1)
        inplacequicksort(arr,currLeft + 1,right)
    inplacequicksort(arr,cmp,arr[0],arr[len(arr)-1])
    pass