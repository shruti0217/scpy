#find ducplicate from the given array
#given an array of size N, find all the elements occuring more than once .

'''e.g. a[]=[2,3,4,5,3,6,2]
output : [2,3]

'''

def find_dup(arr):
    assert type(arr) is list
    assert type(arr) is not str 
    assert  len(arr) > 0 and len(arr)<=100,f"Shouldn't be empty or greater than 100"
    
    
    arr_d=[]
   
    for i in range(0,len(arr)):

        '''if arr[i] in arr:
            arr_d.append(arr[i])'''
        if arr.count(arr[i])>1 and not arr[i] in arr_d:
            arr_d.append(arr[i])
            
    return arr_d
if __name__=="__main__":
    array=[]
    n=0

    try:
        n=int(input("Enter length of list:"))
    except:
        n=0

    int
    for i in range(0,n):
        try:
            array.append(int(input(f"Element {i+1}")))
        except:
            array.append(0)  

    print(f"You entered : {array}:")
    print(find_dup(array)) 
    


