from itertools import permutations

input = '3,8,1001,8,10,8,105,1,0,0,21,34,59,68,85,102,183,264,345,426,99999,3,9,101,3,9,9,102,3,9,9,4,9,99,3,9,1002,9,4,9,1001,9,2,9,1002,9,2,9,101,5,9,9,102,5,9,9,4,9,99,3,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,2,9,1001,9,5,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,102,3,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99'

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

def amp(value, phase, input):
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
        buffer = check3n4(value, inx, phase)
        phase = input
        if buffer:
          output = buffer
        inx += 2

      elif int(str(value[inx])[-1]) == 5 or int(str(value[inx])[-1]) == 6:
        inx = check5n6(value, inx)
      
      elif int(str(value[inx])[-1]) == 7 or int(str(value[inx])[-1]) == 8:
        check7n8(value, inx)
        inx += 4

def calculate(value):
  value = string_to_list(value)
  perms = list(permutations([0, 1, 2, 3, 4]))
  signals = []

  for perm in perms:
    input = 0
    for phase in perm:
      input = amp(value, phase, input)
    signals.append(input)
  return max(signals)

def amp_loop(value, phase, input):
  inx = 0
  output = 0
  input_used = False

  while(inx < len(value)):
    if value[inx] == 99:
      break
    else:
      if int(str(value[inx])[-1]) == 1 or int(str(value[inx])[-1]) == 2:
        check1n2(value, inx)
        inx += 4

      elif int(str(value[inx])[-1]) == 3 or int(str(value[inx])[-1]) == 4:
        buffer = check3n4(value, inx, phase)
        inx += 2
        if buffer:
          output = buffer
          phase = yield output
          buffer = 0
        elif not input_used:
          phase = input
          input_used = True

      elif int(str(value[inx])[-1]) == 5 or int(str(value[inx])[-1]) == 6:
        inx = check5n6(value, inx)
      
      elif int(str(value[inx])[-1]) == 7 or int(str(value[inx])[-1]) == 8:
        check7n8(value, inx)
        inx += 4

def feedback_loop(value):
  value = string_to_list(value)
  perms = list(permutations([5, 6, 7, 8, 9]))
  amps = []
  signals = []

  for perm in perms:
    input = 0
    amps = []
    amp_vals = [0] * 5
    for i in range(len(perm)):
      amps.append(amp_loop(value[:], perm[i], amp_vals[i-1]))
      amp_vals[i] = next(amps[i])

    try:
      while(True):
        for i in range(len(amps)):
           amp_vals[i] = amps[i].send(amp_vals[i-1])
    except StopIteration:
      signals.append(amp_vals[-1])

  return max(signals)

print(calculate(input), feedback_loop(input))