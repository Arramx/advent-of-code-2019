input = '3,225,1,225,6,6,1100,1,238,225,104,0,2,218,57,224,101,-3828,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,26,25,224,1001,224,-650,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1102,44,37,225,1102,51,26,225,1102,70,94,225,1002,188,7,224,1001,224,-70,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,86,70,225,1101,80,25,224,101,-105,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,101,6,91,224,1001,224,-92,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,61,60,225,1001,139,81,224,101,-142,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,102,40,65,224,1001,224,-2800,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1102,72,10,225,1101,71,21,225,1,62,192,224,1001,224,-47,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1101,76,87,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,374,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,107,677,226,224,102,2,223,223,1006,224,404,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1107,677,677,224,1002,223,2,223,1006,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,449,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,509,1001,223,1,223,1007,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,539,101,1,223,223,1108,226,226,224,1002,223,2,223,1006,224,554,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,629,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,644,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226'

def string_to_list(value):
  return [int(i) for i in value.split(',')]


def check1n2(value, inx):
  modes = str(value[inx])[:-2][::-1]
  params = []

  for i in range(2):
    if i >= len(modes):
      params.append(value[value[inx+i+1]])
    else:
      if int(modes[i]) == 0:
        params.append(value[value[inx+i+1]])
      elif int(modes[i]) == 1:
        params.append(value[inx+i+1])
  params.append(value[inx+3])

  if int(str(value[inx])[-1]) == 1:
    value[params[2]] = params[0] + params[1]
  elif int(str(value[inx])[-1]) == 2:
    value[params[2]] = params[0] * params[1]
    

def check3n4(value, inx, to_input):
  modes = str(value[inx])[:-2][::-1]
  params = []

  if len(modes) == 0:
    params.append(value[inx+1])
  else:
    if int(modes[0]) == 0:
      params.append(value[inx+1])
    elif int(modes[0]) == 1:
      params.append(inx+1)

  if int(str(value[inx])[-1]) == 3:
    value[params[0]] = to_input
  elif int(str(value[inx])[-1]) == 4:
    return value[params[0]]


def check5n6(value, inx):
  modes = str(value[inx])[:-2][::-1]
  params = []

  for i in range(2):
    if i >= len(modes):
      params.append(value[value[inx+i+1]])
    else:
      if int(modes[i]) == 0:
        params.append(value[value[inx+i+1]])
      elif int(modes[i]) == 1:
        params.append(value[inx+i+1])

  if int(str(value[inx])[-1]) == 5 and params[0]:
    inx = params[1]
  elif int(str(value[inx])[-1]) == 6 and params[0] == 0:
    inx = params[1]
  else:
    inx += 3
  return inx

def check7n8(value, inx):
  modes = str(value[inx])[:-2][::-1]
  params = []

  for i in range(2):
    if i >= len(modes):
      params.append(value[value[inx+i+1]])
    else:
      if int(modes[i]) == 0:
        params.append(value[value[inx+i+1]])
      elif int(modes[i]) == 1:
        params.append(value[inx+i+1])
  params.append(value[inx+3])

  if int(str(value[inx])[-1]) == 7:
    value[params[2]] = int(params[0] < params[1])
  elif int(str(value[inx])[-1]) == 8:
    value[params[2]] = int(params[0] == params[1])


def calculate1(value):
  value = string_to_list(value)
  to_input = 1
  inx = 0
  output = 0

  while(inx < len(value)):
    if value[inx] == 99:
      return output
    else:
      if int(str(value[inx])[-1]) == 1 or int(str(value[inx])[-1]) == 2:
        check1n2(value, inx)
        inx += 4

      elif int(str(value[inx])[-1]) == 3 or int(str(value[inx])[-1]) == 4:
        buffer = check3n4(value, inx, to_input)
        if buffer:
          output = buffer
        inx += 2

def calculate2(value):
  value = string_to_list(value)
  to_input = 5
  inx = 0
  output = 0

  while(inx < len(value)):
    if value[inx] == 99:
      return output
    else:
      if int(str(value[inx])[-1]) == 1 or int(str(value[inx])[-1]) == 2:
        check1n2(value, inx)
        inx += 4

      elif int(str(value[inx])[-1]) == 3 or int(str(value[inx])[-1]) == 4:
        buffer = check3n4(value, inx, to_input)
        if buffer:
          output = buffer
        inx += 2

      elif int(str(value[inx])[-1]) == 5 or int(str(value[inx])[-1]) == 6:
        inx = check5n6(value, inx)
      
      elif int(str(value[inx])[-1]) == 7 or int(str(value[inx])[-1]) == 8:
        check7n8(value, inx)
        inx += 4


print(calculate1(input), calculate2(input))