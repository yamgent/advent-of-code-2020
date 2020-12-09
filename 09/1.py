import sys


def pair_exists(nums, value):
    for v in nums:
        if value - v in nums:
            return True
    return False


def main():
    nums = [int(x.strip()) for x in sys.stdin]
    # window_size = 5
    window_size = 25
    for i in range(window_size, len(nums)):
        if not pair_exists(nums[(i-window_size):i], nums[i]):
            print(nums[i])
            return


main()
