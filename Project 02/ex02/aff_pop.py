import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def convert_population(value: str) -> float:

    '''
    Function to Convert population strings to numeric value
    Argument: a str : The value to convert
    Return: a float : the convert value
    '''

    if pd.isna(value):
        return None

    if isinstance(value, str):
        value = value.strip()
        if value.endswith('K'):
            return float(value[:-1]) * 1_000
        elif value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('B'):
            return float(value[:-1]) * 1_000_000_000

    return float(value)


def main() -> bool:

    '''
    Program to display the populations of two countries
    Argument: None
    Return: 1 on fail, 0 on succes
    '''

    df = load('population_total.csv')
    if df is None:
        return 1

    try:
        fr_data = df.query("country == 'France'")
        fr_data = fr_data.drop(columns=['country']).T
        fr_data.columns = ['France']
        fr_data['France'] = fr_data['France'].apply(convert_population)

        bel_data = df.query("country == 'Belgium'")
        bel_data = bel_data.drop(columns=['country']).T
        bel_data.columns = ['Belgium']
        bel_data['Belgium'] = bel_data['Belgium'].apply(convert_population)

    except ValueError:
        print("ValueError : error during reading informations")
        return 1

    all_data = pd.concat([fr_data, bel_data], axis=1)
    all_data.index = all_data.index.astype(int)
    all_data = all_data[(all_data.index >= 1800) & (all_data.index <= 2050)]
    all_data.plot()

    ax = plt.gca()
    ax.yaxis.set_major_formatter(lambda x, pos: f'{int(x/1_000_000)}M')

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.show()

    return 0


if __name__ == "__main__":
    main()
