## clustering
Clustering is a method of grouping together similar data points. 

### K-Means
- K-Means is a clustering algorithm. 
- How it works?
  1. Guess cluster centroids location and group the points to the centroids based on the distance
     - say we have 30 data points.
     - We want to group them into two
     - K-means will start by guessing two center (cluster centroids) that later will be used as the basis of the grouping
     - then the algorithm will look at all the data points to see which are closer to the one of the centroids. 
     - the data that are closer to centroid 1 will be grouped together, and so for the data that are closer to the centroid 2. 
  2. change location of the cluster centroid based on the average of the points in each group
     - After the grouping in the first step, we then calculate the average of them and use the value as the new location for centroid. 
     - then recalculate the distance and regroup them based on the new distance
  3. redo the step 2 iteratively until the algorithm converged which means that no change in the location of centroids

#### NOTE
If we ever in a situation where one of the centroid has zero points assigned to it, then our number of centroid will be K-1 (1 is the centroid with zero points). But if we really need two centroid then we can reinitialized them. 