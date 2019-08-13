def append_size(lst):
  length = len(lst)
  lst.append(length)
  return lst

print(append_size([23, 42, 108]))