# Machine Learning 공부

모두의 ML : https://hunkim.github.io/ml/

## 1. 수업의 개요
- 머신러닝이란?
- Linear regression
- Logistic regression
- Multivariable linear/logistic regression
- Neural networks
- Deep learning
  - CNN
  - RNN
  - Bidrectional/Neural networks
- Tensorflow, Python

## 2. 머신러닝의 개념과 용어
- limitions of explicit programming.
- supervised learning
  - training set (labled)

- unsupervised learning
  un labled data.

### supervised learning
- regression
- binary classification
- multi-lable classification

### Tensorflow (lab1)
https://www.tensorflow.org/

- data flow graph
- node = mathematical operation
- edge = multidimensional data array(tensor)

- install
```shell
# Mac OS X
$ sudo easy_install pip
$ sudo easy_install --upgrade six
$ pip install tensorflow
```

## 3. Linear Regression 의 개념
- hypothesis
```math
H(x) = Wx + b
```

- cost(loss) function
```math
(H(x) - y)^2

cost = 1/m * M(H(x^(i)) - y^(i))^2

cost(W,b)
```


-----
explicit programming :
explicit vs implicit in programming: https://www.quora.com/What-is-meant-by-implicit-and-explicit-in-programming
