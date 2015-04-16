## Objectives
* run through the lights in the room problem from lecture
* Use kernels with PCA
* Application of PCA to new data

## The lights in a room problem
To verify that the light problem works out, we can generate some random data and test the theory.

    # Libraries and seed set
    from pandas import DataFrame
    from matplotlib import pyplot as plt
    import numpy as np
    from sklearn.decomposition import PCA
    np.random.seed(500)


Generate some data--we're building out a few lights in our room, and the data the cameras recorded.

intensities:   the lights<br />
recorded_data: data from our camera, generated through dists and the cameras (recorders)

    recorders   = DataFrame({'locations' : ('A', 'B', 'C', 'D'), 'X' : (0, 0, 1, 1), 'Y' : (0, 1, 1, 0)})
    locations   = np.array([ [.3, .5], [.8, .2] ])
    intensities = np.array([
        [np.sin(np.array(range(100)) * np.pi/10) + 1.2],
        [np.cos(np.array(range(100)) * np.pi/15) * .7 + .9]]).T
    distances   = np.array([
        np.sqrt((locations[0] - recorders.X[i])**2 + (locations[1] - recorders.Y[i])**2) for i in range(4)]).T

    data = np.dot(intensities, np.exp(-2*distances))
    data_transposed = data.T

Take the mean of each column so we can later center the data--extremely useful for PCA.

    row_means = [np.mean(i) for i in data_transposed]
    data_transposed_scaled = np.array([data_transposed[i][0] - row_means[i] for i in range(4)])

Now that all the data has been generated, we can build the PCA model.

    pca = PCA()
    pca.fit(data_transposed_scaled)

Pull out variance as an array. To make it easier to determine what to keep, scale the top variance to 1--in this practice, we should keep everything above .1 post scaling.

In the plot below, we can use the elbow rule to say that the first two components are useable and the last two are not.

    variance = pca.explained_variance_ratio_
    readable_variance = variance * (1/variance[0])
    plt.plot(range(4), readable_variance)
    plt.show()

Plotting all four components against eachother, we can see how clear the patters are for the first two (red and blue), while the others are much less readable/useable.

    colors = ('red', 'blue', 'green', 'orange')
    for i in range(4):
        plt.plot(range(100), pca.components_[i], c=colors[i])

## Using Kernels with PCA

Code accessible in the [repo](https://github.com/podopie/DS_GA_NYC/blob/master/DS_NYC3_sample_code/lesson_12_plot_kernel_pca.py).

## Application of PCA to data
Submit answers on Schoology for 1-2 under Classwork PCA.

1. Work through the iris data set include in sklearn and determine how many principal components are required to accurately predict the data. Note: you should be able to graph it, so it has to be one or two :)

2. Try using a kernel to make the PCs have an even clearer distinction between each class label in the iris data set. Submit your parameters in Schoology.

3. The data from the KPCA section of lecture is from [this data](https://github.com/podopie/DS_GA_NYC/blob/master/DS_NYC3_sample_code/wine.csv). See what you can reproduce using KPCA to accurately predict the "Wine" column.

4. How can PCA/KPCA be used on either the baseball or cars problem? Continue practicing your application of these data sets and see how you can improve your current model implementation.


## Resources
- [A Tutorial on PCA](http://www.snl.salk.edu/~shlens/pca.pdf)
- [Stanford PCA Tutorial](http://ufldl.stanford.edu/wiki/index.php/PCA)
- [Aaron's PCA/3d/clustering post](http://planspace.org/2013/02/03/pca-3d-visualization-and-clustering-in-r/)