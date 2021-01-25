# lec11 - Convolutional Neural Networks

![image](https://user-images.githubusercontent.com/55024771/105681337-5c839f00-5f34-11eb-8511-ba52b85145b6.png)

![image](https://user-images.githubusercontent.com/55024771/105681486-88068980-5f34-11eb-87d0-b428e126cf63.png)

![image](https://user-images.githubusercontent.com/55024771/105681548-99e82c80-5f34-11eb-8804-e06ab111881f.png)

![image](https://user-images.githubusercontent.com/55024771/105681602-aa98a280-5f34-11eb-9ad3-03930d5593c9.png)

![image](https://user-images.githubusercontent.com/55024771/105681648-bb491880-5f34-11eb-9832-9166e19fe939.png)

![image](https://user-images.githubusercontent.com/55024771/105681735-df0c5e80-5f34-11eb-8c6c-373665679ba7.png)

![image](https://user-images.githubusercontent.com/55024771/105681803-f77c7900-5f34-11eb-98b8-63bcf0f8e222.png)

![image](https://user-images.githubusercontent.com/55024771/105681966-2e528f00-5f35-11eb-9539-1875d2fd7bc1.png)

![image](https://user-images.githubusercontent.com/55024771/105682094-580bb600-5f35-11eb-8005-a6b5c8c569bb.png)

stride가 2인 경우

![image](https://user-images.githubusercontent.com/55024771/105682691-19c2c680-5f36-11eb-9070-5fe10904a7dc.png)

![image](https://user-images.githubusercontent.com/55024771/105682766-319a4a80-5f36-11eb-8eae-7dd15cdc29bc.png)

이미지가 작아지면서 정보 소실이 발생한다.

![image](https://user-images.githubusercontent.com/55024771/105682827-437bed80-5f36-11eb-9dbd-5417097d1254.png)

이는 padding으로 해결

그림이 급격하게 작아지는 것을 방지하고 그림의 모서리를 알려준다.

![image](https://user-images.githubusercontent.com/55024771/105683071-92298780-5f36-11eb-92ed-e2d361e46bd7.png)

![image](https://user-images.githubusercontent.com/55024771/105683376-e9c7f300-5f36-11eb-9add-b9eb1c145417.png)

![image](https://user-images.githubusercontent.com/55024771/105683450-fea48680-5f36-11eb-8602-91882617c11b.png)

![image](https://user-images.githubusercontent.com/55024771/105683645-2f84bb80-5f37-11eb-9c0d-f0813519e052.png)

![image](https://user-images.githubusercontent.com/55024771/105683977-a91ca980-5f37-11eb-991f-8eb4d24adfa5.png)

![image](https://user-images.githubusercontent.com/55024771/105684102-d8331b00-5f37-11eb-9279-fe873848b73a.png)

첫 번째 activation map에서 weight 개수는 5 * 5 * 3 * 6개

두 번째 activation map에서는 5 * 5 * 3 * 10개

초기화 방법은 random하게 초기화한 후 학습

## Max pooling and others

layer 한 개씩 뽑아서 사이즈를 작게 만드는 것

![image](https://user-images.githubusercontent.com/55024771/105684521-6909f680-5f38-11eb-8d05-93066b8356ab.png)

![image](https://user-images.githubusercontent.com/55024771/105684729-aff7ec00-5f38-11eb-8df2-16d4ffdaaddf.png)

** [ConvNetJS demo: training on CIFAR-10] **

https://cs.stanford.edu/people/karpathy/convnetjs/demo/cifar10.html

## CNN case study

![image](https://user-images.githubusercontent.com/55024771/105686196-52649f00-5f3a-11eb-9a16-e3ab56ca9e3c.png)

#1. conv layer

![image](https://user-images.githubusercontent.com/55024771/105686377-817b1080-5f3a-11eb-9435-b95dd12a8892.png)

#2. pooling layer

![image](https://user-images.githubusercontent.com/55024771/105686463-9b1c5800-5f3a-11eb-9155-8a8dd0dac9bb.png)

![image](https://user-images.githubusercontent.com/55024771/105686595-c737d900-5f3a-11eb-8e8c-729f7c74d395.png)

![image](https://user-images.githubusercontent.com/55024771/105687231-8c827080-5f3b-11eb-9076-15fffd2dcb69.png)

fast forward를 사용

![image](https://user-images.githubusercontent.com/55024771/105687407-c0f62c80-5f3b-11eb-9e4b-e53480c0eed5.png)

![image](https://user-images.githubusercontent.com/55024771/105687521-e5520900-5f3b-11eb-91b9-765314567243.png)

전체적인 깊이는 깊지만 실제로 학습할 때는 layer가 깊지 않은 느낌으로 학습할 수 있다.

![image](https://user-images.githubusercontent.com/55024771/105687587-f8fd6f80-5f3b-11eb-820e-04e5e385f11f.png)

![image](https://user-images.githubusercontent.com/55024771/105687815-4083fb80-5f3c-11eb-9c6e-0b3da0eacccb.png)

![image](https://user-images.githubusercontent.com/55024771/105687894-5691bc00-5f3c-11eb-8d0b-c4656f42f4fd.png)

![image](https://user-images.githubusercontent.com/55024771/105688016-788b3e80-5f3c-11eb-895e-ecede998bb65.png)


