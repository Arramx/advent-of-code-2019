import math
from collections import defaultdict

input ='''##.#..#..###.####...######
#..#####...###.###..#.###.
..#.#####....####.#.#...##
.##..#.#....##..##.#.#....
#.####...#.###..#.##.#..#.
..#..#.#######.####...#.##
#...####.#...#.#####..#.#.
.#..#.##.#....########..##
......##.####.#.##....####
.##.#....#####.####.#.####
..#.#.#.#....#....##.#....
....#######..#.##.#.##.###
###.#######.#..#########..
###.#.#..#....#..#.##..##.
#####.#..#.#..###.#.##.###
.#####.#####....#..###...#
##.#.......###.##.#.##....
...#.#.#.###.#.#..##..####
#....#####.##.###...####.#
#.##.#.######.##..#####.##
#.###.##..##.##.#.###..###
#.####..######...#...#####
#..#..########.#.#...#..##
.##..#.####....#..#..#....
.###.##..#####...###.#.#.#
.##..######...###..#####.#'''

def string_to_grid(value):
  return list(map(lambda x: [j for j in x], [i for i in value.split('\n')]))

def get_asteroids_coords(input):
  coords = []
  for inx_y, y in enumerate(input):
    for inx_x, x in enumerate(y):
      if x == '#':
        coords.append((inx_x, inx_y))
  return coords

def count_detectable(input, pos):
  detectable = 0
  for coord in input:
    pos_diff = (coord[0] - pos[0], coord[1] - pos[1])
    increment = 0
    detect = True
    if pos_diff[0] < 0:
      x_sign = -1
    else:
      x_sign = 1
    if pos_diff[1] < 0:
      y_sign = -1
    else:
      y_sign = 1

    try:
      ypx = abs(pos_diff[1] / pos_diff[0])
      for i in range(abs(pos_diff[0])):
        if (pos[0] + x_sign*i, pos[1] + y_sign*i*ypx) in input:
          increment += 1
        if increment == 2:
          detect = False
          break
    except ZeroDivisionError:
      try:
        xpy = abs(pos_diff[0] / pos_diff[1])
      except ZeroDivisionError:
        pass
      for i in range(abs(pos_diff[1])):
        if (pos[0] + x_sign*i*xpy, pos[1] + y_sign*i) in input:
          increment += 1
        if increment == 2:
          detect = False
          break

    if detect:
      detectable += 1
  return detectable - 1
    
def calculate1(input, return_index):
  input = get_asteroids_coords(string_to_grid(input))
  if not return_index:
    return max([count_detectable(input, asteroid) for asteroid in input])
  else:
    detectable = [count_detectable(input, asteroid) for asteroid in input]
    return input[detectable.index(max(detectable))]

def angle_map(input):
  pos = calculate1(input, True)
  x, y = pos
  d = defaultdict(list)
  asteroids = get_asteroids_coords(string_to_grid(input))

  for a in asteroids:
    if a == pos:
      continue
    ax, ay = a
    angle = (math.degrees(math.atan2(ay - y, ax - x)) + 90 + 360) % 360
    d2 = (x - ax) ** 2 + (y - ay) ** 2
    d[angle].append((d2, a))

  for angle, pairs in d.items():
    d[angle] = [*sorted(pairs)]
  return d, asteroids

def calculate2(input):
  by_angle, asteroids = angle_map(input)
  angles = [*sorted(by_angle.keys())]
  vaporized = []
  while len(vaporized) < len(asteroids) - 1:
    for angle in angles:
      pointed_as = by_angle[angle]
      if pointed_as:
        vaporize, *rest = pointed_as
        vaporized.append(vaporize[1])
        by_angle[angle] = rest
  return vaporized[199][0] * 100 + vaporized[199][1]


print(calculate1(input, False), calculate2(input))