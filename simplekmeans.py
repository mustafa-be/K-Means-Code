import numpy as np
def KMeans(data,k,iters):
  # Select random indexes equal to number of clusters
  idx = np.random.choice(len(data), k, replace=False)
  # Initilize centroids with indexes in above step
  centroids=[]
  for i in idx:
    centroids.append(data[i,:])
  correspondingclusters=[]

  for it in range(iters):
    correspondingclusters=[]
    # For each Data Point # Calculate distance from all centroids and choose minimum as label
    for i in data:
      distances=[]
      for j in centroids:
        distances.append(np.linalg.norm(i-j))
      correspondingclusters.append(np.argmin(distances))
    # Move centroid to the avg locations of all data points
    for j in range(len(centroids)):
      centroids[j]=np.mean([data[i] for i in range(len(data)) if correspondingclusters[i]==j],axis=0)
  return correspondingclusters,centroids




data=np.random.rand(100,2)
labels,centroids=KMeans(data,4,20)