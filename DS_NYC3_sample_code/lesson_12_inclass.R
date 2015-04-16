# Generate some data--we're building out a few lights in our room, and the data the cameras recorded
# intensities:   the lights
# recorded.data: data from our camera, generated through dists and the cameras (recorders)

set.seed(500)
recorders   <- data.frame("X" = c(0,0,1,1), "Y" = c(0,1,1,0),
row.names   <- c("A", "B","C","D"))
locs        <- data.frame("X" = c(.3,.5),"Y" = c(.8,.2))
intensities <- data.frame(
  "sine" = sin(0:99*(pi/10)) + 1.2,
  "cosine" = .7*cos(0:99*(pi/15))+.9)

dists <- matrix(
  nrow = dim(locs)[1], ncol = dim(recorders)[1],
  dimnames = list(NULL, row.names(recorders)))

for (i in 1:dim(dists)[2]){
  dists[,i]=sqrt((locs$X-recorders$X[i])^2 + (locs$Y-recorders$Y[i])^2)
}

recorded.data <- data.frame(jitter(as.matrix(intensities) %*% as.matrix(exp(-2*dists)),amount=0))

# Obtain data in a matrix
Xoriginal <- t(as.matrix(recorded.data))

# Center the data so that the mean of each row is 0
rm <- rowMeans(Xoriginal)
X  <- Xoriginal-matrix(rep(rm, dim(Xoriginal)[2]), nrow=dim(Xoriginal)[1])

# Calculate P
A <- X %*% t(X)
E <- eigen(A,TRUE)
P <- t(E$vectors)

# Find the new data and standard deviations of the principal components
newdata <- P %*% X
sdev <-  sqrt(diag((1/(dim(X)[2]-1)* P %*% A %*% t(P))))

pr <- princomp(recorded.data)

# Same thing for SVD
# Obtain data in a matrix
Xoriginal <- t(as.matrix(recorded.data))

# Center the data so that the mean of each row is 0
rm <- rowMeans(Xoriginal)
X  <- Xoriginal-matrix(rep(rm, dim(Xoriginal)[2]), nrow=dim(Xoriginal)[1])

# Calculate the SVD
X.svd <- svd(X)

# Run along and preview some of our data
barplot(X.svd$d^2/X.svd$d[1]^2)
plot.ts(X.svd$v)