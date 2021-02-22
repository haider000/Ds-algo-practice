
a= [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#print(a[0])
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j],end=" ")
    print()
dire = 0
top = 0 ;
left = 0;
bottom = len(a)-1;
right = len(a)-1
te = 16;
count=0
while(count < te):
    if(dire==0):
        for i in range(left,right+1):
            print(a[top][i],end=" ")
            count+=1
        top=top+1
        
    elif(dire==1):
        for i in range(top,bottom+1):
            print(a[i][right],end=" ")
            count+=1
        right=right-1
    
    elif(dire==2):
        for i in range(right,left-1,-1):
            print(a[bottom][i],end=" ")
            count+=1
        bottom=bottom-1
        
    elif(dire==3):
        for i in range(bottom,top-1,-1):
            print(a[i][left],end=" ")
            count+=1
        left+=1
        
    dire = (dire+1)%4
