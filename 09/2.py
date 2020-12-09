import sys
from collections import deque


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
            invalid = nums[i]

            group = deque()
            group.append(nums[0])
            group_sum = nums[0]

            j = 1
            while group_sum != invalid:
                if group_sum > invalid:
                    out = group.popleft()
                    group_sum -= out
                else:
                    group.append(nums[j])
                    group_sum += nums[j]
                    j += 1

            print(str(min(group) + max(group)))
            return


main()
