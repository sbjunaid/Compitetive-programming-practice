bananas=list(map(int,input().split()))
w=int(input())
vehicle=0
bananas.sort()
for i in bananas:
    if i==w//2:
        if i in bananas[bananas.index(i)+1:]:
            bananas.remove(i)
            bananas.remove(w-i)
            
            vehicle+=1
            
    elif w-i in bananas:
        bananas.remove(w-i)
        bananas.remove(i)
        vehicle+=1
if w in bananas:
    bananas.remove(w)
    vehicle+=1        
    
if len(bananas)==2:
    if sum(bananas)<=w:
        
        vehicle+=1
        

else:
    vehicle+=len(bananas)
       
print(vehicle)    