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


def cmp(a,b):
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1

# must be in-place sort
#Member A will solve the in-place merge_sort
#it does so by solving using recursion that uses a set midpoint it solves first the left then right side and then merges the two
def inplaceMerge(arr,left,mid,right):
    currL = left
    currR = mid + 1
    #Brute force the merge by going through each element and testing if it is in the correct location.
    # If it is in the correct location , which should hace the left side be equal to or less then the right,then movve on
    #  but if not then shift all elements betweeen the points and swap the points. Repeat until it it reaches end of one side.
    while(currL <= mid and currR <= right):
        if(arr[currL] <= arr[currR]):
            currL += 1
        else:
            tempVal = arr[currR]
            currIn = currR
            #shift to the right
            while(currIn > currL):
                arr[currIn] = arr[currIn-1]
                currIn -= 1
            #swap
            arr[currL] = tempVal
            currL,currR,mid += 1

def merge_sort(arr,cmp):
    def inplaceMergeSort(arr,cmp,left,right):
        if cmp == 0: return
        mid = (left+right)//2
        inplaceMergeSort(arr,cmp,left,mid)
        inplaceMergeSort(arr,cmp,mid+1,right)
        inplaceMerge(arr,left,mid,right)
    #Call Function. No need to return anything
    inplaceMergeSort(arr,cmp,arr[0],arr[len(arr)-1])
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