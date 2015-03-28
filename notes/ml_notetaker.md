# Machine Learning Notetaker

Use this notetaker for each algorithm so you can keep track of the important information for each algorithm

## logistic regression

> What data problem does it solve?

categorical (mostly binary)
supervised learning (uses a training set)

> How do we evaluate performance?

accuracy (model-level): number correct / number of observations
chi^2 test (feature-level):

> What is the output?

probability: value btw 0 and 1

> What is interpretable of the algorithm?

log-odds (coefficients): how likely an input fits a category
average result given no information (X% of observations are category 1)

> How is it prone to overfitting?

assume same concerns as linear regression

> How is it customizable?

regularization parameters


## Naive Bayes

> What data problem does it solve?

classification - where does this obeservation belong?

> How do we evaluate performance?

accuracy
confusion matrix

> What is the output?

conditional probability - probability of target class, given input features

> What is interpretable of the algorithm?

probability of a feature, given the target
probability of features
a priori information (independent probability of target)

> How is it prone to overfitting?

all features are independent of each other ("naive"), so less likely to overfit
does very well with small data sets
good predictor, bad estimator: predicts very well on large data sets, but coefficients tend to be less useful

> How is it customizable?

sklearn includes alpha parameter, so we assume some type of regularization
several "versions":
    multinomial: counting (how often does this feature show up?)
    bernoulli: presence (does this feature show up?)


## Support Vector Machines

> What data problem does it solve?

supervised, can classify or regress
discriminitive, uses a decision line to split data into definitive classes

> How do we evaluate performance?



> What is the output?

hyperplane, a vector that divides the data

> What is interpretable of the algorithm?



> How is it prone to overfitting?

relies on specific data points in the training set to build the model

> How is it customizable?

kernels - designates linear or non-linear hyperplanes
C parameter - error-tolerance of hyperplane, impacts margin
alpha parameter - scalar multiplier


## K Nearest Neighbors (KNN)

> What data problem does it solve?

supervised
classification
generative, gets a feel for what the classes *should* be based on the data
solves for class using distance and similarity

> How do we evaluate performance?

regression - mean squared error
classification - confusion matrix

> What is the output?

class labels - generative, solved using all data and their labels first

> What is interpretable of the algorithm?

nothing like a coefficient

> How is it prone to overfitting?

if the threshold (k) for each group isn't reasonable

> How is it customizable?

*k* - the number of nearest neighbors to find
distance metric can be changed - Minkowski (continuous) and Jaccard (ranked/categorical)


## K Nearest Neighbors (KNN)

> What data problem does it solve?

unsupervised
clustering

> How do we evaluate performance?

"Elbow rule" - plot k against % of variance explained, left of "elbow" is better (majority of variance explained with room for error)
rule sets - trees

> What is the output?

k clusters (every observation assigned to a cluster)

> What is interpretable of the algorithm?

variance of the sum of squares

> How is it prone to overfitting?

Rule of thumb: k clustes should be < o/2
feature scaling - late variances can account for the majority of the cluster

> How is it customizable?

