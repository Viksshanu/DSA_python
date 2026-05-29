from array import*
val=array('i',[1,2,3,10,0,1,5,6])
# print(val)                          #direct print the array

# for i in range(0,6):            #if you know the number of elements in array then you can use this method
#     print(val[i] , end=" ")

# for x in val:                    #if you don't know the number of elements in array then you can use this method
#     print(x , end=" ")

# for i in range(len(val)):           #if you don't know the number of elements in array then you can use this method
#     print(val[i] , end=" ")


# print(val.reverse())                
# print(val)
 
 

copyarray=array(val.typecode,(x for x in val))   #copy array

print(copyarray)