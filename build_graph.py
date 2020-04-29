import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the dataset and print the first lines
data = pd.read_csv('./data/customers.csv')
x = data[["LoanAmount", "ApplicantIncome"]]

# Nb of clusters
k = 3


centroids = (x.sample(n = k))
plt.scatter(x["ApplicantIncome"], x["LoanAmount"], c = 'b')
plt.scatter(centroids["ApplicantIncome"], centroids["LoanAmount"], c = 'r')
plt.xlabel('Annual Income')
plt.ylabel('Loan Amount (in K)')
plt.savefig("original-plot.png")

def connectpoints(x, y, p1, p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1, x2], [y1, y2], 'k-')

threshold = 1000


diff = 1
j = 0
ai = "ApplicantIncome"
la = "LoanAmount"
xd = x
i = 1
for idx1, rowC in centroids.iterrows():
    ed = []
    for idx2, rowD in xd.iterrows():
        d1 = (rowC[ai] - rowD[ai]) ** 2
        d2 = (rowC[la] - rowD[la]) ** 2
        d = np.sqrt(d1 + d2)
        ed.append(d)
        if d <= threshold:
            if ai is not la :
                connectpoints(rowC, rowD, ai, la)
        print(d)
    x[i] = ed
    i = i + 1
    #plt.show()
    plt.axis('equal')
    plt.savefig("compatibilitygraph.png")