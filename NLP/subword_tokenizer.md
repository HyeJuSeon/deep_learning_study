# subword_tokenizer

- subword 토큰화 하는 이유?
  - OOV(Out Of Vocabulary): 모르는 단어로 인해 문제 풀이가 까다로워지는 상황
  - 하나의 단어는 더 작은 단위의 의미있는 여러 서브워드들의 조합
  - subword segmentation을 통해 OOV, 신조어, 희귀 단어 문제 해결 가능

<br>

## Byte Pair Encoding(BPE)

paper: https://arxiv.org/pdf/1508.07909.pdf

- 대표적인 subword 분리 알고리즘으로 데이터 압축 알고리즘
- 알고리즘 동작을 몇 회 반복할 것인지 사용자가 정함
- 가장 빈도수가 높은 유니그램 쌍을 하나의 유니그램으로 통합하는 동작

<br>

## Wordpiece Model

paper: https://static.googleusercontent.com/media/research.google.com/ko//pubs/archive/37842.pdf

구글이 Wordpiece Model을 변형하여 번역기에 사용했다는 논문 : https://arxiv.org/pdf/1609.08144.pdf

- 기존 띄어쓰기는 _, 서브워드 구분은 띄어쓰기
- BERT 훈련에 사용됨

<br>

## Unigram Language Model Tokenizer

paper: https://arxiv.org/pdf/1804.10959.pdf

- 각각의 서브워드들에 대해서 손실(loss)을 계산함 
  - 서브 단어의 손실: 해당 서브워드가 단어 집합에서 제거되었을 경우, 코퍼스의 우도(Likelihood)가 감소하는 정도 
- 서브워드들을 손실의 정도로 정렬하여, 최악의 영향을 주는 10~20%의 토큰을 제거 
- 이를 원하는 단어 집합의 크기에 도달할 때까지 반복합니다.

<br>

## SentencePiece

paper: https://arxiv.org/pdf/1808.06226.pdf

github: https://github.com/google/sentencepiece

- 사전 토큰화 작업없이 단어 분리 토큰화를 수행하므로 언어에 종속되지 않음

