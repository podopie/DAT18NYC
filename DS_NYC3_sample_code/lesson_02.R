## EXAMPLE 1 - supervisor performance

# this dataset shows a set of six numeric survey responses Xi (survey responses) and a dependent variable Y (perceived supervisor quality)
# we want to predict Y from the X's
x <- read.table('http://www.ats.ucla.edu/stat/examples/chp/p054.txt', sep='\t', h=T)
head(x)

# this set of scatterplots gives us an idea of the pairwise relationships present in the dataset
plot(x)

# this linear fit represents the "full model"; eg, the fit with all of the independent variables included
fit <- lm(Y ~ ., data=x)
summary(fit)

fit2 <- update(fit, .~. -X5)	# remove feature w/ lowest (abs) t score
summary(fit2)			# note R-sq decreases slightly, but adj R-sq increases slightly
				# --> increasing bias, decreasing variance

fit3 <- update(fit2, .~. -X4)	# ditto
summary(fit3)

fit4 <- update(fit3, .~. -X2)	# ditto
summary(fit4)			# stopping criteria met: all featuers have |t| > 1a
				# --> optimal bias-variance pt reached
				# --> Residual standard error (RSE) minimized

fit5 <- update(fit4, .~. -X6)	# note this model is weaker (lower R-sq, higher RSE)
summary(fit5)

fit6 <- update(fit5, .~. -X3)	# weaker still
summary(fit6)

plot(resid(fit4))		# want to see absence of structure in resid scatterplot ("gaussian white noise")
				# --> this plot looks pretty good; also note that resid quartiles look good

qqnorm(resid(fit4))		# want to see straight diagonal line in resid qqplot
				# --> again, looks pretty good

## EXAMPLE 2 - cigarette consumption

x <- read.table('http://www.ats.ucla.edu/stat/examples/chp/p081.txt', sep='\t', h=T)
head(x)
x$State <- NULL			# remove state label

fit <- lm(Sales ~ ., data=x)	# full model
summary(fit)

fit <- lm(Sales ~ 0 + ., data=x)# remove intercept
summary(fit)			# note weird stats! (high R-sq, low t-scores)
				# --> linear regression assumps violated
				# --> likely explanation: need more data for prediction
fit2 <- update(fit, .~. -HS)
summary(fit2)

fit3 <- update(fit2, .~. -Female)
summary(fit3)			# note t-score of Age jumps (Age becomes much more significant)
				# --> make sure you remove only one feature at a time with BE!

plot(resid(fit3))	        # obvious outlier present
qqnorm(resid(fit3))		# this does not look good! also resid quartiles are out of wack
				# --> conclusion: this dataset doesn't support multiple linear regression very well!
				# --> next step: before discarding modeling approach, get more data!

