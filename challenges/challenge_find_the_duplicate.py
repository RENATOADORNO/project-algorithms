def find_duplicate(nums):
    if not nums or type(nums) is not list or len(nums) <= 1:
        return False

    nums.sort()
    for i in range(len(nums) - 1):
        if type(nums[i]) is not int or nums[i] < 0:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
