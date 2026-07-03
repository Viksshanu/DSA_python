def missingnum(self, nums):
    n = len(nums) + 1

    actual_sum = n * (n - 1) // 2

    currsum = 0

    for num in nums:
        currsum += num

    ans = actual_sum - currsum
    return ans