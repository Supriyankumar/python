def larger_list(lst1,lst2):
  list1 = len(lst1)
  list2 = len(lst2)
  if (list1 > list2):
    return lst1[-1]
  elif(list2 > list1):
    return lst2[-1]
  else:
    return lst1[-1]
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))