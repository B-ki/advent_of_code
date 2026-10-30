import pandas as pd


def loop(df: pd.DataFrame, operators: list[str]) -> int:
    """
    Operate over the df with the corresponding operators and sum results
    """
    count = 0
    for col in range(len(df.columns)):
        if operators[col] == "+":
            count += df[col].astype(int).sum()
        elif operators[col] == "*":
            count += df[col].astype(int).prod()
    return count


def get_input(path: str) -> tuple[pd.DataFrame, list[str]]:
    """
    Read text input and output a Dataframe and a list of operators
    """
    with open(path, "r") as f:
        lines = f.readlines()

    operators = lines[len(lines) - 1].split()
    df = pd.DataFrame([line.split() for line in lines[:-1]])
    return df, operators


def main():
    df, list_op = get_input("input.txt")
    print(loop(df, list_op))


if __name__ == "__main__":
    main()
