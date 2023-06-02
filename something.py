import pandas as pd


df = pd.DataFrame({'A': [1, 2, 4], 'B': [0, 3, 6]})
print(df)


def something(x: int) -> int:
    return x ** 2


x = 7
print(something(x))

