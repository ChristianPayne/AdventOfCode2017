with open("input.txt") as f:
 data = f.read()

processed_data = [[int(num) for num in row.split('\t')] for row in data.split('\n')]

def Part1 ():
  total = 0
  for row in processed_data:
    row.sort()
    lowest_num = row[0]
    highest_num = row[-1]

    total += highest_num - lowest_num
  print(f"Total is: {total}")

def Part2():
  pass

Part2()