# Import librairies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# load the dataset and print the first lines
data = pd.read_csv('./data/customers.csv')
x = data[["LoanAmount", "ApplicantIncome"]]

# 1] Choose the number of cluster (k) & Select random centroids for each cluster

# Nb of clusters
k = 3

# Select random observation as centroids

centroids = (x.sample(n = k))
plt.scatter(x["ApplicantIncome"], x["LoanAmount"], c = 'b')
plt.scatter(centroids["ApplicantIncome"], centroids["LoanAmount"], c = 'r')
plt.xlabel('Annual Income')
plt.ylabel('Loan Amount (in K)')
# plt.show()

# 3 - Assign all the points to the closest cluster centroid by using euclidian dist
# 4 - Recompute centroids of newly formed clusters
# 5 - Repeat 3 and 4

diff = 1
j = 0

while(diff != 0):
    xd = x
    i = 1
    for idx1, rowC in centroids.iterrows():
        ed = []
        for idx2, rowD in xd.iterrows():
            d1 = (rowC["ApplicantIncome"] - rowD['ApplicantIncome'])**2
            d2 = (rowC["LoanAmount"] - rowD["LoanAmount"])**2
            d = np.sqrt(d1 + d2)
            ed.append(d)
        x[i] = ed
        i = i + 1

    c = []
    for idx, row in x.iterrows():
        min_dist = row[1]
        pos = 1
        for i in range(k):
            if row[i + 1] < min_dist:
                min_dist = row[i + 1]
                pos = i + 1
        c.append(pos)
    x["Cluster"] = c
    centroids_new = x.groupby(["Cluster"]).mean()[["LoanAmount", "ApplicantIncome"]]
    if j == 0:
        diff = 1
        j = j + 1
    else:
        diff = (centroids_new["LoanAmount"] - centroids["LoanAmount"]).sum() +\
               (centroids_new["ApplicantIncome"] - centroids["ApplicantIncome"]).sum()
        #print(diff.sum())
    centroids = x.groupby(["Cluster"]).mean()[["LoanAmount", "ApplicantIncome"]]

# Plot the clusters

with open('result.csv', 'w', newline='') as result:
    thewriter = csv.writer(result)
    thewriter.writerow(['Cluster', 'ApplicantIncome', 'LoanAmount'])

    color = ['purple','yellow','green']
    for K in range(k):
        data = x[x["Cluster"] == K + 1]
        plt.scatter(data["ApplicantIncome"], data["LoanAmount"], c = color[K])
        thewriter.writerow(data['Cluster'])
        thewriter.writerow(data['ApplicantIncome'])
        thewriter.writerow(data['LoanAmount'])

plt.scatter(centroids["ApplicantIncome"], centroids["LoanAmount"], c = 'red')
plt.xlabel('Income')
plt.ylabel('Loan Amount (In Thousands)')
plt.savefig("plot.png")



