import random


class MySort:

    @staticmethod
    def heap_sort(nums: list):
        for i in range((len(nums) - 1) // 2, -1, -1):
            MySort._adjust_heap(nums, i, len(nums))
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            MySort._adjust_heap(nums, 0, i)

    @staticmethod
    def _adjust_heap(nums: list, index: int, len: int):
        top = nums[index]
        k = 2 * index + 1
        while k < len:
            if k + 1 < len and nums[k + 1] > nums[k]:
                k += 1
            if nums[k] > top:
                nums[index] = nums[k]
                index = k
            else:
                break
            k = 2 * k + 1
        nums[index] = top

    @staticmethod
    def quick_sort(nums: list, left: int, right: int):
        if left >= right:
            return
        sentinel = nums[left]
        i = left
        j = right
        while i < j:
            while i < j and nums[j] >= sentinel:
                j -= 1
            while i < j and nums[i] <= sentinel:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[left] = nums[i]
        nums[i] = sentinel
        MySort.quick_sort(nums, left, i - 1)
        MySort.quick_sort(nums, i + 1, right)


if __name__ == '__main__':
    array = []
    for i in range(50):
        array.append(random.randint(0, 100))
    print(array)
    MySort.heap_sort(array)
    print(array)
