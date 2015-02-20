"""
1. What's the primary difference between the following two ipython magic (%)
commands?
"""

%matplotlib inline
%pylab inline

## The first line will only load matplotlib inline in IPython Notebook
## THe secon will load both matplotlib and numpy

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

ads = pd.read_csv("https://gist.githubusercontent.com/podopie/be35a78b76501c7c63b0/raw/fcb6283e1ac0fcf60fc5ba43ea908680ee16e282/ads.csv", skiprows=3, skipfooter=1, header=0)
ads.head()


"""
3. With the ads dataset stored in name `ads`, write code that'd create a subset
of just ad_id 200 where the spend was more than 30 dollars

subset = ads...(some_code)...
"""

subset = ads[(ads.ad_id == 200) & (ads.spend >= 300)]
subset.head()

## Unless I'm doing something wrong, there is no ad_id 200

"""
4. We want to aggregate the sum of spend by day and ad. What code would return
back that dataset?
"""

ads_date = ads.groupby('date')
print ads_date.spend.sum()

ads_id = ads.groupby('ad_id')
print ads_id.spend.sum()


"""
5. Explain what the following code block is doing, line by line.
"""
import matplotlib.pyplot as plt ## import matplotlib into the namespace
from __future__ import division ## import the python 3 division module

ads['ctr'] = ads['clicks'] / ads['impressions']  ## create a new column that shows click per impression

fig = plt.figure()  ## create a plot object
plt.subplot(1, 2, 1) ## define the first subplot of a 1x2 plot
plt.hist(ads.spend) ## create a histogram using the data in the spend column

plt.subplot(1, 2, 2) ## define the second subplot
plt.plt(ads.spend, ads.ctr, 'g.') ## create a scatter plot of spend vs ctr, colored green
plt.show() ## display the figure


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
## 6. $0.02

## 7. clicks -- the p-value is very high

## 8. It has a negative correlation, ad 1772 is generally cheaper to place

"""
9. What does a Trellis plot allow you to do?
What python library does the Trellis plot come from?
"""
## A Trellis plot lets you loop over a data set, creating multiple plots using different subsets
## It comes from the rplot library, which is included as one of pandas miscellaneous toolsets

"""
10. What does the reset_index() function do on a DataFrame?
Describe an instance you might need to use it.
"""
## reset_index() will reset the index column of a dataframe to a default index number
## you would need to use this after melting a dataset and wanting to use the values of the resulting index column for another operation
