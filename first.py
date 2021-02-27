while True:
    try:
        n1 = int(input())
        nums1 = list(map(int, input().split()))
        n2 = int(input())
        nums2 = list(map(int, input().split()))
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            elif nums1[i] < nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        print(' '.join(map(str, res)))
    except Exception:
        break
