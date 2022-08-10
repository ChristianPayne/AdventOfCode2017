with open("input.txt", "r") as f:
 data = f.read()

def Part1 ():
  total = 0
  for index, number in enumerate(data):
    # Set the next index
    next_index = index + 1

    # If the index goes out of range, set it to zero.
    if(next_index >= len(data)):
      next_index = 0

    # If our numbers are the same, add the second one to the total.
    if(int(number) == int(data[next_index])):
      total += int(data[next_index])

  print(f"Total value: {total}")

def Part2 ():
  total = 0
  length = len(data)
  for index, number in enumerate(data):
    next_index = int(length / 2) + index
    if(next_index >= length):
      next_index -= length
    # print(index, next_index, length)
    if(int(number) == int(data[next_index])):
      total += int(data[next_index])


  print(f"Total value: {total}")

Part2()

