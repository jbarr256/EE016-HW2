from random import Random, randint

# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b, i.e. a is less then b
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged, a and b are equal already
#          cmp(a,b)>0   if a should be placed behind b. a is larger then b
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
#Member A will solve the in-place merge_sort
#it does so by solving using recursion that uses a set midpoint it solves first the left then right side and then merges the two

def merge_sort(arr,cmp):
    if cmp(len(arr),1) <= 0:
        return
    mid = len(arr)//2

    left = merge_sort(arr[:mid],cmp)
    right = merge_sort(arr[mid:],cmp)
    merged_list = []
    i,j = 0
    while i < len(left) and j < len(right):
        if cmp(left[i],right[j]) > 1:
            merged_list.append(left)
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    while i < len(left):
        merged_list.append(left[i])
        i += 1
    while j < len(right):
        merged_list.append(right[j])
        j += 1
    return merged_list

# must be in-place sort
#Member B wil solve in place quicksort
#Using a similar code that was found in the book but modified to use cmp
#cmp will be used to compare the first and last element of the array and this will allow the algorithm 
# to know if it 
def quick_sort(arr,cmp):
    def inplacequicksort(arr,cmp,left,right):
        if cmp(left,right) >= 0: return
        pivot = randint(0,len(arr)-1)
        currLeft = left
        currRight = right -1
        while currLeft <= currRight: #currLeft <= currRight:
            while currLeft <= currRight and cmp(arr[currLeft],pivot) < 0:
                currLeft += 1
            while currLeft <= currRight  and cmp(arr[currRight],pivot) > 0:
                currRight -= 1
            if currLeft <= currRight:
                arr[currLeft],arr[currRight] = arr[currRight],arr[currLeft]
                left,right = left + 1, right - 1
        arr[currLeft],arr[right] = arr[right], arr[left]
        inplacequicksort(arr,left,currLeft-1)
        inplacequicksort(arr,currLeft + 1,right)

    inplacequicksort(arr,cmp,arr[0],arr[len(arr)-1])
    pass