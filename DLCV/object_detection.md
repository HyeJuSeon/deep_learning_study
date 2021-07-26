# object detection

<br>

## localization vs object detection vs segmentation 

localization: 1개 이미지에 1개 object 위치를 bounding box로 지정하여 찾음

object detection: 1개 이미지에 여러 개 object들의 위치를 bounding box로 지정하여 찾음

segmentation: pixel 레벨 detection

-> Localization / object detection은 해당 object의 위치를 bounding box로 찾고(box regression), bounding box내의 object를 판별(classification)

<br>

## 일반적인 object detection 모델

1. region proposal
2. feature extraction & FPN & network prediction
3. IOU, NMS, mAP, Anchor box

<br>

## Object detection의 난제

1. classification과 regression 동시에
2. 다양한 크기와 유형의 object가 섞여 있다.
3. 수행 시간
4. 이미지가 명확하지 않은 경우 / 전체 이미지에서 detect할 object가 차지하는 비중이 높지 않음
5. training dataset 부족(annotation을 만들어야 하기 때문에 어려움)

<br>

## object localization 개요

**img(224x224) -> feture extractor -> feature map(7x7x512) -> dense layer(classification layer) -> FC layer -> softmax class**

- feature extractor: img에서 중요한 features 뽑아냄

- feature map: 사이즈 줄고, 채널 수 증가

<br>

**dense layer(classification layer) -> bounding box regression**

- 특정 feature map이 나오면 특정 regression을 적용하도록

<br>

