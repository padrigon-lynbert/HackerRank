# 2 3 6 6 5 - 5

n = int(input())
arr = list(map(int, input().split()))

scores = sorted(set(arr))
print(scores[-2])