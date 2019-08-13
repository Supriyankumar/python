def every_three_nums(start):
    if start > 100:
        return []
    else:
        return list(range(start,101,3))

print(every_three_nums(91))