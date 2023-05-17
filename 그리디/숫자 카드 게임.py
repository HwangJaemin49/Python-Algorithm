n, m = map(int, input().split())
nums = []
max = 0
for i in range(n):
    nums.append(list(map(int, input().split())))
    nums[i].sort()
    if nums[i][0] > max:
        max = nums[i][0]
print(max)