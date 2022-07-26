data = list(map(int, input().split()))
bin_size = int(input())
for x in data:
    if x > bin_size:
        print("data cannot be greater than bin size")
        quit()
ans = [0 for x in range(len(data))]
waste = 0
for x in data:
    for y in range(len(ans)):
        if x + ans[y] < bin_size:
            ans[y] += x
            break
while 0 in ans:
    ans.remove(0)
bins = len(ans)
for x in ans:
    waste += (bin_size - x)
print(str(bins) + " bins")
print(str(waste) + " wasted space")
