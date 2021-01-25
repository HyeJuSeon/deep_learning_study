# lec10 = ReLU, Initialize Weight, Dropout and Ensemble, Network Module

## ReLU

![image](https://user-images.githubusercontent.com/55024771/104817608-a8b04e80-5865-11eb-9618-86b1e64f3297.png)

입력이 최종값에 거의 영향을 미치지 않는 문제점이 있다. : Vanishing gradient

![image](https://user-images.githubusercontent.com/55024771/104817754-866b0080-5866-11eb-8269-8aa283341a2e.png)

![image](https://user-images.githubusercontent.com/55024771/104817795-dea20280-5866-11eb-9437-650e37995cf0.png)

sigmoid함수로 1보다 작은 값으로 만들어지기 때문에 최종값이 매우 작게 나온다. 따라서 ReLU함수 사용

![image](https://user-images.githubusercontent.com/55024771/104817818-101ace00-5867-11eb-90e9-e4317ce5a4a3.png)

![image](https://user-images.githubusercontent.com/55024771/104817844-3c364f00-5867-11eb-92d6-7374a266d728.png)

최종값은 0~1 사이의 값이 나와야하기 때문에 sigmoid함수 사용

![image](https://user-images.githubusercontent.com/55024771/104817857-5ec86800-5867-11eb-8b90-fa18b9506691.png)

![image](https://user-images.githubusercontent.com/55024771/104817880-8f100680-5867-11eb-879f-7d98b8081dc8.png)

![image](https://user-images.githubusercontent.com/55024771/104817900-ae0e9880-5867-11eb-85fa-8c0b02b9d260.png)

## Initialize Weight

w = 0이면 앞에 모든 gradient도 0

![image](https://user-images.githubusercontent.com/55024771/104818027-4a389f80-5868-11eb-972d-ec46246c3372.png)

RBM을 사용해서 초기화 시킨 네트워크를 DBN이라고 한다.

![image](https://user-images.githubusercontent.com/55024771/105151226-1059e880-5b49-11eb-9298-1987befeb8d3.png)

x값을 비교해서 차이가 최저가 되도록 wight를 조절

![image](https://user-images.githubusercontent.com/55024771/105151684-96762f00-5b49-11eb-8cdf-b653228ad445.png)

encoder, decoder라고도 한다.

![image](https://user-images.githubusercontent.com/55024771/105152054-11d7e080-5b4a-11eb-96db-d33e0ef09232.png)

인접한 두 레이어를 encode, decode를 반복하면서 처음값이 부여한 값과 유사하게 나오는 weight를 학습시킬 수 있다. 다음 레이어로 이동해서 반복한다.

![image](https://user-images.githubusercontent.com/55024771/105152269-49468d00-5b4a-11eb-9483-d5cfbfcdea38.png)

![image](https://user-images.githubusercontent.com/55024771/105152641-c8d45c00-5b4a-11eb-906d-10cd0bc046d9.png)

![image](https://user-images.githubusercontent.com/55024771/105152839-0a650700-5b4b-11eb-8e52-134a459bd50f.png)

RBM과 비슷한 결과가 나온다.

![image](https://user-images.githubusercontent.com/55024771/105152989-3da79600-5b4b-11eb-940f-9112252d2252.png)

![image](https://user-images.githubusercontent.com/55024771/105153175-79daf680-5b4b-11eb-89fc-4a856fc914d7.png)

![image](https://user-images.githubusercontent.com/55024771/105153278-96772e80-5b4b-11eb-925b-f5358096c2c4.png)

두가지 문제 해결

![image](https://user-images.githubusercontent.com/55024771/105153361-b0b10c80-5b4b-11eb-887a-43b8b6386d79.png)

## NN dropout

![image](https://user-images.githubusercontent.com/55024771/105651574-9768e100-5efa-11eb-8118-3d768691747d.png)

![image](https://user-images.githubusercontent.com/55024771/105651642-c7b07f80-5efa-11eb-9875-63eae0dd90cc.png)

![image](https://user-images.githubusercontent.com/55024771/105651727-fc243b80-5efa-11eb-8555-1813ff8a1ef9.png)

overfitting을 해결하는 방법으로 dropout도 있다. 

dropout은 학습시킬 때 랜덤하게 neuron을 사용하지 않고 예측할 때는 모두 사용한다.

![image](https://user-images.githubusercontent.com/55024771/105651815-37266f00-5efb-11eb-9cd4-1c0f90639089.png)

![image](https://user-images.githubusercontent.com/55024771/105651847-4ad1d580-5efb-11eb-9b7d-f84c84e41967.png)

## Ensemble

똑같은 형태의 NN을 만들고 나온 결과를 합친 것

![image](https://user-images.githubusercontent.com/55024771/105652075-cc296800-5efb-11eb-9a18-f4a805c3951d.png)

## Network Module

![image](https://user-images.githubusercontent.com/55024771/105652135-ee22ea80-5efb-11eb-905a-be3ee6021f3d.png)

이전의 결과를 합침

![image](https://user-images.githubusercontent.com/55024771/105652259-27f3f100-5efc-11eb-9ce8-5ed9822b9269.png)

![image](https://user-images.githubusercontent.com/55024771/105652372-67224200-5efc-11eb-912d-02dd13dc973a.png)

![image](https://user-images.githubusercontent.com/55024771/105652425-8c16b500-5efc-11eb-92a6-c187bd9ec2fd.png)

