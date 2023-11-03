import sys
input = sys.stdin.readline

n, k = map(int,input().split())
tmp = list(map(int, input().split()))

result = []
result.append(sum(tmp[:k]))

for i in range(n - k):
    result.append(result[i] - tmp[i] + tmp[k+i])
        
print(max(result))
