# Given an integer array nums, 
# return true if any value appears at least twice in the array,
# return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        mySet = set()

        for num in nums: 
            if num in mySet:
                return True
            else:
                mySet.add(num)
        return False



if __name__ == '__main__':

    num = [2, 2, 5, 3, 7]

    print(Solution().containsDuplicate(num))

