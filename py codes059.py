my_points = {'a':(4,3),'D':(1,2),'c':(5,1)}
list1=[]
add=0
for j in my_points.values():
    list1.append(list(j))
print(list1)
for i in list1:
    for j in i:
        add = add+j
print("addition :",add)
    
