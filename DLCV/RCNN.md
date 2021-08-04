# R-CNN: Regions with CNN features

- FC는 feature map을 압축해서 일차원으로 만든 것으로 사이즈가 정해져 있다.(feature map 사이즈도 정해져 있다.) -> 다른 이미지 사이즈가 들어가면 안된다.

- selective search 할 때 image crop 후에 이미지 사이즈를 동일하게 바꿈 -> 이미지가 찌그러짐

- feature map을 1차원으로 펴고 SVM 적용

-  
