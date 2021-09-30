import numpy as np
def KMeans(data,k,iters):
  idx = np.random.choice(len(data), k, replace=False)
  centroids=[]
  for i in idx:
    centroids.append(data[i,:])
  correspondingclusters=[]
  for it in range(iters):
    correspondingclusters=[]
    for i in data:
      distances=[]
      for j in centroids:
        distances.append(np.linalg.norm(i-j))
      correspondingclusters.append(np.argmin(distances))
    for j in range(len(centroids)):
      centroids[j]=np.mean([data[i] for i in range(len(data)) if correspondingclusters[i]==j],axis=0)
  return correspondingclusters,centroids




data=np.random.rand(100,2)
labels,centroids=KMeans(data,4,20)