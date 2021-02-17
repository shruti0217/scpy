#find ducplicate from the given array
#given an array of size N, find all the elements occuring more than once .

'''e.g. a[]=[2,3,4,5,3,6,2]
output : [2,3]

'''

def find_dup(arr):
    assert type(arr) is list
    assert type(arr) is not str 
    assert  len(arr) > 0 and len(arr)<=100,f"Shouldn't be empty or greater than 100"
    
    t=0
    arr_d=[]
   
    for i in range(0,len(arr)):

        '''if arr[i] in arr:
            arr_d.append(arr[i])'''
        if arr.count(arr[i])>1 and not arr[i] in arr_d:
            arr_d.append(arr[i])
        t+=1
    print(f"takes {t} rounds of loop")
            
    return arr_d

def find_dup_2(arr):    #[5,2,4,5,1,2]
    arr.sort()          #[1,2,2,4,5,5]
    arr_d=[]
    test=0
    #t=0
    
    '''for i in range(0,len(arr)):
        if arr.count(arr[i]) > 1 :
            arr_d.append(arr[i])
            i=i+arr.count(arr[i])-1     #this  creates another variable instead of updating the one that already exist 
        test+=1
    print(test)'''
    while test < len(arr) :                 
        if arr.count(arr[test]) > 1 :       
            arr_d.append(arr[test])
            test = test + (arr.count(arr[test]))
        else :   
            test += 1
       
        #t+=1
      
    
    #print(f"takes {t} rounds of loop") # takes t=len(arr) times to complete it 
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
    print(f"Now from the second function: {find_dup_2(array)}")    

