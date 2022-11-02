ls=[1,2,3,4,5,6]
k=10
n=len(ls)
k=k%n
def swap(a, b):
    temp=ls[a]
    ls[a]=ls[b]
    ls[b]=temp

def reverse(ls):
    p1=0
    p2=len(ls)-1
    while(p1<p2):
        swap(p1,p2)
        p1+=1 
        p2-=1
    firsthalf=0
    midhalf=k-1
    while(firsthalf<midhalf):
        swap(firsthalf,midhalf)
        firsthalf+=1
        midhalf-=1
    seconhalf=k
    endhalf=n-1
    while(seconhalf<endhalf):
        swap(seconhalf,endhalf)
        seconhalf+=1 
        endhalf-=1
    print(ls)
    
reverse(ls)
