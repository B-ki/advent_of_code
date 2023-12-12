#%%

dict = {'one' : '1', 'two': '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
keys = list(dict.keys())


def find(word, sentence):
    if (sentence.find(word) == -1):
      return 100 + int(dict[word]), word
    return sentence.find(word), word


def replace_literal_number_by_int(str):
  new_dict = {}
  for key in keys:
    res = find(key, str)
    new_dict[res[0]] = res[1]
  indexes = list(new_dict.keys())
  min_index = min(indexes)

  while (min_index < 100):
    word = new_dict[min_index]
    str = str.replace(word, dict[word] + word[-1])
    del new_dict[min_index]
    for key in keys:
      res = find(key, str)
      new_dict[res[0]] = res[1]
    indexes = list(new_dict.keys())
    min_index = min(indexes)

  return str


def sum_first_last_digit(lines):
  sum = 0
  for line in lines:
    res = []
    line = replace_literal_number_by_int(str(line))
    str_list = list(line)
    for i in str_list:
      if i.isdigit():
        res.append(int(i))
        # res = [1, 4, 7, 4 , 2]
    if len(res) == 0:
      sum += 0
    elif len(res) == 1:
      sum += res[0] * 10 + res[0]
    else:
      sum += res[0] * 10 + res[-1]
    print(sum)
  return sum


ready = True

if not ready :
  file2 = open('test2.txt', 'r')
  Lines2 = file2.readlines()
  R = sum_first_last_digit(Lines2)
  print('test1 result =', R)
  assert R == 281
else :
  file = open('input.txt', 'r')
  Lines = file.readlines()
  print(sum_first_last_digit(Lines))