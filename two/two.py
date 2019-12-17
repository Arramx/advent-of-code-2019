input = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,9,19,23,1,13,23,27,1,5,27,31,2,31,6,35,1,35,5,39,1,9,39,43,1,43,5,47,1,47,5,51,2,10,51,55,1,5,55,59,1,59,5,63,2,63,9,67,1,67,5,71,2,9,71,75,1,75,5,79,1,10,79,83,1,83,10,87,1,10,87,91,1,6,91,95,2,95,6,99,2,99,9,103,1,103,6,107,1,13,107,111,1,13,111,115,2,115,9,119,1,119,6,123,2,9,123,127,1,127,5,131,1,131,5,135,1,135,5,139,2,10,139,143,2,143,10,147,1,147,5,151,1,151,2,155,1,155,13,0,99,2,14,0,0'

def to_num_array(val):
  val = val.strip().split(',')
  return [int(i) for i in val]

def calculate1(val):
  val = to_num_array(val)
  val[1] = 12
  val[2] = 2

  for i in range(0, len(val)-1, 4):
    current = val[i:i+4]

    if current[0] == 99:
      return val[0]
    elif current[0] == 1:
      val[current[3]] = val[current[1]] + val[current[2]]
    elif current[0] == 2:
      val[current[3]] = val[current[1]] * val[current[2]]

def calculate2(val):
  val = to_num_array(val)

  for noun in range(0, 100):
    for verb in range(0, 100):
      copy = val[:]
      copy[1] = noun
      copy[2] = verb

      for i in range(0, len(copy)-1, 4):
        current = copy[i:i+4]
        if current[0] == 99 and copy[0] == 19690720:
          return 100 * noun + verb
        elif current[0] == 1:
          copy[current[3]] = copy[current[1]] + copy[current[2]]
        elif current[0] == 2:
          copy[current[3]] = copy[current[1]] *copy[current[2]]


print(calculate1(input), calculate2(input))