import pandas as pd
import math


def loop(list_of_list: list[list[int]], operators: list[str]) -> int:
    """
    Operate over the df with the corresponding operators and sum results
    """
    count = 0
    if len(list_of_list) != len(operators):
        raise ValueError("The number of DataFrames and operators must be the same.")
    for i in range(len(list_of_list)):
        if operators[i] == "+":
            count += sum(list_of_list[i])
        elif operators[i] == "*":
            count += math.prod(list_of_list[i])
    return count


def get_input(path: str) -> tuple[list[list[int]], list[str]]:
    """
    Read text input and output a Dataframe and a list of operators
    """
    with open(path, "r") as f:
        lines = f.readlines()

    operators = lines[len(lines) - 1].split()
    df = pd.DataFrame(list(line[:-1]) for line in lines[:-1])
    sep_grid = (df == " ").all()
    sep_col_index = list(sep_grid[sep_grid].index)
    bounds = [-1, *sep_col_index, len(df.columns)]
    list_df: list[pd.DataFrame] = []
    for a, b in zip(bounds[:-1], bounds[1:]):
        list_df.append(df.iloc[:, a + 1 : b])
    list_of_list: list[list[int]] = []
    for df in list_df:
        new_list: list[int] = []
        for col in df.columns:
            new_list.append(int(df[col].sum()))
        list_of_list.append(new_list)

    return list_of_list, operators


def main():
    df, list_op = get_input("input.txt")
    print(loop(df, list_op))


if __name__ == "__main__":
    main()
