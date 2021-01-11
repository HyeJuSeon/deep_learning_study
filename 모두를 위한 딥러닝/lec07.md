# lec07 - learning rate, overfitting, regularization


## learing rate

![image](https://user-images.githubusercontent.com/55024771/104178941-7a3e0800-544e-11eb-8aad-c4df4a04beb5.png)

![image](https://user-images.githubusercontent.com/55024771/104179015-917cf580-544e-11eb-9fb9-d2fda414c646.png)

따라서 data set에 따라 cost functino 값을 관찰하고 learning rate을 설정

## preprocessing

![image](https://user-images.githubusercontent.com/55024771/104179272-eae52480-544e-11eb-87f7-0fdbe172d110.png)

![image](https://user-images.githubusercontent.com/55024771/104179446-3697ce00-544f-11eb-858b-f1d25405d2fc.png)

![image](https://user-images.githubusercontent.com/55024771/104179401-22ec6780-544f-11eb-883d-3a4eeb7aa93a.png)

![image](https://user-images.githubusercontent.com/55024771/104179500-4b746180-544f-11eb-8638-5032d791df04.png)

## overfitting

![image](https://user-images.githubusercontent.com/55024771/104179614-78287900-544f-11eb-96bc-ec25fd4ba896.png)

**해결방법**은 1) training data 수를 늘린다 2) feature 수를 줄인다 3) regularization

## regularization

일반적인 방법: 각 element를 제곱해서 합하는 항을 더한다.

![image](https://user-images.githubusercontent.com/55024771/104179821-cb023080-544f-11eb-9bb1-ade9b3900a7b.png)

lambda가 0이면 regularization X

lambda가 큰 값이면 regulariztion의 중요성은 커짐

## training set, test set

![image](https://user-images.githubusercontent.com/55024771/104180665-d86bea80-5450-11eb-8968-9e4d4d14820f.png)

![image](https://user-images.githubusercontent.com/55024771/104180607-becaa300-5450-11eb-9eac-457b308c993e.png)

validation set은 parameter tunning을 위한 것

![image](https://user-images.githubusercontent.com/55024771/104180699-e7529d00-5450-11eb-9903-570a0ff577ce.png)

## online learning

새로운 데이터가 생겼을 때 이전 데이터(100만개)를 새로 학습시키지 않고 새로운 데이터만 추가로 학습시킬 수 있기 때문에 유용

![image](https://user-images.githubusercontent.com/55024771/104180852-28e34800-5451-11eb-92ff-4a8b7ecaf3b4.png)


