from math import floor

def to_int_list(input):
  return [int(i) for i in input.split()]

def count_fuel(input):
  if type(input) is list or type(input) is tuple:
    return [floor(i/3)-2 for i in input]
  else:
    return floor(input/3)-2

def calc_fuel_fuel(input):

  for inx, unit in enumerate(input):
    input[inx] = iterate_fuel(unit)

  return input

def iterate_fuel(input):
  fuel = count_fuel(input)

  if fuel > 0:
    fuel += iterate_fuel(fuel)
  else:
    return 0

  return fuel

def calculate(input):
  mass_fuel = count_fuel(to_int_list(input))
  mass_fuel_num = sum(mass_fuel)
  fuel_fuel = sum(calc_fuel_fuel(mass_fuel))
  return [mass_fuel_num, mass_fuel_num + fuel_fuel]


print(calculate('''79620
58052
119910
138477
139102
78373
51937
63751
100937
56664
128939
115929
136981
68215
90317
97455
130858
94009
123221
81390
61726
78271
73354
103061
131261
140510
120555
117319
91154
96009
75491
90245
141689
118783
104601
121969
98547
108924
117114
65916
120037
66166
93973
105777
63501
89199
117551
126021
93466
107901
82323
104471
98794
57270
59457
120558
128142
137648
127375
103353
116578
97950
110725
96438
128425
75503
132178
138363
67009
127873
135747
108109
118818
75396
92822
63886
82973
116243
129066
74185
145298
83483
83417
54682
55648
142206
121420
149890
56561
107108
111376
139885
147373
131657
140634
79704
90263
139892
103841
50730'''))