#!/usr/bin/python3
"""alx interview question on Pascal's Triangle"""


def pascal_triangle(n):
  """returns a list of lists of integers representing the Pascal’s triangle of n
  Args:
      n (n): size of triangle
  Returns:
      list: returns empty list if n <= 0 or list of lists of integers
      representing Pascal's triangle of n otherwise
  """
  if n <= 0:
    return []
  
  tri, store_list = [], []
  for a in range(n):
    if a == 0:
      tri.append([1])
      continue
    if a == 1:
      tri.append([1, 1])
      continue
    
    sum_figs_list = tri[-1]
    for b in range(len(sum_figs_list) + 1):
      if b in [0, len(sum_figs_list)]:
        store_list.append(1)
        continue
      store_list.append(sum_figs_list[b] + sum_figs_list[b - 1])
    
    tri.append(store_list)
    store_list = []
    
  return tri
