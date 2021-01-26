# lec12 - RNN

![image](https://user-images.githubusercontent.com/55024771/105851912-12c7b100-6027-11eb-8ed0-0702de26b33a.png)

이전의 연산이 현재 연산에 영향을 미친다.

![image](https://user-images.githubusercontent.com/55024771/105851965-2541ea80-6027-11eb-8e65-1ccb164461cf.png)

new state 계산에 old state가 이용된다.

![image](https://user-images.githubusercontent.com/55024771/105852296-a13c3280-6027-11eb-96b3-05a55c9a9726.png)

h, y의 벡터 크기는 weight 벡터 크기에 의해 정해진다. 

![image](https://user-images.githubusercontent.com/55024771/105852474-d9dc0c00-6027-11eb-85a7-3016e7b3ad1e.png)

w값은 모두 동일하게 적용된다.

![image](https://user-images.githubusercontent.com/55024771/105852747-2e7f8700-6028-11eb-90f2-b2044f037382.png)

h 다음에 오는 문자를 예측한다.

![image](https://user-images.githubusercontent.com/55024771/105852959-7bfbf400-6028-11eb-8888-77dae10b8aab.png)
 
 첫 번째는 이전 h값이 없기 때문에 보통 0으로 놓고 계산한다.

![image](https://user-images.githubusercontent.com/55024771/105853094-a9e13880-6028-11eb-9e03-3ee86643dd04.png)

![image](https://user-images.githubusercontent.com/55024771/105853459-11978380-6029-11eb-9716-ff885c4f70eb.png)

![image](https://user-images.githubusercontent.com/55024771/105854055-b87c1f80-6029-11eb-8281-d80807c147db.png)

![image](https://user-images.githubusercontent.com/55024771/105854791-a9e23800-602a-11eb-9300-51bdebd76ec4.png)

![image](https://user-images.githubusercontent.com/55024771/105855101-0ba2a200-602b-11eb-9158-81bf7f79cac2.png)

![image](https://user-images.githubusercontent.com/55024771/105855155-1bba8180-602b-11eb-8042-095671db8d2c.png)
