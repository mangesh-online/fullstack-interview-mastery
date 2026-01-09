def two_sum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        complement = target - v
        if complement in seen:
            return [seen[complement], i]
        seen[v] = i

if __name__ == '__main__':
    print(two_sum([2,7,11,15], 9))
