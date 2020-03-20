def quicksort(nums):
    if len(nums)<= 1:
        return nums
    else:
        pivot = nums.pop()

    nums_less_pivot = []
    nums_gt_pivot = []

    for i in nums:
        if i < pivot:
            nums_less_pivot.append(i)
        else:
            nums_gt_pivot.append(i)

    return quicksort(nums_less_pivot) + [pivot]  +  quicksort(nums_gt_pivot)

obj = quicksort([3,2,6,5,2,4])

print(obj)