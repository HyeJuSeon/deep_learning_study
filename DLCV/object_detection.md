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

<br>

## Metric - IOU(Intersection of Union)

- IOU = area of overlap / area of union

<br>

## NMS(Non Max Suppression)

Detected Object의 bounding box 중에 가장 적합한 box를 선택하는 기법

- 배경: Object Detection 알고리즘은 object가 있을만한 위치에 많은 detection을 수행하는 경향이 강함

#1. 특정 confidence threshold 이하 bounding box 제거 (ex. confidence score < 0.5)
#2. 가장 높은 confidence score를 가진 box 순으로 내림차순으로 정렬
#3. 모든 box에 순차적으로 높은 confidence score를 가진 box와 겹치는 다른 box들을 모두 조사하여 IOU가 특정 threshold 이상인 box 모두 제거 (ex. IOU > 0.4)
#4. 남아있는 box만 선택

- confidence score가 높을수록, IOU threshold가 낮을수록 많은 box가 제거됨

<br>

## Metric - mAP(mean Average Precision)

실제 Object가 Detected된 재현율(Recall)의 변화에 따른 정밀도(Precision)의 값을 평균한 성능 수치

### 정밀도(Precision)와 재현율(Recall)

- 주로 이진 분류(binary classification)에서 사용되는 성능 지표
- 정밀도(precision): 예측을 positive로 한 대상 중 실제값이 positive로 일치한 데이터의 비율
- 재현율(recall): 실제값이 positive인 대상 중 예측을 positive로 한 데이터의 비율

<br>

- Object Detection에서 개별 object에 대한 detection 예측이 성공했는지 여부를 IOU로 결정
- 일반적으로 IOU가 0.5이상이면 예측 성공으로 인정 (PASCAL VOC Challenge 기준)

<br>

### 오차 행렬(Confusion Matrix)

이진 분류의 예측 오류가 얼마인지와 더불어 어떠한 유형의 예측 오류가 발생하고 있는지를 나타내는 지표

- TN(True Negative): 실제 N, 예측 N
- FP(False Positive): 실제 N, 예측 P
- FN(False Negative): 실제 P, 예측 N
- TP(True Positive): 실제 P, 예측 P

<br>

- Precision = TP / (FP + TP)
- Recall = TP / (FN + TP)

<br>

**업무에 따른 재현율(Recall)과 정밀도(Precision)의 상대적 중요도**
- 재현율이 상대적으로 더 중요한 경우: 실제 positive인 데이터를 negative로 잘못 예측하면 업무상 큰 영향이 발생하는 경우 (ex. 암 진단, 금융사기 판별)
- 정밀도가 상대적으로 더 중요한 경우: 실제 negative인 데이터를 positive로 잘못 예측하면 업무상 큰 영향이 발생하는 경우 (ex. 스팸 메일)

<br>

**정밀도와 재현율의 맹정**
- 정밀도를 100%로 만드는 법: 확실한 기준이 되는 경우만 positive, 나머지는 모두 negative로 예측한다. 1 / (1 + 0)
- 재현율을 100%로 만드는 법: 모든 경우를 positive로 예측한다. 1000 / (1000 + 0)

<br>

### Confidence 임계값에 따른 Precision-Recall 변화

- Confidence 임계값이 낮을수록 더 많은 예측 Bbox를 만들게 되어 Precision은 낮아지고 Recall은 높아짐
- Confidence 임계값이 높을수록 예측 Bbox를 만드는데 신중하게 되어 Precision은 높아지고 Recall은 낮아짐

<br>

**Precision Recall Trade-off**

- confidence 임계값을 조정하면 precision 또는 recall의 수치를 높일 수 있지만, 둘은 상호 보완적인 평가 지표이기 때문에 어느 한쪽을 강제로 높이면 다른 하나의 수치는 떨어지기 쉬움

<br>

**Precision-Recall Curve**

- Recall 값의 변화에 따른 Precision 값을 나타낸 곡선
- 여기서 얻어진 Precision의 평균을 **AP(Average Precision)** 라고 하며, 일반적으로 정밀도 재현율 곡선의 면적 값으로 계산됨

<br>

**AP 계산**

- 일반적으로 AP는 지그재그 형태로 나옴
- 지그재그 형태를 최대 Precision값으로 연결해서 계단 형태로 만듦
- 그래프 너비가 AP
- 각 recall 포인트 별로 최대 precision 평균값을 구함

<br>

### mAP(mean Average Precision) 계산

- AP는 한 개 object에 대한 성능 수치
- mAP는 여러 objects의 AP를 평균한 값
