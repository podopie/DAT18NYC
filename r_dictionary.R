## R Function Dictionary
# Use this as a reference for all R methods we use either in class, read about at outside reading, or use in homework.

## Reading in things
# these two functions take text data stored in a matrix.
# read.csv is a version of read.table that changes the sep option
# according to standard csv format
read.table()
read.csv()

# source takes in an R script. Great for storing common functions that
# you write for everyday use, or an easy way to quickly grab common libraries
# used over and over again in R.
# arguments are a string with the file location. it operates like bash.
source()

# use these two to help get a better idea where you are in your filesystem,
# or to change it.
getwd()
setwd()

## Writing things
# writes a csv file from a data frame
write.csv()

## Looking at data
# checking size. Use length for vectors/arrays and nrow/ncol for data
# frames or matrices
length()
nrow()
ncol()

# summary spits out valueable information about whatever you are lookin at
summary()

# if you're looking at a fit or prediction, anova explains the variance.
anova()

# str lets you know what your data types are in a data frame or matrix.
str()

# Other various capture points
mean()
colSums()
rowSumns()
colMeans()
rowMeans()
quantile()
median()

## Changing data
# change a column to a different data type

as.factor()
as.numeric()
as.character()

# Transform data into something new.

# Better than for loops
apply()
*apply() # could be m, t, v, s. Can get complicated!

# Aggregations over data points.
aggregate()

## Functions for Machine Learning
# Keep in mind these are essential starters for machine learning problems
# we have only used them in their simplest forms, and can be incredibly
# powerful tools

# linear models
lm()
update()

# classification problems
knn()
knnImputation()
naiveBayes()

## Graphing data
# Please refer to the ggplot2 documentation since this gets verbose
# Otherwise, we've used (or I like to use)
ggplot()
geom_point()
geom_smooth()
geom_bar()

aes()
scale_color_brewer()
scale_fill_brewer()
labs()
theme_bw()

# basic plotting
plot()
abline()

## Libraries we've installed or used (or are recommended)
# Graphing
library(lattice)
library(ggplot2)

# data
library(MASS)

# classification
library(class)
library(e1071)

# text mining
library(tm)
library(Snowball)

# Manipulation
library(plyr)
library(reshape2)