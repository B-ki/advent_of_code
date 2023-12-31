#%%


h = 0
w = 0


def check_num():
    # print(h)
    # print(w)
    s = ''
    sum_result = 0
    for j in range(h):
        for i in range(w):
            # print('i :', i, ', j:', j, 'lines:', lines[j][i])
            if lines[j][i].isdigit():
                s += lines[j][i]
            else:
                if i == 0:
                    ret = add_to_sum_result_if_valid(w, j - 1, s)
                else:
                    ret = add_to_sum_result_if_valid(i, j, s)
                if ret > 0:
                    sum_result += ret
                s = ''
        i = 0
    return sum_result


def add_to_sum_result_if_valid(i, j, s):
    # print(s)
    size = len(s)
    start_i = i - len(s)
    # if s.isdigit():
    #     print('add_to_sum', s)
    #     print('i:', i, 'j:', j, size, start_i)
    #     print(max(0, start_i - 1), min(w - 1, i))
    #     print(max(0, j - 1), min(h - 1, j + 1))
    for v in range(max(0, j - 1), min(h - 1, j + 1) + 1):
        for u in range(max(0, start_i - 1), min(w - 1, i) + 1):
            # if s.isdigit():
            #     print('u :', u, ', v:', v, 'lines:', lines[v][u])
            if not (lines[v][u].isdigit() or lines[v][u] == '.'):
                # print('tada')
                if s.isdigit():
                    print('adding : ', int(s))
                    return int(s)
    return 0


ready = True


def get_delimiter(lines):
    unique_char = set()

    for line in lines:
        unique_char.update(char for char in line if not char.isdigit() and char != '.')
    for i in unique_char:
        if i.isdigit() or i == '.':
            unique_char.remove(i)

    print('delimiters :', unique_char)


if not ready:
    file = open('test8', 'r')
    lines = file.readlines()
    # lines = [s[:-1] for s in lines]
    lines = [s.rstrip('\n') for s in lines]
    print(lines)
    h = len(lines)
    w = len(lines[0])
    R = check_num()
    print(R)
else:
    file = open('input', 'r')
    lines = file.readlines()
    lines = [s.rstrip('\n') for s in lines]
    print(lines)
    h = len(lines)
    w = len(lines[0])
    R = check_num()
    print(R)
    get_delimiter(lines)
