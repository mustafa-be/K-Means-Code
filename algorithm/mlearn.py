
import matplotlib.pyplot as plt
import os
import numpy as np
import argparse
import pandas as pd

def generateOutputs(data,labels,centroidLoc,clusters,iterations):
    if not os.path.exists("./output"):
        os.makedirs("./output")
    
    plt.scatter(data[:,0],data[:,1])
    plt.savefig("output/initial-data.png")
    plt.close()
    
    plt.scatter(data[:,0],data[:,1],c=labels)
    centroids=np.array(centroidLoc)
    plt.scatter(centroids[:,0],centroids[:,1],c=range(0,len(centroids)),s=200,marker="*")
    plt.savefig("output/data-{}-clusters-{}-iteration.png".format(clusters,iterations))
    plt.close()

    df=pd.DataFrame(data=data,columns = ['x','y'])
    df.to_csv("output/rawdata.csv",index=False)
    df['label']=labels
    df.to_csv("output/data-with-labels.csv",index=False)
    

class KMeans:
    def __init__(self, n_clusters=3, max_iter=20):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.data = []
        self.labels = []
        self.centroids =[]

    def fit(self,data):
        idx = np.random.choice(len(data), self.n_clusters, replace=False)
        centroids=[]
        for i in idx:
            centroids.append(data[i,:])

        correspondingclusters=[]
        
        for it in range(self.max_iter):
            correspondingclusters=[]

            for i in data:
                distances=[]
                for j in centroids:
                    distances.append(np.linalg.norm(i-j))
                correspondingclusters.append(np.argmin(distances))

            for j in range(len(centroids)):
                centroids[j]=np.mean([data[i] for i in range(len(data)) if correspondingclusters[i]==j],axis=0)
        
        self.data = data
        self.labels = correspondingclusters
        self.centroids = centroids

        return correspondingclusters,centroids

        pass

    def predit(self,Y):
        points=np.array(Y)
        if len(points.shape)==2:
            if points.shape[1]==2:
                correspondingclusters=[]
                for i in points:                    
                    distances=[]
                    for j in self.centroids:
                        distances.append(np.linalg.norm(i-j))
                    correspondingclusters.append(np.argmin(distances))
                return correspondingclusters

                
            else:
                raise ValueError('Data Shape isnt 2-D')

        else:
            raise ValueError('Data Shape isnt 2-D')
