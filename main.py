

import matplotlib.pyplot as plt
from algorithm.mlearn import KMeans,generateOutputs
import os
import numpy as np
import argparse
import pandas as pd



if __name__ == "__main__":
    parse_ag = argparse.ArgumentParser(description='K-Means Algorithm')
    parse_ag.add_argument('datapoints',metavar='datapoints',type=int,help='Number of Clusters ie k')
    parse_ag.add_argument('clusters',metavar='clusters',type=int,help='Number of Clusters ie k')
    parse_ag.add_argument('iterations',metavar='iterations',type=int,help='Number of Iterations ie iters')

    args = parse_ag.parse_args()

    clusters=args.clusters
    iterations=args.iterations
    data=np.random.rand(args.datapoints,2)

#    np.savetxt("rawdata.csv", data, delimiter=",")

    labels,centroidLoc=KMeans(n_clusters=clusters,max_iter=iterations).fit(data)

    generateOutputs(data,labels,centroidLoc,clusters,iterations)
