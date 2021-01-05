"""
You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed. All houses at this place are arranged in a circle. That
means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a
security system connected, and it will automatically contact the police if two adjacent
houses were broken into on the same night.
Given a list of non-negative integers nums representing the amount of money of each
house, return the maximum amount of money you can rob tonight without alerting the
police.
Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.
Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:
Input: nums = [0]
Output: 0
Constraints:
• 1 <= nums.length <= 100
• 0 <= nums[i] <= 1000
"""


def robberHouse(nums):

    if len(nums)== 0:
            return 0
    elif len(nums)== 1:
        return nums[0]
    elif len(nums)== 2:
        return max(nums)
    return max([rob_helper(nums[:-1]), rob_helper(nums[1:])]) 
    # nums(:-1) =[1,2,3] nums[1:]=[2,3,1]
    
def rob_helper(nums) :    
    if len(nums) == 0:
        return 0
    
    M = [0 for n in range(len(nums))]
    for i in range(len(nums)):
        val = M[i-2] if i-2 >= 0 else 0
        M[i] = max(M[i-1], val + nums[i])
    return M[-1]


if __name__ == "__main__":
    array = [1,2,3,1]
    n = len(array)
    print(robberHouse(array))

