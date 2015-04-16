## Information about the data set
df <- read.csv('~/data_science_class_examples/lesson_example_code/sparrows.csv')


# sparrows.csv contains data about sparrow abundance vs human distrubance
# It covers roughly the number of people walking in a park per minute (ped)
# and the breeding pairs of sparrows found nearby.


summary(df)

# let's use a regular linear model first, and plot it against our data set
fit <- lm(pairs ~ ped, df)
plot(pairs ~ ped, df)
abline(fit, col="red")

# What's going on here? Do we think this is a good fit of the model?
# probably not.

# Let's try polynomial regression at various levels and compare each performance

# fit with two values
fit2 <- lm(pairs ~ poly(ped, 2), df)
points(df$ped, predict(fit2), col="blue", type="l")

# fit with three values
fit3 <- lm(pairs ~ poly(ped, 3), df)
points(df$ped, predict(fit3), col="orange", type="l")

# fit with four values
fit4 <- lm(pairs ~ poly(ped, 4), df)
points(df$ped, predict(fit4), col="green", type="l")



# which data set performed the best? Why do you think so?

# check the analysis of variance between each fit. which fit has the best p value?
anova(fit, fit2, fit3, fit4)