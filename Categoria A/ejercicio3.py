#Bear and big brother
#http://codeforces.com/contest/791/problem/A

weights = [int(x) for x in input().split()]
years = 0

while(weights[0] <= weights[1]):
    weights[0] *= 3
    weights[1] *= 2
    years += 1

print(years)