# You may need to install.packages('plyr')
# Check out plyr here: http://plyr.had.co.nz/09-user/
library(ggplot2)
library(plyr)
set.seed(1234)

data(iris)
summary(iris)

ggplot(iris, aes(Sepal.Length, Sepal.Width)) + geom_point()
res.kmeans <- lapply(1:10, function(i) {
    kmeans(iris[,c("Sepal.Length","Sepal.Width")], centers = i)
})

lapply(res.kmeans, function(x) x$withinss)
res.within.ss <- sapply(res.kmeans, function(x) sum(x$withinss))

ggplot(data.frame(cluster = 1:10, within.ss = res.within.ss), aes(cluster, within.ss)) +
  geom_point() + geom_line() +
  scale_x_continuous(breaks = 0:10)

cluster.colors <- lapply(res.kmeans, function(x) x$cluster)
l_ply(cluster.colors, function(colors) {
  plot.dat <- cbind(iris, cluster = factor(colors))

  gg.obj <- ggplot(plot.dat, aes(Sepal.Length, Sepal.Width, color = cluster)) +
    geom_point() + labs(title = paste(nlevels(factor(colors))))

  print(gg.obj)
})

# Compare our kmeans to the actual:
gg.pdf <- ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) + geom_point()
ggsave(gg.pdf, file="iris_original.pdf", scale=1)

res.kmeans <- lapply(3, function(i) {
  kmeans(iris[,c("Sepal.Length","Sepal.Width")], centers = i)
})

cluster.colors <- lapply(res.kmeans, function(x) x$cluster)
l_ply(cluster.colors, function(colors) {
  plot.dat <- cbind(iris, cluster = factor(colors))

  gg.obj <- ggplot(plot.dat, aes(Sepal.Length, Sepal.Width, color = cluster)) +
    geom_point() + labs(title = paste(nlevels(factor(colors))))

  print(gg.obj)
})