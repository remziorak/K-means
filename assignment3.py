import pandas as pd
from KMeans import KMeans
import outpaths


# Name of the txt files
file1 = 'data1.txt'
file2 = 'data2.txt'
file3 = 'data3.txt'


# load datasets from files
dataset1 = pd.read_csv(file1, sep=',', header=None)
dataset2 = pd.read_csv(file2, sep=',', header=None)
dataset3 = pd.read_csv(file3, sep=',', header=None)


"=====================  K-Means for Dataset1: k=3, k=7 ====================="
kmeans1 = KMeans(n_cluster=3, random_state=721)
kmeans1.fit(dataset1)
kmeans1.save_figures(outpaths.outpath1)
kmeans1.create_gif(outpaths.outpath1)

kmeans2 = KMeans(n_cluster=7, random_state=721)
kmeans2.fit(dataset1)
kmeans2.save_figures(outpaths.outpath2)
kmeans2.create_gif(outpaths.outpath2)

"=====================  K-Means for Dataset2: k=2, k=5 ====================="
kmeans3 = KMeans(n_cluster=2, random_state=721)
kmeans3.fit(dataset2)
kmeans3.save_figures(outpaths.outpath3)
kmeans3.create_gif(outpaths.outpath3)

kmeans4 = KMeans(n_cluster=5, random_state=721)
kmeans4.fit(dataset2)
kmeans4.save_figures(outpaths.outpath4)
kmeans4.create_gif(outpaths.outpath4)

"=====================  K-Means for Dataset3: k=3, k=8 ====================="
kmeans5 = KMeans(n_cluster=3, random_state=721)
kmeans5.fit(dataset3)
kmeans5.save_figures(outpaths.outpath5)
kmeans5.create_gif(outpaths.outpath5)

kmeans6 = KMeans(n_cluster=8, random_state=721)
kmeans6.fit(dataset3)
kmeans6.save_figures(outpaths.outpath6)
kmeans6.create_gif(outpaths.outpath6)

