# To delete the elements from the front of the list until the front of the list is not even

def deleting_starting_evens(lst):

  while (len(lst) > 0 and lst[0] % 2 == 0):
      lst = lst[1:]
      return lst


print(deleting_starting_evens([4, 8, 10, 11, 12, 15]))
print(deleting_starting_evens([4, 8, 10]))