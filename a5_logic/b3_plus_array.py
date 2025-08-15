import os

os.system("cls")


def first_goal(nums: list[int], goal: int) -> None | list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                return [i, j]  # Return indices
    return None


nums = [4, 5, 6, 2]
goal = 8

print(first_goal(nums, goal))
