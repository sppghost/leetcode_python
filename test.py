while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        sorted_nums = list(nums)
        sorted_nums.sort()
        for num in nums:
            first_app = sorted_nums.index(num)
            print(sorted_nums[n // 2 - 1] if first_app >= n // 2 else sorted_nums[n // 2])
    except Exception:
        break