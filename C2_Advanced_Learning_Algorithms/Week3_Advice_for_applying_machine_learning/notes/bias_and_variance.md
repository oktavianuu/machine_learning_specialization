# Bias and Variance
## 1) High Bias (Underfit)
- Underfit or high bias algorithm means that the algorithm does not do well on the training data. This causing large errors on both J-train and J-CV train.
- Jtrain and J-CVtrain are high, they have large errors
- this means that high bias algorithm is not even doing well on the training data.
- Example, J=1 
- This also means that the Jtrain and J-CV is close to each other in terms of errors, they're both high. 

## 2) High Variance
- Also called overfit, this is where the algorithm perform very well on the training set. It performs best on the training set, but poor on CV. 
- Jtrain is low but JCV high. 
- JCV much higher on the the Jtrain. It only good on the seen data but not the unseen. 
- Example, J=4
- JCV is much higher than Jtrain, J-CV >> Jtrain

## 3) Just right
- low Jtrain, low JCV
- for example, d=2

## 4) Notes
- As the degree of polynomial increases, the error tend to decreases. 
- It is possible for an algorithm to have both high bias and high variance. In this case, the Jtrain will be high and the J-CV is even much higher. 
- In the case of high bias and high var, the algorithm perform better on some part (half) of the input but perform worse on the other half of the input. 

# Regularization
- How to determine a good value of lambda (the regularization param of the algorithm). 
- 
