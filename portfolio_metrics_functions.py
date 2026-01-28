import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function that calculates weekly percentage returns
def get_weekly_returns(stocks_data_adj_close):
    stocks_data_adj_close = stocks_data_adj_close.set_index("Date")
    stocks_data_adj_close.index = pd.to_datetime(stocks_data_adj_close.index)

    # resample the data on a weekly basis (using Friday's closing)
    weekly_data = stocks_data_adj_close.resample('W-FRI').last()
    # calculate weekly returns
    weekly_returns = weekly_data.pct_change().dropna().to_numpy()

    return weekly_returns

# Function to analyze the performance of a portfolio given some data on securities and weights
def calculate_portfolio_performance(weekly_returns, weights, plot_title= "Cumulative Portfolio Yield", savefig_name= "name.jpg"):

    # calculate the weekly return of the weighted portfolio
    portfolio_return = np.sum(weights * weekly_returns, axis=1)

    # calculate the cumulative yield
    cumulative_return = np.cumprod(1 + portfolio_return) - 1

    # calculate the average annual return and annual standard deviation
    average_annual_return = np.mean(portfolio_return) * 52
    annual_std_dev = np.std(portfolio_return) * np.sqrt(52)

    # graph representation
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_return, label='Cumulative Yield') #marker='o'
    plt.title(plot_title)
    plt.xlabel('Weeks')
    plt.ylabel('Cumulative Yield')
    plt.grid(True)

    # add annotations for the average annual return and annual standard deviation
    textstr = '\n'.join((
        f'Average Annual Return: {average_annual_return:.2%}',
        f'Annual Standard Deviation: {annual_std_dev:.2%}'))
    
    # box characteristics with average performance and annual standard deviation
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.gca().text(0.02, 0.90, textstr, transform=plt.gca().transAxes, fontsize=12,
                   verticalalignment='top', bbox=props)
    
    plt.legend()
    plt.savefig(savefig_name)
    plt.show()

def compare_portfolio_performance(weekly_returns, weights_custom, weights_equal, plot_title="Portfolio Equal-Weighted vs Random Forest", savefig_name="name.jpg", p1_name= "Portfolio 1", p2_name= "Portfolio 2"):
    # calculate the weekly return of weighted portfolios
    custom_portfolio_return = np.sum(weights_custom * weekly_returns, axis=1)
    equal_portfolio_return = np.sum(weights_equal * weekly_returns, axis=1)

    # calculate cumulative return for both portfolios
    custum_cumulative_return = np.cumprod(1 + custom_portfolio_return) - 1
    equal_cumulative_return = np.cumprod(1 + equal_portfolio_return) - 1

    # calculate the average annual return and annual standard deviation for both portfolios
    custom_avg_year_return = np.mean(custom_portfolio_return) * 52
    custom_year_std_dev = np.std(custom_portfolio_return) * np.sqrt(52)
    
    equal_avg_year_return = np.mean(equal_portfolio_return) * 52
    equal_year_std_dev = np.std(equal_portfolio_return) * np.sqrt(52)

    # graph representation
    plt.figure(figsize=(10, 6))
    plt.plot(custum_cumulative_return, label=f'Cumulative Return ({p2_name})', color='green')
    plt.plot(equal_cumulative_return, label=f'Cumulative Return ({p1_name})', color='red')
    plt.title(plot_title)
    plt.xlabel('Weeks')
    plt.ylabel('Cumulative Return')
    plt.grid(True)

    # add annotations for the average annual return and annual standard deviation
    textstr_equal = '\n'.join((
        f'Average Annual Return ({p1_name}): {equal_avg_year_return:.2%}',
        f'Annual Standard Deviation ({p1_name}): {equal_year_std_dev:.2%}'))
    
    textstr_custom = '\n'.join((
        f'Average Annual Return ({p2_name}): {custom_avg_year_return:.2%}',
        f'Annual Standard Deviation ({p2_name}): {custom_year_std_dev:.2%}'))

    # box characteristics with average performance and annual standard deviation
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.gca().text(0.02, 0.73, textstr_equal, transform=plt.gca().transAxes, fontsize=12,
                   verticalalignment='top', bbox=props)
    
    plt.gca().text(0.02, 0.85, textstr_custom, transform=plt.gca().transAxes, fontsize=12,
                   verticalalignment='top', bbox=props)
    
    plt.legend()
    plt.savefig(savefig_name)
    plt.show()