#Anton and Danik
#https://codeforces.com/contest/734/problem/A

games = int(input())
winners = input()
anton  = 0
danik = 0

for i in winners:
    if i == "A":
        anton += 1
    elif i == "D":
        danik += 1

if anton == danik:
    print("Friendship")
elif anton > danik:
    print("Anton")
else:
    print("Danik")