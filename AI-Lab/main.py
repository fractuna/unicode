import pandas as pd

def main():
    housing = pd.read_csv("datasets/housing.csv")

    housing.head()

    housing.info()


if __name__ == "__main__":
    main()
