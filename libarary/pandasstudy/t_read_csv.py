import pandas as pd


def func_main():
    read_csv()
    pass


def read_csv():
    df = pd.read_csv('./pandasstudy/student.csv')
    print(type(df), df)
    pass
