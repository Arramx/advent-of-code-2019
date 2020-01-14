from math import gcd

value = '''<x=16, y=-11, z=2>
<x=0, y=-4, z=7>
<x=6, y=4, z=-10>
<x=-3, y=-2, z=-4>'''

def string_to_list(value):
  value = value.split()
  ret = [[]]

  for val in value:
    start = val.index('=')
    try:
      stop = val.index(',')
    except ValueError:
      stop = val.index('>')

    if len(ret[-1]) < 3:
      ret[-1].append(int(val[start+1:stop]))
    else:
      ret.append([int(val[start+1:stop])])

  return ret

class Moon():
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.dx = 0
    self.dy = 0
    self.dz = 0

  def gravity_x(self, rest):
    for moon in rest:
      if self.x < moon.x:
        self.dx += 1
      elif self.x > moon.x:
        self.dx -= 1

  def gravity_y(self, rest):
    for moon in rest:
      if self.y < moon.y:
        self.dy += 1
      elif self.y > moon.y:
        self.dy -= 1

  def gravity_z(self, rest):
    for moon in rest:
      if self.z < moon.z:
        self.dz += 1
      elif self.z > moon.z:
        self.dz -= 1

  def gravity(self, rest):
    self.gravity_x(rest)
    self.gravity_y(rest)
    self.gravity_z(rest)

  def velocity(self):
    self.x += self.dx
    self.y += self.dy
    self.z += self.dz
  
  def energy(self):
    return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.dx) + abs(self.dy) + abs(self.dz))

def calculate1(value, repeat):
  value = string_to_list(value)
  value = [Moon(*val) for val in value]

  for i in range(repeat):
    for inx, moon in enumerate(value):
      moon.gravity(value[:inx] + value[inx+1:])
    for moon in value:
      moon.velocity()
  return sum([moon.energy() for moon in value])

def calculate2(value):
  value = string_to_list(value)
  beginning = value
  value = [Moon(*val) for val in value]
  i = 0
  x = 0
  y = 0
  z = 0

  while True:
    for inx, moon in enumerate(value):
      moon.gravity_x(value[:inx] + value[inx+1:])
    for moon in value:
      moon.velocity()
    i += 1
    check = [[moon.x, moon.y, moon.z] for moon in value]
    check_vel = [moon.dx for moon in value]
    if check == beginning and not any(check_vel):
      x = i
      break
  i = 0

  while True:
    for inx, moon in enumerate(value):
      moon.gravity_y(value[:inx] + value[inx+1:])
    for moon in value:
      moon.velocity()
    i += 1
    check = [[moon.x, moon.y, moon.z] for moon in value]
    check_vel = [moon.dy for moon in value]
    if check == beginning and not any(check_vel):
      y = i
      break
  i = 0

  while True:
    for inx, moon in enumerate(value):
      moon.gravity_z(value[:inx] + value[inx+1:])
    for moon in value:
      moon.velocity()
    i += 1
    check = [[moon.x, moon.y, moon.z] for moon in value]
    check_vel = [moon.dz for moon in value]
    if check == beginning and not any(check_vel):
      z = i
      break

  x_and_y = int((x*y) / gcd(x, y))
  return int((x_and_y*z) / gcd(x_and_y, z))

print(calculate1(value, 1000), calculate2(value))