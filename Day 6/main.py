from collections import defaultdict
with open("input.txt") as f:
 data = f.read()

# Parse each response into a look up table to query easily later.
program_response_lut = defaultdict(dict)
program_responses = [x.split(' -> ') for x in data.split('\n')]
for program_response in program_responses:
  program_data = program_response[0].split(' ')

  # Save their name and weight
  program_name = program_data[0]
  program_weight = int(eval(program_data[1]))
  program_children = []

  # print(program_name)
  # print(program_weight)

  # If we have a program holding others
  if(len(program_response) > 1):
    program_children = program_response[1].split(', ')
    # print(program_children)

  program_response_lut[program_name] = {
    "program_name": program_name,
    "program_weight": program_weight,
    "program_children": program_children,
    "parent": None
  }

def GetChildren(parent, program_name):
  print("GetChildren", parent, program_name)
  program = program_response_lut[program_name]
  program["parent"] = parent
  if len(program["program_children"]) != 0:
    for child in program["program_children"]:
      print("recursion")
      GetChildren(program_name, child)
  return program


for program in program_response_lut.values():
  GetChildren(program["parent"], program["program_name"])


for program in program_response_lut.values():
  if(program["parent"] == None and len(program["program_children"]) > 0):
    print(program)
