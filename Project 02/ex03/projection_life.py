from load_csv import load
import matplotlib.pyplot as plt


def main() -> bool:

    '''
    Program to display information about 2 files
    Argument: None
    Return: 1 on fail, 0 on succes
    '''
    pth = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    income_df = load(pth)
    expectancy_df = load("life_expectancy_years.csv")
    if income_df is None or expectancy_df is None:
        return 1

    try:
        income_1900 = income_df['1900']
        expectancy_1900 = expectancy_df['1900']
    except KeyError:
        print("KeyError : 1900 isn't present in one or both .csv files")
        return 1

    fig, ax = plt.subplots()
    ax.scatter(income_1900, expectancy_1900)

    ax.set_xscale('log')
    ax.set_xticks([300, 1000, 10000])
    ax.set_xticklabels(['300', '1k', '10k'])
    ax.set_xlabel("Gross domestic product")
    ax.set_ylabel("Life Expectancy")
    ax.set_title("1900")

    plt.show()
    return 0


if __name__ == "__main__":
    main()
