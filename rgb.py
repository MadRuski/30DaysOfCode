#prvi zad sa skolskog 2011
rgb=list(map(int,input().split()))
mini=[]
maxi=[]
mini.append(min(rgb))
rgb.remove(mini[0])
maxi.append(max(rgb))
rgb.remove(maxi[0])
print((rgb[0]-mini[0])+(maxi[0]-rgb[0]))