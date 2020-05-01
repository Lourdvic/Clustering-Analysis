# Import librairies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# load the dataset and print the first lines
data = pd.read_csv('./data/customers.csv')
col1 = "LoanAmount"
col2 = "ApplicantIncome"
x = data[[col1, col2]]

# 1] Choose the number of cluster (k) & Select random centroids for each cluster

# Nb of clusters
k = 3

# Select random observation as centroids

centroids = (x.sample(n = k))
plt.scatter(x[col2], x[col1], c = 'b')
plt.scatter(centroids[col2], centroids[col1], c = 'r')
plt.xlabel(col2)
plt.ylabel(col1)
plt.savefig("startplot.png")
plt.show()

# 3 - Assign all the points to the closest cluster centroid by using euclidian dist
# 4 - Recompute centroids of newly formed clusters
# 5 - Repeat 3 and 4

def connectpoints(x, y, p1, p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1, x2], [y1, y2], 'k-')

threshold = 1000


diff = 1
j = 0
ai = "ApplicantIncome"
la = "LoanAmount"
while(diff != 0):
    xd = x
    i = 1
    for idx1, rowC in centroids.iterrows():
        ed = []
        for idx2, rowD in xd.iterrows():
            d1 = (rowC[col2] - rowD[col2]) ** 2
            d2 = (rowC[col1] - rowD[col1]) ** 2
            d = np.sqrt(d1 + d2)
            ed.append(d)
            #print(d)
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
    centroids_new = x.groupby(["Cluster"]).mean()[[col1, col2]]
    if j == 0:
        diff = 1
        j = j + 1
    else:
        diff = (centroids_new[col1] - centroids[col1]).sum() +\
               (centroids_new[col2] - centroids[col2]).sum()
        print(diff.sum())
    centroids = x.groupby(["Cluster"]).mean()[[col1, col2]]



# Plot the clusters

with open('result.csv', 'w', newline='') as result:
    thewriter = csv.writer(result)
    thewriter.writerow(['Cluster', col2, col1])

    color = ['purple','yellow','green']
    for K in range(k):
        data = x[x["Cluster"] == K + 1]
        plt.scatter(data[col2], data[col1], c = color[K])
        thewriter.writerow(data['Cluster'])
        thewriter.writerow(data[col2])
        thewriter.writerow(data[col1])

plt.scatter(centroids[col2], centroids[col1], c = 'red')
plt.xlabel(col2)
plt.ylabel(col1)
plt.savefig("plot2.png")
plt.show()


