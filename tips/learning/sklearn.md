# What's the basic sklearn approach?

* sklearn is modular because the tools within sklearn are subsections of eachother
* This means all modules of sklearn fit patterns in coding
* By the end of the day, your code should always look like this implementing sklearn:

```python
import numpy as np
# All machine learning tools will live inside a library of sklearn
# This one is the DummyClassifier, which is a baseline classifier
from sklearn.dummy import DummyClassifier

# Split your data into the features you want to use (X) and what you're trying to predict (y)
X = np.array([[1, 2], [30, 40], [3, 4], [800, 100]])
y = np.array([0, 0, 1, 1])

# fit the classifier. Ultimately this can be any regressor or classifier class included in sklearn
clf = DummyClassifier().fit(X, y)

# All classifiers have the same outputs!
print clf.predict(X) #  This is also in regressions
print clf.predict_proba(X)
print clf.predict_log_proba(X)
print clf.score(X, y) # This is also in regressions

# Returns everything about how the classifier was created.
# This is useful in determining what is adjustable within the specific
# algorithm you are using.
print clf.get_params()
```
