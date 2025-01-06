def get_dict_input(file_path: str) -> dict:
    """
    Transform an input like : 

    Button A: X+69, Y+23
    Button B: X+27, Y+71
    Prize: X=18641, Y=10279

    Button A: X+17, Y+86
    Button B: X+84, Y+37
    Prize: X=7870, Y=6450

    to :
    {
        1: [(69, 23), (27, 71), (18641, 10279)], 
        2: [(17, 86), (84, 37), (7870, 6450)]
    }
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    lines.append('\n')
    i = 0
    value_list: list = []
    dict_input: dict = {}
    for i, line in enumerate(lines):
        if (i+1) % 4 != 0:
            if 'Button' in line:
                str_list = line.split(',')
                value_list.append((int(str_list[0].split('+')[1]), 
                                   int(str_list[1].split('+')[1])))
            if 'Prize' in line:
                str_list = line.split(',')
                value_list.append((int(str_list[0].split('=')[1]), 
                                   int(str_list[1].split('=')[1])))
        else:
            dict_input[int(i / 4)] = value_list
            value_list = []
    return dict_input


def calculate(list_input: list) -> int:
    """
    x_result = a * x_a + b * x_b
    y_result = a * y_a + b * y_b
    """
    x_r = list_input[2][0]
    y_r = list_input[2][1]
    x_a = list_input[0][0]
    y_a = list_input[0][1]
    x_b = list_input[1][0]
    y_b = list_input[1][1]
    a = (x_r * y_b - y_r * x_b) / (x_a * y_b - y_a * x_b)
    b = (y_r * x_a - x_r * y_a) / (x_a * y_b - y_a * x_b)
    if a > 0 and b > 0 and a.is_integer() and b.is_integer():
        return int(a) * 3 + int(b)
    else:
        return 0


def main():
    input_data = get_dict_input('input.txt')
    #print(input_data)
    result = 0
    for key, value in input_data.items():
        result += calculate(value)
    print(result)
    return


if __name__ == '__main__':
    main()


