# TIME SERIES ANALYSIS

```python
import numpy as np
import pandas
import matplotlib.pyplot as plt
from sklearn import linear_model

import statsmodels.api as sm
from scipy import stats
from statsmodels.graphics.api import qqplot

print sm.datasets.sunspots.NOTE

dta = sm.datasets.sunspots.load_pandas().data

dta[:2]

dta.plot(x="YEAR", y="SUNACTIVITY", figsize=(12,3));
plt.show()
```

## Modeling Sunspots with a Linear Regression

### What problems do you think we will have?
```python
regr = linear_model.LinearRegression()

#dta = log(dta)
#dta = dta.replace([inf, -inf], np.nan)
#dta = dta.dropna()

years = [ [x] for x in dta["YEAR"].values]
sunsp = dta["SUNACTIVITY"].values

yearsTrain = years[:250]
yearsTest  = years[251:]
sunspTrain = sunsp[:250]
sunspTest  = sunsp[251:]

regr.fit(yearsTrain, sunspTrain)

regr.predict(yearsTest)

dta.plot(x="YEAR", y="SUNACTIVITY", figsize=(12,3));
plt.plot(years, regr.predict(years), color='red', linewidth=3)
plt.show()

regr.score(yearsTest, sunspTest)
```
This literally means that we did worse than a flat line -- yikes, time to try something else.

## Diagnostic Tools

### Residuals plot
```python
import random

sampleSize = 5000

x = []

for i in range(sampleSize):
    x.append(random.normalvariate(0,1))

resid = pandas.DataFrame([ [x[i] ] for i in range(len(x))])

resid.plot();
```

Note: These aren't actual residuals just normally distributed random data (which is how we want our actual residuals to look). Pretend the Y axis is time rather than just an index.

### Time Series data manipulation 101

Now that we have a pretty new picture I know you're itching to plot some thing with some other thing but first we should clean up our data a bit:

```python
dta[:2]

dta.index = pandas.Index(sm.tsa.datetools.dates_from_range('1700', '2008'))

dta[:2]

del dta["YEAR"]

dta[:2]

dta.plot(figsize=(12,3));
```
### Autocorrelation and Partial Autocorrelation in the Correlogram

Now that we've stared at statistics for a while it's time to make some pretty pictures.

```python
fig = plt.figure(figsize = (12, 6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta.values, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta, lags=40, ax=ax2)
```
### Fit a model

```python
#dta = log(dta)
#dta = dta.replace([inf, -inf], np.nan)
#dta = dta.dropna()

arma_mod20 = sm.tsa.ARMA(dta, (2, 0)).fit()
print arma_mod20.params
```
### Let's see how we did

```python
print "AIC: ", arma_mod20.aic
print "BIC: ", arma_mod20.bic
print "HQIC:", arma_mod20.hqic
# (Minimize these -- "___ Information Criterion")

fig = plt.figure(figsize=(12,3))
ax = fig.add_subplot(111)
ax = arma_mod20.resid.plot(ax=ax)

resid = arma_mod20.resid
stats.normaltest(resid)

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)
```

### Let's fit a different model!

```python
bestResult = [inf, 0, 0]

for i in range(15):
    arma_mod = sm.tsa.ARMA(dta, (i,0)).fit()
    print i, arma_mod.aic

    if arma_mod.aic < bestResult[0]:
        bestResult[0] = arma_mod.aic
        bestResult[1] = i

bestResult

arma_mod = sm.tsa.ARMA(dta, (bestResult[1],0)).fit()
resid = arma_mod.resid
arma_mod

fig = plt.figure(figsize = (12,3))
ax = fig.add_subplot(111)
ax = arma_mod.resid.plot(ax=ax)

stats.normaltest(resid)

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)

predict_sunspots = arma_mod.predict('1980', '2050', dynamic=True)

ax = dta.ix['1950':].plot(figsize(12,3))
ax = predict_sunspots.plot(ax=ax, style='r--', label='Dynamic Prediction');
ax.legend();
ax.axis((-20.0, 38.0, -4.0, 200.0));
ax.set_xlim(0, 50)

r, q, p = sm.tsa.acf(resid.values.squeeze(), qstat=True)
data = np.c_[range(1,41), r[1:], q, p]
table = pandas.DataFrame(data, columns=["lag", "AC", "Q", "Prob(>Q)"])
print table.set_index('lag')

def mean_forecast_err(y, yhat):
    return y.sub(yhat).mean()

mean_forecast_err(dta.SUNACTIVITY, predict_sunspots)
```

## Other things to play with: ARMA, Stationary processes, Unit root tests, Macroeconomic data

```python
from statsmodels.tsa.arima_process import arma_generate_sample, ArmaProcess

np.random.seed(1234)
arparams = np.array([1, .75, -.65, -.55, .9])
maparams = np.array([1, .65])

arma_t = ArmaProcess(arparams, maparams)

arma_t.isinvertible()

arma_t.isstationary()

fig = plt.figure(figsize(12,3))
ax = fig.add_subplot(111)
ax.plot(arma_t.generate_sample(size=50));

arparams = np.array([1, 0])
maparams = np.array([1, .5])
arma_t = ArmaProcess(arparams, maparams)
arma_t.isstationary()

arma_rvs = arma_t.generate_sample(size=500, burnin=250, scale=2.5)

fig = plt.figure(figsize(12,6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(arma_rvs, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(arma_rvs, lags=40, ax=ax2)

arma1 = sm.tsa.ARMA(arma_rvs, (1,1)).fit()
resid = arma1.resid
r, q, p = sm.tsa.acf(resid, qstat=True)
data = np.c_[range(1,41), r[1:], q, p]
table = pandas.DataFrame(data, columns=["lag", "AC", "Q", "Prob(>Q}"])
print table.set_index("lag")

macrodta = sm.datasets.macrodata.load_pandas().data
macrodta.index = pandas.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3'))

cpi = macrodta["infl"]
macrodta

fig = plt.figure(figsize=(12,3))
ax = fig.add_subplot(111)
ax = cpi.plot(ax=ax)
ax.legend()

print sm.tsa.adfuller(cpi)
```