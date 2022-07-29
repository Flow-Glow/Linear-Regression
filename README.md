# Linear Regression
## What is Linear Regression?
  In linear regression, the relationships are modeled using linear predictor functions whose unknown model parameters are estimated from the data. Such models are called linear models. Most commonly, the conditional mean of the response given the values of the explanatory variables (or predictors) is assumed to be an affine function of those values; less commonly, the conditional median or some other quantile is used. Like all forms of regression analysis, linear regression focuses on the conditional probability distribution of the response given the values of the predictors, rather than on the joint probability distribution of all of these variables, which is the domain of multivariate analysis.
  
### What is Gradient Descent/ Stochastic Gradient Descent
  Gradient descent is an optimization algorithm used to minimize some function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient. In machine learning, gradient descent is used to update the parameters of a model in order to minimize a cost function.

  Stochastic gradient descent (SGD) is a variation of gradient descent where instead of updating the parameters after processing all training data, the parameters are updated after each training example is processed.
- - - - 
### Flow Chart
![image](https://user-images.githubusercontent.com/89105476/152719356-fba3d020-ca56-471a-a025-a5e398628863.png)

## How it works?
#### Grid Search
1. Generate data 
2. Generate a line by generating the slope array and the y intercept array
3. find Euclidean distance between line and all data points
4. Add all the euclidean distance together to get score of the line
5. Repeat all steps above until went over every number in slope array and y - intercept array
#### Least Squares
1. Generate data 
2. Generate a line by generating the slope and the y intercept by using the least squares formula
3. find Euclidean distance between line and all data points
4. Add all the euclidean distance together to get score of the line
- - - - 
## Linear Regression in action:

### Least Squares
![image](https://user-images.githubusercontent.com/89105476/152720525-1580cf30-89eb-4f9d-b9f1-8eb7ec8a7c69.png)

### Brute Force
![image](https://user-images.githubusercontent.com/89105476/152720721-ec7fd821-2605-4b5d-a6d3-f63f1036cde4.png)

- - - - 

### Sources :
1. [Yale Statistics Department](http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm)
2. [Linear Regression Wikipidia](https://en.wikipedia.org/wiki/Linear_regression)
3. [Stochastic Gradient Descent Wikipidia](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)
4. [Gradient Descent Wikipidia](https://en.wikipedia.org/wiki/Gradient_descent)

   
