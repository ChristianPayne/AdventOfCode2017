import enum


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
  total = 0
  for row in processed_data:
    # Sorting just to make the division easier later.
    row.sort()
    for num1 in row:
      for num2 in row:
        # Find the two numbers in each row that divide evenly
        # Also make sure that the two are not the same number.
        if( num2 % num1 == 0 and num1 != num2):
          # Divide those two numbers to get a results
          total += num2 / num1
          break
  print(int(total))
Part2()