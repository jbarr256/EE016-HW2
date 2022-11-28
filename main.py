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
    if a==b:
        return 0
    elif a < b:
        return -1
    else:
        return 1

# must be in-place sort
#member A will solve the in-place merge_sort
def merge_sort(arr,cmp):


    pass

# must be in-place sort

def quick_sort(arr,cmp):
    pass