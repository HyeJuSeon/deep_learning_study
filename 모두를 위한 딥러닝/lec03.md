# lec03 - Linear Regression and How to minimize cost

[1. Linear Regression](#1-linear-regression)

[2. How to minimize cost](#2-how-to-minimize-cost)

## 1. Linear Regression

![image](https://user-images.githubusercontent.com/55024771/103666994-b25dca80-4fb8-11eb-8416-f149a8438c17.png)

![image](https://user-images.githubusercontent.com/55024771/103667055-c73a5e00-4fb8-11eb-89df-f0454881c65b.png)


## 2. How to minimize cost

![image](https://user-images.githubusercontent.com/55024771/103669618-ebe40500-4fbb-11eb-8495-c4aaf75ea2ee.png)

![image](https://user-images.githubusercontent.com/55024771/103669688-05854c80-4fbc-11eb-881a-9bac822c60b4.png)

![image](https://user-images.githubusercontent.com/55024771/103669814-2a79bf80-4fbc-11eb-8548-93cbb5e0e995.png)


## Gradient descent algorithm
cost를 최소화하는 W, b를 찾음

1. 임의의 값으로 W, b값 초기화
2. 미분값(기울기) 구해서 cost가 최소화 되는 방향으로 W, b를 업데이트
3. Repeat
4. 최소점에 도달하면 종료

![image](https://user-images.githubusercontent.com/55024771/103667587-7a0abc00-4fb9-11eb-9326-7285b81c1c65.png)

![image](https://user-images.githubusercontent.com/55024771/103667818-bccc9400-4fb9-11eb-9202-c995760c2837.png)


m의 계수는 cost에 영향을 거의 주지 않음



![image](https://user-images.githubusercontent.com/55024771/103668133-2351b200-4fba-11eb-9326-4455ee3380e2.png)

![image](https://user-images.githubusercontent.com/55024771/103668333-55fbaa80-4fba-11eb-9511-b1657b0494b2.png)


alpha: learning rate, 즉 업데이트한 미분값의 반영 정도를 결정


![image](https://user-images.githubusercontent.com/55024771/103668666-af63d980-4fba-11eb-8c6d-2319954c257e.png)


gradient descent는 원래 W에서 cost function을 W로 편미분한 값에 특정값 alpha(learning rate)를 뺀 것


![image](https://user-images.githubusercontent.com/55024771/103668800-dd491e00-4fba-11eb-81d4-71376d37be71.png)


local minimum이 여러 개인 경우 global minimum인지 확인할 수 없기 때문에 gradient descent를 사용할 수 없다.


![image](https://user-images.githubusercontent.com/55024771/103668967-1da89c00-4fbb-11eb-832f-e2aece9708c2.png)


local minimum과 global minimum이 동일한 경우엔 사용 가능
