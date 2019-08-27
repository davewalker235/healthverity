def main(list, current = 0, counter = 0, seen = None):
  """
  Recursively iterate through a seed list using the current value as the next
  values index. Count the unique values output before the list itself loops @
  after hitting an index it has already used.
  """

  # Careful to sidestep the python function defaults gotcha, seen = set() will
  # create a linked object in memory for all func calls
  if seen == None: seen = set()

  current = list[current]
  if current not in seen:
    seen.add(current)
    return main(list, current, counter + 1, seen)
  else:
    return counter

if __name__ == '__main__':
  # Just a quick and dirty list of simple test cases, it's a busy week,
  # so I don't have enough time to really set up a comprehensive test strategy
  lists = [
    (3, [1, 2, 0]),
    (3, [4, 1, 3, 4, 2]),
    (2, [4, 1, 3, 1, 1]),
    (3, [4, 1, 3, 4, 2, 4, 1, 3, 4, 2]),
    (6, [1, 2, 3, 4, 5, 0]),
    (3, [1, 2, 3, 1, 5, 0]),
  ]

  for [count, list] in lists:
    print(count == main(list))
