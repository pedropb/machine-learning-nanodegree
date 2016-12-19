# Dimensionality Reduction

## Principal Component Analysis

### Definition

![PCA Definition](images/review-definition-PCA.png)

![Maximal Variation and Minimal Loss](images/maximal-variation-minimal-loss.png)

### When to use PCA

![When to use PCA](images/when-to-use-pca.png)

### PCA in sklearn

![PCA in sklearn](images/PCA-sklearn.png)

![PCA in sklearn 2](images/PCA-sklearn-2.png)

## Feature Transformation

### Definition

![Feature Transformation Definition](images/feature-transformation-definition.png)

### Independent Component Analysis

Independent component analysis (ICA) is a method in which the goal is to find a linear representation of nongaussian data so that the components are statistically independent, or as independent as possible. [This paper](http://mlsp.cs.cmu.edu/courses/fall2012/lectures/ICA_Hyvarinen.pdf) describes ICA in detail. ICA has also been applied to the information retrieval problem, in a [paper](http://www.cc.gatech.edu/~isbell/papers/isbell-ica-nips-1999.pdf) written by Charles himself.

[The cocktail party demo](http://research.ics.aalto.fi/ica/cocktail/cocktail_en.cgi) is an example of ICA application

![ICA notes](images/ica-notes.png)

### ICA vs PCA

- ICA:
    - finds hidden features 
    - finds *statistically independent* features
    - maximizes mutual information
    - order between found features don't matter
    - works better on nongaussian distributions
    - is a probabilistic analysis
- PCA: 
    - decomposes the data onto orthogonal dimensions
    - maximizes variance
    - maximizes reconstruction
    - order between found features matters - former features cover more variance than latter features
    - works better on gaussian distributions
    - is a linear algebra analysis

![ICA vs PCA examples](images/ica-vs-pca.png)

In the image above:
- *BSS* stands for Blind Source Separation problem (ie: Cocktail Party).
- Directional means that ICA input direction is meaningful. For example, ICA will output two different results for a matrix M and M<sup>T</sup>, while, PCA will output the same result for both inputs.
- Faces: PCA will find Brightness, then Average Face (*eigenfaces*), while ICA will find feature selectors like noses, mouths, eyes, etc.
- Natural Scenes: ICA will find edges.
- Documents: ICA will find topics.

![ICA vs PCA quiz](images/ica-vs-pca-2.png)

### Alternatives

- RCA: Random Component Analysis consists on projecting the data into random dimensions. It works in both cases, when M < N and also where M > N (for example: Kernel Methods)
- LDA: Linear Discriminant Analysis consists of using labels to find projections that summarize the data.

![Alternatives to PCA and ICA](images/alternatives.png)

### Summary

[This excellent paper](http://computation.llnl.gov/casc/sapphire/pubs/148494.pdf) is a great resource for the Feature Transformation methods from this course, and beyond


![Summary](images/summary.png)