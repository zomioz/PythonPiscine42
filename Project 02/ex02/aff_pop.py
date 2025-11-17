import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from load_csv import load

def convert_population(value: str) -> float:

    '''
    Function to Convert population strings to numeric value
    Argument: a str : The value to convert
    Return: a float : the convert value
    '''

    if pd.isna(value):
        return np.nan
    
    if isinstance(value, str):
        value = value.strip()
        if value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('K'):
            return float(value[:-1]) * 1_000
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
        france_data = df.query("country == 'France'")
        france_data = france_data.drop(columns=['country']).T
        france_data.columns = ['France']
        france_data['France'] = france_data['France'].apply(convert_population)

        belgium_data = df.query("country == 'Belgium'")
        belgium_data = belgium_data.drop(columns=['country']).T
        belgium_data.columns = ['Belgium']
        belgium_data['Belgium'] = belgium_data['Belgium'].apply(convert_population)
        
    except ValueError:
        print("ValueError : error during reading informations")
        return 1

    both_data = pd.concat([france_data, belgium_data], axis=1)
    both_data.index = both_data.index.astype(int)
    both_data = both_data[(both_data.index >= 1800) & (both_data.index <= 2050)]
    both_data.plot()

    ax = plt.gca()
    ax.yaxis.set_major_formatter(lambda x, pos: f'{int(x/1_000_000)}M')

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.show()

    return 0


if __name__ == "__main__":
    main()
