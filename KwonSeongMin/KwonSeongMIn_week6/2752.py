#https://www.acmicpc.net/problem/2752

n = list(map(int,input().split()))
n.sort()
for i in range(3):
    print(n[i],end=' ')