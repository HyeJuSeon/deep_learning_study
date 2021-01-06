# lec05 - Logistic Classification

![image](https://user-images.githubusercontent.com/55024771/103753152-049cfb00-504e-11eb-84a7-f8c51d15acb4.png)

linear regression에서

![image](https://user-images.githubusercontent.com/55024771/103753869-e8e62480-504e-11eb-95a3-82dfad383efe.png)

<br>

![image](https://user-images.githubusercontent.com/55024771/103755227-d371fa00-5050-11eb-8717-d5b26ee6cff2.png)

hypothesis 값이 0보다 작거나 1보다 클 수 있고 새로운 데이터를 학습한 데이터에서는 pass임에도 fail이 나올 수 있다. 

**따라서 logistic hypothesis의 값이 0~1이도록 만들어야 한다.**

![image](https://user-images.githubusercontent.com/55024771/103753662-a91f3d00-504e-11eb-9531-ef07840dd815.png)

![image](https://user-images.githubusercontent.com/55024771/103755570-61e67b80-5051-11eb-84fa-80abe936403b.png)

cost function의 local minimum이 여러 개인 경우엔 gradient descent를 사용할 수 없다.

![image](https://user-images.githubusercontent.com/55024771/103783191-bef72700-507b-11eb-99c7-eb94d2595f90.png)

![image](https://user-images.githubusercontent.com/55024771/103783328-ec43d500-507b-11eb-80b3-7c45a8ade4c2.png)

y=1일 때,

H(X)=1이면 cost=0

H(X)=0이면 cost=무한대

y=0일 때,

H(X)=1이면 cost=무한대

H(X)=0이면 cost=0


![image](https://user-images.githubusercontent.com/55024771/103783474-1eedcd80-507c-11eb-9bed-55853267c515.png)

C(H(x), y) = - y*log(H(x)) - (1-y)*log(1-H(x))

![image](https://user-images.githubusercontent.com/55024771/103784076-de428400-507c-11eb-9529-979ccae1050a.png)

![image](https://user-images.githubusercontent.com/55024771/103784192-fd411600-507c-11eb-8596-7f5be116293d.png)

**summary**

![image](https://user-images.githubusercontent.com/55024771/103784592-7b9db800-507d-11eb-811e-cdd47cf323c7.png)

