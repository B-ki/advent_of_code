def check_num():
    s = ''
    sum_result = 0
    for j in range(h):
        for i in range(w):
            if lines[j][i].isdigit():
                s += lines[j][i]
            else:
                ret = add_to_sum_result_if_valid(i, j, s, check_num)
                if ret > 0:
                    sum_result += ret
                s = ''
    return sum_result


def add_to_sum_result_if_valid(i, j, s, check_func):
    size = len(s)
    start_i = i - size  # Adjust the start index

    valid_chars = {'*', '+', '$', '#'}  # Add more valid characters if needed

    for v in range(max(0, j - 1),  min(h, j + 2)):
        for u in range(max(0, start_i - 1), min(w, i + 2)):
            if lines[v][u] not in valid_chars:
                if s.isdigit():
                    print('adding:', int(s))
                    return int(s)
    return 0


ready = False

if not ready:
    with open('test8', 'r') as file:
        lines = [s.rstrip('\n') for s in file.readlines()]
    h, w = len(lines), len(lines[0])
    R = check_num()
    print(R)
else:
    with open('input', 'r') as file:
        lines = [s.rstrip('\n') for s in file.readlines()]
    h, w = len(lines), len(lines[0])
    R = check_num()
    print(R)

