with open("input.txt") as f:
 data = f.read()

instructions = [int(instruction) for instruction in data.split('\n')]
total_instructions_length = len(instructions)
total_instructions_run = 0
current_instruction_index = 0
printStatements = False

while current_instruction_index < total_instructions_length:
  print("--------------") if printStatements else 0

  current_instruction = instructions[current_instruction_index]

  print("Read index: ", current_instruction) if printStatements else 0

  instructions[current_instruction_index] = current_instruction + (-1 if current_instruction >= 3 else 1)

  print(current_instruction, " >> ", instructions[current_instruction_index]) if printStatements else 0

  print("Index Before: ", current_instruction_index) if printStatements else 0

  current_instruction_index = current_instruction_index + current_instruction
  
  print("Index After: ", current_instruction_index) if printStatements else 0
  
  # Increment total instructions calculated
  total_instructions_run = total_instructions_run + 1

print(f"Total instructions calculated: {total_instructions_run}. Current instruction index: {current_instruction_index}")


# Part 1
# 1067 too low

# Part 2
# 20738928 too low
