arr=[1,2,3,5,8,4,7,9,1,4,12,5,6,5,2,1,0,8,1]
a = [None] * len(arr);    
visited = 0;
for i in range(0, len(arr)):
    count = 1;
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            count = count + 1;
            a[j] = visited;    
        if(a[i] != visited):
            a[i] = count;  
for i in range(0, len(a)):    
    if(a[i] != visited):    
        print(" "+ str(arr[i]) +" has occured "+ str(a[i])+" times");    
