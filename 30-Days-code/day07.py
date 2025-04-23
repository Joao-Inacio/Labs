n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
for i in arr[::-1]:
    print(i, end=" ")
