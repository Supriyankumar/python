# check the list of numbers that is divisible by ten and return that number divisible by ten

def divisible_by_ten(nums):
    count = 0
    for number in nums:
        if (number % 10 == 0):
            count += 1
    return count

print(divisible_by_ten([print(divisible_by_ten([20, 25, 30, 35, 40]))]))