"""
1. What's the primary difference between the following two ipython magic (%)
commands?
"""
%matplotlib inline
%pylab inline

# matplotlib inline and pylab inline both bring matplotlib inline to the notebook;
# matplotlib does not import libraries. pylab import numpy and matplotlib.

"""
2.  We have a file called "ads_performance.csv" which includes the following
header rows, and one row and the end that sums the total of the dataset.

Google Adwords Perfomance
February 16 2015, February 22 2015
Brand
date, ad_id, strategy_group, description, spend, spend_wfees, impressions, clicks
02/16/2015, 1772, 'team_bananas', 'Did you know there are 100s of bananas? Click here to find out more!', 23.75, 24.33, 107771, 10

Write the pd.read_csv function that would ignore the additional headers, use the
correct header for the column names, and ignore the very last row.
"""

ads = pd.read_csv(url, skip_footer=1, skiprows=3)

"""
3. With the ads dataset stored in name `ads`, write code that'd create a subset
of just ad_id 200 where the spend was more than 30 dollars

subset = ads...(some_code)...
"""

# There are plenty of ways to solve this, below is just one.
subset = ads[(ads.ad_id == 200) && (ads.spend > 30.0)] # note this subset has no rows in the csv file.

"""
4. We want to aggregate the sum of spend by day and ad. What code would return
back that dataset?
"""

ads.groupby(['date', 'ad_id',]).spend.sum()
ads.groupby(['date', 'ad_id',]).agg({'spend': 'sum'})

"""
5. Explain what the following code block is doing, line by line.
"""
# import the plotter as namespace plt
import matplotlib.pylab as plt
#allow division of integers to return floats
from __future__ import division

# create a column called "ctr" which is clicks divided by impressions
ads['ctr'] = ads['clicks'] / ads['impressions']

# create a figure space
fig = plt.figure()
# generate the first subplot of 1x2
plt.subplot(1, 2, 1)
# The first subplot is a histogram
plt.hist(ads.spend)

# generate the second subplot
plt.subplot(1, 2, 2)
# this plot is a scatter plot of spend vs click thru rate (ctr)
plt.plot(ads.spend, ads.ctr, 'g.')
# show the figure
plt.show()


"""
6-8. Imagine we're viewing the following coefficient table for the following
regression:

(ad_id1772 is either 1 or 0, meaning it was ad 1772, or it was not)
'spend ~ impressions + clicks + ad_id1772'

column          coefficient         pvalue
y_intercept     0.02                0.000
impressions     0.00057             0.038
clicks          0.976               0.78
ad_id1772      -0.5                 0.02


6. How much can we assume the ad cost to place online, based on it having
   no impressions?
7. Which part of the model seems insignificant to solving for cost?
8. What effect does ad 1772 have on the cost of the ad?
"""

# 6. 2 cents
# 7. clicks; despite a high coefficient, it seems like clicks isn't related to spend.
# 8. If it is the ad_id 1772, spend seems to be less by 50 cents, on average.

"""
9. What does a Trellis plot allow you to do?
What python library does the Trellis plot come from?
"""

# Trellis quickly allows you to plot a grid of subplots comparing unique values along the x and y axis (of the figure)
# given other data to plot.
# Trellis comes from pandas.

"""
10. What does the reset_index() function do on a DataFrame?
Describe an instance you might need to use it.
"""

# Reset index moves the current index (or MultiIndex) as separate columns to be referenced.
# It could be used to change a series into a dataframe, or make it simpler to subset along the index.
