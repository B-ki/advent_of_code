#%%


h = 0
w = 0


def check_num():
    # print(h)
    # print(w)
    s = ''
    one_char = []
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
                if ret != None:
                    one_char.append(ret)
                s = ''
        i = 0
    new_dict = {}
    for k in range(len(one_char)):
        for l in range(len(one_char)):
            if k != l and one_char[k][1] == one_char[l][1] and one_char[k][2] == one_char[l][2]:
                key = one_char[k][1] + one_char[k][2] * w
                # print('key', key)
                if key not in new_dict:
                    new_dict[key] = [one_char[k][0]]
                    # print('adding to new_dict :', one_char[k][0])
                else:
                    new_dict[key].append(one_char[k][0])
    ret = 0
    # print( 'new_dict :', new_dict)
    for s in new_dict.values():
        if len(s) == 2:
            ret += s[0] * s[1]
    return ret


def add_to_sum_result_if_valid(i, j, s):
    size = len(s)
    start_i = i - len(s)
    for v in range(max(0, j - 1), min(h - 1, j + 1) + 1):
        for u in range(max(0, start_i - 1), min(w - 1, i) + 1):
            if not (lines[v][u].isdigit() or lines[v][u] == '.'):
                if s.isdigit():
                    # print('adding : ', int(s), u, v)
                    return (int(s), u, v)


def get_delimiter(lines):
    unique_char = set()

    for line in lines:
        unique_char.update(char for char in line if not char.isdigit() and char != '.')
    for i in unique_char:
        if i.isdigit() or i == '.':
            unique_char.remove(i)

    print('delimiters :', unique_char)


ready = True


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
    print('Should get :', 755 * 598)
    print('and not :', 114 * 467 * 35 + 755 * 598)
    assert R == (755 * 598)
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
