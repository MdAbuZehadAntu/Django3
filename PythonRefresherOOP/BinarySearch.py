l=[int(item) for item in map(int,input().split())]
l.sort()
import sys
import time
sys.setrecursionlimit(10000)
n=66
mid=0
def b_search(lst,l,u,n):

    if lst[l]==n:
        globals()['mid'] = l
        return True
    elif lst[u]==n:
        globals()['mid'] = u
        return True
    else:

        globals()['mid']=int((l+u)/2)



        if abs(l-u)==1:
            return False

        elif lst[mid]==n:

            return True
        elif lst[mid]>n:

            return b_search(lst,l,mid,n)
        elif lst[mid]<n:
            return b_search(lst,mid,u,n)




if b_search(l,0,len(l)-1,n):
    print(f"Found at pos {mid+1}")
else:
    print("Not found")
