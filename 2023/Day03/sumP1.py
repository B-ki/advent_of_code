def check_num(lines):
    height = length(lines)
    width = length(lines)
    print(height)
    print(width)
    return 0


ready = False

if not ready:
    file = open('test', 'r')
    lines = file.readlines()
    R = check_num(lines)
    print(R)
else:
    file = open('input', 'r')
    lines = file.readlines()
    print()
