import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from load_csv import load
from mpl_toolkits.axes_grid1 import Divider, Size

def main() -> bool:

    df = load('life_expectancy_years.csv')
    if df is None:
        return 1

    try:
        france_data = df.query("country == 'France'")
        france_data = france_data.drop(columns=['country']).T
        france_data.columns = ['Life Expectancy']
    except ValueError:
        print("ValueError : error during reading France informations")
        return 1

    france_data.plot()
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('France Life Expectancy Projections')
    plt.show()

    return 0


if __name__ == "__main__":
    main()
