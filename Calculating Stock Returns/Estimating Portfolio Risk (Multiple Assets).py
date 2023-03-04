# To import package dependencies

import pandas as pd
import numpy as np

df = pd.read_csv("~\Desktop\Compilation of Data Science Quantitative Finance and Statistics\Calculating Stock Returns\data\VIRT_Virtu_Financial,_Inc_from_Yahoo.csv")

# To start off by converting string format dates into pandas datetime objects
# Why? This may assist in exploring the time series dataset (e.g., determining the start and end of the sample)

df['date_gsheets'] = pd.to_datetime(df['date_gsheets'])

df['date_gsheets'].describe()

# To explore the date

df.describe()

# To explore the datatypes | checking for NaNs

df.info()

# To set the date column as the index to, potentially, be used for applying formulas to the dataframe (overall)

df.set_index('date_gsheets', inplace=True)

# To calculate returns for an individual stock at each time

returns_df = df.pct_change(1)

# To create a vector of equal weights (\omega_1 = \omega_1 = ... = \omega_10)

num_stocks = 10
weights = [1 / num_stocks] * num_stocks

# To calculate the variance covariance matrix

vcv_matrix = returns_df.cov()

# To calculate the variance of the 10 asset portfolio

var_p = np.dot(np.transpose(weights), np.dot(vcv_matrix, weights))

# To calculate the total risk / standard deviate of the 10 asset portfolio

sd_p = np.sqrt(var_p)

# To calculate the Annualized Standard Deviation of the 10 asset portfolio (Apparently, there are only
# 250 trading days in a standard year [subtract weekends and holidays from the standard calendar
# year - when exchanges are closed])

sd_p_annual = sd_p * np.sqrt(250)

# To compare the portfolio risk with the individual risks of each security

individual_risks = np.std(returns_df) * np.sqrt(250)