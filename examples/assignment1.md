Naive Bayes Classification
==========================

Naive Bayes methods are a family of supervised learning algorithms used to solve classification problems in Data Science. They make use of Bayes theorem, assigning prior probabilities based on a set of training data. They are known as 'Naive' methods because they assume that all variables of the dataset are independent.

This is a very strong assumption, and therefore not an accurate predictor of the _probability_ of a test data point being in any given class. However, since the algorithm is only concerned with the classification of the data point - i.e. the _most likely_ class, this is not a problem. It turns out that in most cases, Naive Bayes algorithms do a good job of classifying the data.

The advantage of the 'Naive' assumption is that it makes the algorithm relatively simple, thereby allowing speedy processing. The number of parameters in the algorithm is linear in scale to the number of variables in the dataset, making it useful for dealing with large samples or those with a large number of variables.

Uses
----

1. Naive Bayes algorithms perform particularly well with textual data. A common application is in spam email filters. Training data is used to identify a set of key words and phrases, which form the variables for the algorithm. New emails can then be run through the algorithm, and are classified as 'spam' or 'not spam' based on how often they contain these key words or phrases.

2. There are many other applications in which Naive Bayes methods can be used with textual data. For example, classifying a movie review as positive or negative based upon which words are contained within it.

3. Naive Bayes algorithms can be used in genomics to predict susceptibility to disease. Genomic datasets typically contain a very high number of features, so the dimensional scalability of Naive Bayes methods is important here.
e.g. http://www.ncbi.nlm.nih.gov/pubmed/21672907


# Principal Components Analysis (PCA) and Singular Vector Decomposition (SVD)
_These two are essentially closely related._

Principal Components Analysis (PCA): creates new fewer composite attributes that represent all the attributes. Singular Vector Decomposition: established feature extraction method that has a wide range of applications.

PCA is commonly used in Dimensionality Reduction. We have a lot of variables that are correlated but we can reduce the number of variables by categorizing them, find the best matrix with fewer variables that still can explain the data. SVD deals with data compression.

SVD and PCA are commonly used to solve complex systems such as neuroscience, photoscience, meteorology and oceanography - the number of variables to measure can be unwieldy and at times even deceptive, but the underlying dynamics can often be quite simple.

Application 1:
We are trying to understand some phenomenon by measuring
various quantities (e.g. spectra, voltages, velocities,
etc.) in our system. But we cannot figure out what is happening because the data appears clouded, unclear and even redundant.

Application 2: Image processing (source: UCLA)
We can use SVD to compress and recreate images. For example, we read in a jpeg (pansy.jpg) and plots it, first in color (when the image is stored as three matrices--one red, one green, one blue) and then in gray-scale (when the image is stored as one matrix). Then, using SVD, we can essentially compress the image. We can also recover the image to varying degrees of detail as we recreate the image from different numbers of dimensions from our SVD matrices. We can see how many dimensions are needed before you have an image that cannot be differentiated from the original.

Application 3: neuroscience (source: wikipedia)
In neuroscience, PCA is also used to discern the identity of a neuron from the shape of its action potential. Spike sorting is an important procedure because extracellular recording techniques often pick up signals from more than one neuron. In spike sorting, one first uses PCA to reduce the dimensionality of the space of action potential waveforms, and then performs clustering analysis to associate specific action potentials with individual neurons.


The name of the Algorithm I read was Apriori It solves the problem of Association. the Algorithm basically looks at if and else conditions and stores the number of frequency the condition is met. once its done , It can calculate the probability of an item present just by looking at the antecedent. This algorithm can be widely usued in online marketing where recommendations can be made for purchase upon selecting an specified item. In a cosmetics facory setting , this algorithm can be applied to predict mechanic downtime issues with unique packiging. If there is a type of cap that causes issues on two or three pieces of equipment or a certain type of jar causing downtimes on other pieces of equipment. we can use this algorithm to calculate the probablity of equipment downtime based on packaging profile. Also in a factory setting , as assoication can be made in the tool crib where we can determing the tools that have a high probaility of being used at the same time to be stored in a close proximity to save time for the mechanics to be able to acquire tools in a timely fashion.


#Introducing the Apriori Algorithm

**Solves for:**

1. How often do items occur together in a dataset?
2. How likely are these items to occur together?

**How it works:**

The algorithm addresses the problem in two steps:

1. Identify frequent itemsets in the data.
  * *For example, in a pharmacy transaction dataset, what groups of purchases appear together frequently for customers?*
  * Note: there is a frequency minimum set by the user to improve the power of the analysis.  The lower the frequency threshold, the higher chance of a large number of rules with less strength.
2.  Mathematically describe the relationship between the different items in the itemset.
  * *For example, if a common itemset includes a toothbrush, toothpaste and mouthwash, given two of those items are were purchased, what is the probability the third will also be purchased?*

**Application Overview:**

No.| Application          | Business Question
---|----------------------|----------------------------------------------------------------
1. | CRM messenging       | How can a company optimize their customer communications?
2. | Savings offer bundle | Which products should be bundled in coupons to increase sales?
3. | Product placement    | What products should be placed together on a store shelf?

*Details:*

 1. A travel service wants to understand what other cities customers are likely to travel to based on past bookings. The company will use this analysis to tailor emails to included relevant suggestions and encourage use of the travel service.  The analysis may reveal that customers who book in San Francisco, CA and Austin, TX have a 70% probability of later booking in Portland, OR.  As a result, the service can message people who recently booked in SF and Austin about offerings in Portland, OR.
 2. A CPG company wants to boost sales of it's all-surface cleaner.  The association analysis may show that only 40% of customers who purchase paper towels and sponges also purchase the cleaner.  The CPG company can use this to include a bundle coupon where a discount is offered for the cleaner with the purchase of paper towels and sponges.
 3. A grocer wants to optimize store design and shelving for a new location.  They can use this analysis type to itentify bundles of items that should be placed near one another or in sequence throughout the store. Purchasers of frozen pizzas and hot pockets may also often buy Ben and Jerry's ice cream in 80% of cases. Based on these results, the store would want to put hot pockets, frozen pizza and Ben and Jerry's near one another within the frozens section of the store.
