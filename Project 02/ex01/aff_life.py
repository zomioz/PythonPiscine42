import matplotlib.pyplot as plt
from load_csv import load


def main() -> bool:

    '''
    Program to load a .csv file and display the information
    Argument: None
    Return: 1 on Fail, 0 on succes
    '''

    df = load('life_expectancy_years.csv')
    if df is None:
        return 1

    try:
        fr_data = df.query("country == 'France'")
        fr_data = fr_data.drop(columns=['country']).T
        fr_data.columns = ['Life Expectancy']
    except ValueError:
        print("ValueError : error during reading France informations")
        return 1

    fr_data.plot()
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('France Life Expectancy Projections')
    plt.show()

    return 0


if __name__ == "__main__":
    main()
