# lec01 - 기본적인 Machine Learning의 용어와 개념 설명

[1. What is ML?](#1-what-is-ml)

[2. What is learning?](#2-what-is-learning) &nbsp;&nbsp; 1) supervised &nbsp;&nbsp; 2) unsupervised

[3. What is regression?](3-what-is-regression)

[4. What is classification?](4-what-is-classification)

## 1. What is ML?
머신러닝은 일종의 소프트웨어이다. explicit하게 프로그래밍하기 어려운 경우가 있다. 따라서 일일이 프로그래밍하지 말고 자동적으로 할 수 있도록 데이터를 학습해서 배우는 프로그램이다.

## 2. What is learning?
### 1) supervised
- label이 정해진 데이터(training set)로 학습한다.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 예) image labeling, email spam filter, predicting exam score

- 학습에 사용된 데이터를 training set이라고 한다.
- Type of supervised learing

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; regression - Predicting final exam score based on time spent

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; binary classification - Pass/Non-pass based on time spent

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; multi-label classification - Letter grade (A, B, C, E and F) based on time spent

### 2) unsupervised
label이 정해지지 않은 데이터로 학습한다.

----

## lab01

<br>

![image](https://user-images.githubusercontent.com/55024771/103656515-07471400-4fac-11eb-9361-310fb34132f6.png)

TensorFlow: data flow graphs를 사용해서 numerical computation하는 라이브러리

node가 operation이고 edge가 data(tensor)
