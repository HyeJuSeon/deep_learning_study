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

## object detection

bounding box만 모델에 넣어서는 inference가 어려움

### 1) sliding window

window를 왼쪽 상단부터 오른쪽 하단으로 이동시키면서 object detection

#### (1) 다양한 형태의 window를 각각 sliding

#### (2) window scale은 고정하고 image scale을 변경한 여러 이미지를 사용

#### (3) (1) + (2)한 방식

- object detection의 초기 기법으로 활용
- object가 없는 영역도 슬라이딩해야 하며 여러 형태의 window와 여러 scale의 이미지를 스캔해서 검출해야 하므로 수행 시간이 오래 걸리고 성능이 상대적으로 낮음
- region proposal 기법 등장으로 활용도는 떨어졌지만 object detection 발전을 위한 기술적 토대 제공

### 2) region proposal

object가 있을만한 후보 영역을 찾는 것

- 대표적인 방법

빠른 detection과 높은 recall 예측 성능 만족하는 알고리즘

컬러, 무늬(texture), 크기(size), 형태(shape)에 따라 유사한 region을 계층적 그룹핑 방법으로 계산 -> edge detect

selective search는 최초에는 pixel intensity 기반한 graph-based segment 기법에 따라 over segmentation을 수행

<br>

**selective search**

#1. 개별 segment된 모든 부분들을 bounding box로 만들어서 region proposal 리스트로 추가

#2. 컬러, 무늬, 크기, 형태에 따라 유사한 segment들을 그룹핑

#3. 다시 #1 region proposal 리스트 추가, #2 유사도가 비슷한 segment들 그룹핑을 계속 반복하면서 region proposal 수행

<br>

## selective search 실습

[AlpacaDB selectivesearch](https://github.com/AlpacaDB/selectivesearch)
