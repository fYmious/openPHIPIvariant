nums = [int(x) for x in open("17.txt")]
min19 = min(x for x in nums if x % 19 == 0)

res = []
for i in range(len(nums) - 1):
    if any(x % min19 == 0 for x in nums[i:i + 2]):
        res += [nums[i] + nums[i + 1]]

print(len(res), max(res))

