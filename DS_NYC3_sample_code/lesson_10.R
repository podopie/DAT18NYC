# install.packages('randomForest', repos = "http://cran.us.r-project.org/")
library(randomForest)



# Super super simple sample!
data(iris)
randomForest(iris[,-5], iris[,5], ntree=10)

# What's OOB again?
# How did we do?



# Let's try a much different data set.

# Here we have a dataset of chapters from books and plays by specific authors, and their usages of stop words.
# Let's see how accurately a random forest can predict the author based on stop word usage

authorship <- read.csv('http://people.stern.nyu.edu/jsimonof/AnalCatData/Data/Comma_separated/authorship.csv')

# What are some of the stop words we're looking at?
head(authorship)

# Create a random variable (remember, random forests work best with a random variable)
# and create a test and training set
authorship$randu = runif(841, 0,1)
authorship.train = authorship[authorship$randu < .4,]
authorship.test = authorship[authorship$randu >= .4,]


# We want to use all of these counts of words per row in an attempt to determine author.
authorship.model.rf = randomForest(
  Author ~ a + all + also + an + any + are + as + at + be + been + but + by + can + do +
  down + even + every + for. + from + had + has + have + her + his + if. + in. + into +
  is + it + its + may + more + must + my + no + not + now + of + on + one + only + or +
  our + should + so + some + such + than + that + the + their + then + there + things +
  this + to + up + upon + was + were + what + when + which + who + will + with + would + your,
  data=authorship.train, ntree=5000, mtry=15, importance=TRUE)

authorship.test$pred.author.rf = predict(authorship.model.rf, authorship.test, type="response")

# Confusion Matrix
table(authorship.test$Author, authorship.test$pred.author.rf)

# Performance in terms of 0 to 1
prop.table(table(authorship.test$Author, authorship.test$pred.author.rf),1)

# we can plot this prediction forest using plot
plot(authorship.model.rf)

# we can also check out some very specific stats about our trees. we can look at any tree we made!
k <- 1
getTree(authorship.model.rf, k)

## Reading Random Forest outputs for trees
# left daughter:
# right daughter:
# split var:
# split point:
# status prediction: