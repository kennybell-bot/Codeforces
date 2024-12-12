#Vanya y Fence
#http://codeforces.com/contest/677/problem/A

info = [int(x) for x in input().split()]
heights = [int(x) for x in input().split()]
roadWidth = 0

for i in range(info[0]):
    if(heights[i]>info[1]):
        roadWidth += 2
    else:
        roadWidth += 1

print(roadWidth)