var='HELL is better '

def dashed(va):
    dash=[]
    fstr=""
    count=0
    for a in va:
        if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U':
            dash[count:count+1]=["-",a,"-"]
            count+=3
        else:
            dash.append(a)
            count=count+1   
    #fstr.join(dash)
    #print(dash) 
    return (fstr.join(dash))  
    
         


f=""

f=dashed(var);
print("Original string:",var,"\n")
print("Updated string:",f)