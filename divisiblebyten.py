# check the list of numbers that is divisible by ten and return that number divisible by ten

def divisible_by_ten(nums):
    for num in nums:
        if num%10 == 0:
            return num
