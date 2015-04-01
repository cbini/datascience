#Machine Learning / SKLearn Quiz (Quiz 2)

1. Given the following machine learning matrix, fit each of the following algorithms into their respective places. Some may have multiple.

    .               | continuous          | categorical
    ---------------:|:--------------------|:-----------
    supervised      | regression          | classification
    unsupervised    | dimension reduction | clustering

    Algorithms:
    * Ordinary Least Squares (supervised, continuous)
    * Logistic Regression (supervised, categorical)
    * Naive Bayes (supervised, continuous or categorical)
    * Decision Trees (supervised, continuous or categorical)
    * Support Vector Machines (supervised, continous or categorical)
    * Nearest Neighbors (supervised categorical)
    * K Means (unsupervised categorical)
    * Principal Component Analysis (Matrix Decomposition) (unsupervised continuous)


2. Given the 4 entities in the matrix above, describe a problem / example we worked on in class for each, and provide one idea on your own.



3. All sklearn prediction objects have functions akin to fit(), transform(), predict(), and fit_transform(). Explain each in their most general terms.

    - fit() will "fit" the model to using the training data set
    - transform() will return the input data with any transformations that have been applied to it by the algorithm
    - fit\_transform() will both fit the model and transform the input data at the same time
    - predict() will take a new data set with the same features as the training set and will return its prediction of the target variable for each observation


4. Two of the above algorithms can use kernels (in their sklearn context)
    a. Explain what a kernel does
        - A kernel will optimize how the the underlying algorithm works in order to better fit the data.  For example, SVC can return both a linear hyperplane and a polynomial hyperplane to fit the data--you just have to specifcy kernel that you use.
    b. Which are the two algorithms that use kernels?
        - support vector machines
        - 


5. One of the above algorithms is most obviously not a linear solution to classification (it does not draw straight decision lines). Which algorithm is it, and how does it decide on decision lines?
    - KNN will decide which category an observation belongs in by designating *k* random points in the data set as a local centerpoint ("centron") and assigning each observation to it's nearest centron.


6. You are working on microarray (DNA) samples where number of observations (n) is 5 and number of features (m) is > 10,000.
    1. Describe a supervised and unsupervised technique in order to reduce the number of features in the samples to those that are most significant.
        - feature selection (supervised): you can iterate through each feature and decide whether or not to keep it based on its correlation to the target variable
        - principal component analysis (unsupervised): all features a smashed together into *m* "principal components," each of which are 1D representations of all features in order to explain the variance of the data set.
    2. Compare the two techniques in their solution.
        - feature selection will still return the discrete data of each feature, while PCA will return shades of all the features in each principal component that it returns.


7. Below is a table of Gini Importance (Normalized to 1) in predicting rent in New York City.
    1. Which algorithm uses Gini Importance?
        - Decision Trees
    2. Interpret the table.
        - *sqft* is the feature that will best split the data into groups according to the stopping criteria that the model was fit with, *bathrooms* will add the least marginal amount of information.
        - in order: sqft > bedrooms > distance subway > nearby pizza > distance columbus > bathrooms

    Feature           | GiniImportance
    :-----------------|:--------------
    bedrooms          | 0.211
    bathrooms         | 0.005
    sqft              | 0.532
    distance subway   | 0.198
    distance columbus | 0.017
    nearby pizza      | 0.042


8. What is the Receiving Operator Characteristic Curve? What two metrics is it composed of?
    - the ROC Curve will visualize the predictive accuracy of a classification algorithm
    - it is the plot of the % of True Positives Predicted against the % of False Positives


9. How does a grid search work? Use an example algorithm from above to help explain it.
    - grid search will loop through all specified parameters of an algorithm using defined search criteria in order to find the specific parameters that will provide the "best" optimization according to a particular scoring system.
    
10. Three parts:
    1. What's your strongest "takeaway" from machine learning and this segment of the course?
        - there are a wide variety of algorithms that are tools specialized to solve particular problems. it is up to the data scientist to know the right tool for the job
        
    2. Given a 2 dimensional figure where y=effort to learn and x=immediate usefulness, and slope = 1, what is one algorithm that felt above the slope (more effort to learn than usefulness) and one algorithm that felt below the slope (more usefulness than effort to learn)?
        - above: SVMs
        - below: decision trees
        
    3. What's one question you still have about machine learning?
        - can feature scaling (or lack thereof) invalidate a model?