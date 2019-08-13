def combine_sort(lst1,lst2):
  new_list = lst1 + lst2
  print(new_list)
  new_list.sort()
  print(new_list)
  return new_list

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))