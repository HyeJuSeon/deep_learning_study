# lec06 - Softmax Classifier

![image](https://user-images.githubusercontent.com/55024771/103802649-cf66cc00-5092-11eb-88d1-3982a805ed42.png)

A or not, B or not, C or not 으로 binary classification 3가지 독립된 경우로 나눌 수 있다.

logistic regression 여러 개로 multinomial classification 구현이 가능하다. 

![image](https://user-images.githubusercontent.com/55024771/103802724-eb6a6d80-5092-11eb-91cf-0da9c92a36e5.png)

![image](https://user-images.githubusercontent.com/55024771/103802836-1b197580-5093-11eb-9506-83810893872a.png)

matrix 한 개로 합침.

y hat은 예측값을 의미한다. y hat 각각에 sigmoid 함수를 적용해야 한다.

![image](https://user-images.githubusercontent.com/55024771/103803014-5320b880-5093-11eb-9ed3-ce375db6376d.png)

![image](https://user-images.githubusercontent.com/55024771/103803466-f4a80a00-5093-11eb-8c4f-17159d99f864.png)

![image](https://user-images.githubusercontent.com/55024771/103803560-130e0580-5094-11eb-9d2d-aae6e1e3424e.png)

예측값이 0~1 사이이고 모두 더한 값이 1로 만들어야 한다.

sigmoid 함수보다 더 효율적인 softmax function 이용

![image](https://user-images.githubusercontent.com/55024771/103803804-6ed88e80-5094-11eb-8f7d-6171bb54a3f8.png)

one hot encoding 사용하여 하나만 1, 나머지는 0으로

![image](https://user-images.githubusercontent.com/55024771/103803887-9596c500-5094-11eb-9cdb-7b403a2c3872.png)

![image](https://user-images.githubusercontent.com/55024771/103803989-bced9200-5094-11eb-848c-5cf37de431fa.png)

1. 실제값이 B인 경우

예측이 맞았을 때는 cost=0이고 아니면 cost=무한대

![image](https://user-images.githubusercontent.com/55024771/103804324-43a26f00-5095-11eb-92ac-2dcb381fb0b1.png)

2. 실제값이 A인 경우

![image](https://user-images.githubusercontent.com/55024771/103804514-97ad5380-5095-11eb-8094-b5e551410368.png)

![image](https://user-images.githubusercontent.com/55024771/103804712-e0fda300-5095-11eb-8f9b-92c56d6a0864.png)



![image](https://user-images.githubusercontent.com/55024771/103804818-07bbd980-5096-11eb-90db-7dc02d12053d.png)

![image](https://user-images.githubusercontent.com/55024771/103804945-35a11e00-5096-11eb-9801-2a78d9f66de7.png)
