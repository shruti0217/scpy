var='HELL is better '

#def dashed(va):
 #   vol=['a','e','i','o','u','A','E','I','O','U']
   # dash=[]
  #  count=0
    #    for a in va :
     #    for b in vol :
      #      if a==b:
       #        dash[count-1:count+1]=["-",a,"-"] 
        #           else:
         #           dash.append(a)
        #count++

#  print(dash)
 #indentation killed the code


#def dashed(va):
 #   vol=['a','e','i','o','u','A','E','I','O','U']
  #  dash=[]
   # count=-1
    #for a in va:
     #   for b in vol:
      #      count=count+1
       #     if a==b:
        #       dash[count:count+1]=["-",a,"-"]
            #else if a!=b:
               # dash.append(a)
           
                

                #dash.append(a)
   # val=str(dash)                 
    #print(val)
            


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