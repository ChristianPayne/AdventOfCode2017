from collections import defaultdict
with open("input.txt") as f:
 data = f.read()

class Program ():
  def __init__(self, name, weight, children):
    self.name = name
    self.weight = weight
    self.children = children
    self.total_children_weight = 0
    self.parent = None
    self.balanced = False

  def Calculate_Weight_Fix(self, target_weight: int):
    total_weight = self.weight + self.total_children_weight
    print(f"Child Stats: name {self.name}, weight {self.weight}, total_children_weight {self.total_children_weight}, Total Weight: {total_weight}")
    print("Target Weight:", target_weight)
    print("Fixed weight", self.weight + (target_weight - total_weight))

# Parse each response into a look up table to query easily later.
programs = defaultdict(dict)
program_responses = [x.split(' -> ') for x in data.split('\n')]
for program_response in program_responses:
  program_data = program_response[0].split(' ')

  # Save their name and weight
  program_name = program_data[0]
  program_weight = int(eval(program_data[1]))
  program_children = []

  # If we have a program holding others
  if(len(program_response) > 1):
    program_children = program_response[1].split(', ')

  programs[program_name] = Program(program_name, program_weight, program_children)


def GetChildren(parent, program_name):
  program = programs[program_name]
  program.parent = parent
  children_programs = program.children
  if len(children_programs) > 0:
    for child in children_programs:
      GetChildren(program_name, child)
  return program


for program in programs.values():
  GetChildren(program.parent, program.name)


# Run part 1
for program in programs.values():
  if(program.parent == None and len(program.children) > 0):
    print(program.name)

# Part 2
def GetModeWeight(child_weights):
  mode = max(set(child_weights), key=child_weights.count)
  # print('Children',child_weights)
  # print("Children Mode:", mode)
  return mode


def GetChildrenWeights (program: Program, ):
  if(len(program.children) == 0):
    return program.weight

  child_weights = [ GetChildrenWeights(programs[child_name]) for child_name in program.children ]

  program.total_children_weight = sum(child_weights)
  child_target_weight = GetModeWeight(child_weights)
  program.balanced = len(set(child_weights)) == 1

  if(program.balanced == False):
    for index, child_weight in enumerate(child_weights):
      child_program = programs[program.children[index]]

      if(child_weight != child_target_weight):
        print(f"Need to fix {child_program.name}! Current Total:", child_weight, "Target:", child_target_weight)
        child_program.Calculate_Weight_Fix(child_target_weight)
        raise ValueError("HALP")


  total_weight = program.weight + program.total_children_weight
  return total_weight


# Run Part 2
print("Total Weight", GetChildrenWeights(programs["vvsvez"]))
