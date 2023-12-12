#%%

def parse_one_input(str):
  if (str[-1] == '\n'):
    str = str[:-1]
  dict = {}
  dict['n'] = 0
  dict['red'] = 0
  dict['green'] = 0
  dict['blue'] = 0
  colon = str.split(':')
  indexes = colon[0].split(' ')
  dict['n'] = int(indexes[1])
  draws = colon[1].split(';')
  # print('draws :', draws)
  for draw in draws:
    colors = draw.split(',')
    # print('colors :', colors)
    for color in colors:
      color = color[1:]
      # print('color :', color)
      words = color.split(' ')
      # print('words :', words)
      if (dict[words[1]] < int(words[0])):
        dict[words[1]] = int(words[0])
  #print('dict :', dict)
  print()
  return dict
    

def check_if_right(dict):
  if (dict['red'] <= 12 and dict['green'] <= 13 and dict['blue'] <= 14):
    print('Game ', dict['n'], 'is right, with dict =', dict)
    return int(dict['n'])
  return 0


def get_power(dict):
  return dict['red'] * dict['green'] * dict['blue']


def calculate(lines):
  sum_index = 0
  for line in lines:
    sum_index += get_power(parse_one_input(line))
  return sum_index


ready = True

if not ready :
  file = open('test1', 'r')
  lines = file.readlines()
  R = calculate(lines)
  print(R)
  assert R == 2286
else:
  file = open('input.txt', 'r')
  lines = file.readlines()
  print(calculate(lines))