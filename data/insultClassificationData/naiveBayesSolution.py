# STEPS WE NEED TO TAKE
"""
1. Problem: We have text data. We'd like to determine if the text is an insult or not.
2. trianing data already has been decided if it's insult or not, so we know this can be a supervised Problem
3. since it's text, naive_bayes makes the most sense.


### LOAD DATA


### Text data isn't useable in it's form. Ed's said we need to vectorize text in the past?
Makes more sense to get counts? maybe... a count vectorizer?

search text count vectorizer in google, alright, sklearn came up.

seems like there's a bunch of arguments, but tells me it makes a world count matrix. matrix sounds like a training set, so DONE HERE!
Some things I see it also does:

remove stop words. Neat!
ngram range: relatively useful, how many words to consider per feature.


other things I need to do... cross_validation, and hey, let's try getting the auc score!
google: cross validation sklearn



otherwise, we know we just need to make a submission, so the output has to be some prediction alongside the original ids.


"""

from pandas import read_csv, DataFrame
from sklearn import naive_bayes, cross_validation, metrics
from sklearn.feature_extraction.text import CountVectorizer

train = read_csv('train-utf8.csv')
test = read_csv('test-utf8.csv')

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train.Comment)
X_test = vectorizer.transform(test.Comment)

print cross_validation.cross_val_score(naive_bayes.MultinomialNB(), X_train, train.Insult)
model = naive_bayes.MultinomialNB().fit(X_train, list(train.Insult))

fpr, tpr, thresholds = metrics.roc_curve(train.Insult, model.predict(X_train), pos_label=1)
print metrics.auc(fpr, tpr)

predictions = model.predict_proba(X_test)[:,1]

submission = DataFrame({'id': test.id, 'insult': predictions})
submission.to_csv('submission.csv', index=False)
