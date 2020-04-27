# Import librairies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the dataset and print the first lines
data = pd.read_csv('./data/customers.csv')
print(data.head())


# Visualise data points
x = data[["LoanAmount", "ApplicantIncome"]]
plt.scatter(x["ApplicantIncome"], x["LoanAmount"], c='b')
plt.xlabel('Annual Income')
plt.ylabel('Loan Amount (In Thousands)')
plt.show()
