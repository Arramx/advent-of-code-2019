min_num = 125730
max_num = 579381

def adjacent_digits(num):
  for i in range(0, 10):
    try:
      result = str(num).index(str(i)+str(i))
      if result+1:
        return True
    except ValueError:
      pass
  return False

def two_adjacent_digits(num):
  string = str(num)
  for i in range(0, 10):
    try:
      result = string.index(str(i)+str(i))

      if len(string) <= result+2:
        condition = True
      else:
        condition = string[result] !=string[result+2]

      if result+1 and condition:
        return True
    except ValueError:
      pass
  return False


def never_decrease(num):
  string = str(num)
  for inx, i in enumerate(string[:-1]):
    if i > string[inx+1]:
      return False
  return True

def calculate(min_mun, max_num):
  correct_one = 0
  correct_two = 0

  for i in range(min_num, max_num+1):
    if adjacent_digits(i) and never_decrease(i):
      correct_one += 1
    if two_adjacent_digits(i) and never_decrease(i):
      correct_two += 1
  return correct_one, correct_two

print(calculate(min_num, max_num))