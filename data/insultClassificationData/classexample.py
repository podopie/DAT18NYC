## Steps for creating an insult classifier
"""
Problem: Classify text as either an insult or not an insult
Data: Training data with text that decides if the input was an insult or not. soooo.... this is a supervised learning Problem
Classifier: Naive Bayes.

"""
### IMPORT MODULES
from pandas import read_csv, DataFrame
from sklearn import naive_bayes, cross_validation, metrics
from sklearn.feature_extraction.text import CountVectorizer

######## LOAD DATA
train = read_csv('train-utf8.csv')
test = read_csv('test-utf8.csv')



########## TRANSFORM THE DATA: COUNT VECTORIZE, CLEANING
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train.Comment)
X_test = vectorizer.transform(test.Comment)


##### USE THE WORD COUNT MATRIX TO PREDICT INSULT/NOT INSULT (1/0)
### BUILD A TRAINING AND TEST SET
model = naive_bayes.MultinomialNB().fit(X_train, list(train.Insult))



###### TEST RESULTS
###### CROSS VALIDATE
####### DISPLAY RESULTS: AUC TO CHECK FOR ERROR
print cross_validation.cross_val_score(naive_bayes.MultinomialNB(), X_train, train.Insult)
fpr, tpr, thresholds = metrics.roc_curve(train.Insult, model.predict(X_train), pos_label=1)
print metrics.auc(fpr, tpr)


######  OUTPUT RESULTS
predictions = model.predict_proba(X_test)[:,1]

submission = DataFrame({'id' : test.id, 'insult': predictions})
submission.to_csv('submission.csv', index=False)
