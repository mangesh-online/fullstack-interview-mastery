def subsets(nums):
    res = []
    def backtrack(i, path):
        if i == len(nums):
            res.append(path[:])
            return
        path.append(nums[i])
        backtrack(i+1, path)
        path.pop()
        backtrack(i+1, path)
    backtrack(0, [])
    return res

if __name__ == '__main__':
    print(subsets([1,2,3]))
