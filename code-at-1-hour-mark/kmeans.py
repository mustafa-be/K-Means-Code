import numpy as np
data1=np.random.rand(10,2)

idx = np.random.choice(len(data1), 3, replace=False)
centroids=[]

#init centroids
for i in idx:
  centroids.append(data1[i,:])

# compute clusters
correspondingclusters=[]
for i in data1:
  distances=[]
  for j in centroids:
    distances.append(np.linalg.norm(i-j))
  correspondingclusters.append(np.argmin(distances))
correspondingclusters

#reinit centroids with mean
for j in range(len(centroids)):
  centroids[j]=np.mean([data1[i] for i in range(len(data1)) if correspondingclusters[i]==j],axis=0)
